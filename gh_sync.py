#!/usr/bin/env python3
"""Google Health API sync for the Body & Mind tracker.

Commands
--------
  python3 gh_sync.py authurl                # print the authorization URL
  python3 gh_sync.py auth "<code>"          # exchange code -> tokens (.gh_tokens.json)
  python3 gh_sync.py raw <dataType> [n]     # dump n recent raw data points
  python3 gh_sync.py pull [YYYY-MM-DD]      # default: yesterday -> writes tracker.csv

Auto-fills tracker.csv: Steps, Sleep_hrs, Resting_HR, Weight_kg (only if logged in Fitbit).
Sleep_score stays MANUAL — the proprietary 0-100 score isn't exposed by the API.

Secrets live in .gh_config.json / .gh_tokens.json (both gitignored).
Note: OAuth "Testing" apps' refresh tokens expire ~weekly; re-run authurl/auth then.
"""
import csv, json, os, sys, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, ".gh_config.json")
TOKENS = os.path.join(HERE, ".gh_tokens.json")
TRACKER = os.path.join(HERE, "tracker.csv")
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://health.googleapis.com/v4"


# ---------- config / tokens ----------
def _load(p):
    with open(p) as f:
        return json.load(f)


def _save(p, d):
    with open(p, "w") as f:
        json.dump(d, f, indent=2)


def _cfg():
    c = _load(CONFIG)
    if "PASTE" in c.get("client_secret", ""):
        sys.exit("⚠️  Add your Client Secret to .gh_config.json first.")
    return c


def _post(url, fields):
    req = urllib.request.Request(url, data=urllib.parse.urlencode(fields).encode(), method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} from token endpoint:\n{e.read().decode()}")


# ---------- auth ----------
def cmd_authurl():
    c = _cfg()
    p = {"client_id": c["client_id"], "redirect_uri": c["redirect_uri"], "response_type": "code",
         "scope": " ".join(c["scopes"]), "access_type": "offline", "prompt": "consent"}
    print("\nOpen this URL, approve, then copy the 'code' value from the google.com redirect:\n")
    print(AUTH_URL + "?" + urllib.parse.urlencode(p))


def cmd_auth(code):
    c = _cfg()
    tok = _post(TOKEN_URL, {"code": urllib.parse.unquote(code.strip()), "client_id": c["client_id"],
                            "client_secret": c["client_secret"], "redirect_uri": c["redirect_uri"],
                            "grant_type": "authorization_code"})
    if "refresh_token" not in tok:
        print("⚠️  No refresh_token returned — re-run authurl.")
    _save(TOKENS, tok)
    print("✅ Saved tokens to .gh_tokens.json")


def _token():
    c, t = _cfg(), _load(TOKENS)
    return _post(TOKEN_URL, {"client_id": c["client_id"], "client_secret": c["client_secret"],
                             "refresh_token": t["refresh_token"], "grant_type": "refresh_token"})["access_token"]


# ---------- api ----------
def _fetch(data_type, token, filt=None, page_size=10000, paginate=True):
    pts, page = [], None
    while True:
        params = {"pageSize": page_size}
        if filt:
            params["filter"] = filt
        if page:
            params["pageToken"] = page
        url = f"{API}/users/me/dataTypes/{data_type}/dataPoints?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req) as r:
                data = json.load(r)
        except urllib.error.HTTPError as e:
            sys.exit(f"HTTP {e.code} from {data_type}:\n{e.read().decode()}")
        pts += data.get("dataPoints", [])
        page = data.get("nextPageToken")
        if not page or not paginate:
            break
    return pts


def cmd_raw(data_type, n=5):
    print(json.dumps({"dataPoints": _fetch(data_type, _token(), page_size=n, paginate=False)}, indent=2))


# ---------- per-metric extraction ----------
def _local_date(ts, off):
    dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return (dt + timedelta(seconds=int(str(off).rstrip("s")))).date()


def get_steps(token, d):
    nxt = d + timedelta(days=1)
    filt = (f'steps.interval.civil_start_time >= "{d.isoformat()}" '
            f'AND steps.interval.civil_start_time < "{nxt.isoformat()}"')
    pts = _fetch("steps", token, filt)
    return sum(int(p["steps"]["count"]) for p in pts if p.get("steps", {}).get("count")) if pts else None


def get_sleep_hours(token, d):
    # sleep doesn't support interval filtering server-side; fetch recent sessions
    # (newest first) and match the one whose wake (local end) date == d.
    best = None
    for p in _fetch("sleep", token, page_size=31, paginate=False):
        s = p.get("sleep", {})
        iv = s.get("interval", {})
        if iv.get("endTime") and _local_date(iv["endTime"], iv.get("endUtcOffset", "0s")) == d:
            m = int(s.get("summary", {}).get("minutesAsleep", 0))
            best = m if best is None else max(best, m)
    return round(best / 60, 2) if best else None


def get_resting_hr(token, d):
    for p in _fetch("daily-resting-heart-rate", token, page_size=40, paginate=False):
        r = p.get("dailyRestingHeartRate", {})
        dt = r.get("date", {})
        if (dt.get("year"), dt.get("month"), dt.get("day")) == (d.year, d.month, d.day):
            return int(r["beatsPerMinute"])
    return None


def get_weight_kg(token, d):
    for p in _fetch("weight", token, page_size=50, paginate=False):
        w = p.get("weight", {})
        dt = w.get("sampleTime", {}).get("civilTime", {}).get("date", {})
        if (dt.get("year"), dt.get("month"), dt.get("day")) == (d.year, d.month, d.day):
            return round(w["weightGrams"] / 1000, 2)
    return None


# ---------- tracker.csv ----------
def update_tracker(d, fields):
    with open(TRACKER, newline="") as f:
        reader = csv.DictReader(f)
        header, rows = reader.fieldnames, list(reader)
    # Safety net: a stray unquoted comma in Notes makes DictReader overflow into a
    # None key, which then crashes DictWriter. Fold any overflow back into Notes.
    for r in rows:
        extra = r.pop(None, None)
        if extra:
            r["Notes"] = (r.get("Notes") or "") + " " + " ".join(str(x) for x in extra)
    ds = d.isoformat()
    row = next((r for r in rows if r["Date"] == ds), None)
    if row is None:
        row = {c: "" for c in header}
        row["Date"] = ds
        row["Phase"] = rows[-1]["Phase"] if rows else "Recomp"
        rows.append(row)
    for k, v in fields.items():
        if v in (None, ""):
            continue
        if k == "Weight_kg" and row.get("Weight_kg"):
            continue  # never clobber a manual weigh-in
        row[k] = str(v)
    rows.sort(key=lambda r: r["Date"])
    with open(TRACKER, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)


def cmd_pull(date_str):
    token = _token()
    d = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else (datetime.now() - timedelta(days=1)).date()
    f = {"Steps": get_steps(token, d), "Sleep_hrs": get_sleep_hours(token, d),
         "Resting_HR": get_resting_hr(token, d), "Weight_kg": get_weight_kg(token, d)}
    update_tracker(d, f)
    print(f"Pulled {d}: steps={f['Steps']}  sleep_h={f['Sleep_hrs']}  "
          f"resting_hr={f['Resting_HR']}  weight_kg={f['Weight_kg']}")
    print("→ tracker.csv updated. (Sleep_score stays manual — not exposed by the API.)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == "authurl":
        cmd_authurl()
    elif a[0] == "auth" and len(a) >= 2:
        cmd_auth(a[1])
    elif a[0] == "raw" and len(a) >= 2:
        cmd_raw(a[1], int(a[2]) if len(a) >= 3 else 5)
    elif a[0] == "pull":
        cmd_pull(a[1] if len(a) >= 2 else None)
    else:
        print(__doc__)
