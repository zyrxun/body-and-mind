# Body & Mind — How It Works & Your Workflow

## The system in one picture
**You input** food / weigh-in / coffee / sleep score (UI, chat, or phone).
**Automation + Claude do the rest:**
- **8:00am (automatic)** — cron pulls **steps + sleep hours + resting HR** from Google Health → `tracker.csv`.
- **Food → macros** — when you're at your computer, say **"process my inbox"** and Claude turns your
  logged meals into kcal/protein/Na/K and updates the tracker. *(Kept manual on purpose — the estimates
  are judgment calls worth a quick glance, not a silent unattended commit.)*

Everything lives in `tracker.csv` (permanent record) + `food-log.md` (detail), backed up to the private repo.

---

## What YOU do

### Daily (~2 minutes)
1. **Weigh in fasted** (first thing, before eating/drinking) → enter in the UI.
2. Check your **Fitbit Sleep Score** → enter in the UI.
3. Have your **black coffee** → tap it in the UI.
4. **Log each meal** as you eat → free text in the UI (e.g. *"chicken banh mi 326g, extra mayo"*).
5. Once at your computer, say **"process my inbox"** → Claude logs the day's food into the tracker.

### Weekly — Sunday (~5 min)
6. If the health sync's been failing (~weekly token expiry), re-auth:
   `python3 gh_sync.py authurl` → open URL → `python3 gh_sync.py auth "<code>"`.
7. Say **"do my weekly Body & Mind rollup"** → 7-day avg weight, avg calories, maintenance re-check, readout.

---

## What's AUTOMATIC (you never touch)
- Steps, sleep hours, resting HR — 8am cron (`sync_cron.sh`).
- Commits + pushes of the health data.

## Phases
- **Now → ~late July: RECOMP** — eat ~**2,550 kcal** (maintenance), push lifts. Flat scale + rising lifts = winning.
- **~late July → summer: MINI-CUT** — drop to ~**2,100–2,200**. Claude flags the switch.

## Daily targets
~2,550 kcal · **protein 150–165 g** · **fibre ≥30 g** · fat ≥60 g · **K:Na 4:1** · 1 black coffee.

## Manual commands (optional)
- **UI:** `python3 "tracker_ui/server.py"` → open the printed `http://127.0.0.1:8642`
- **Pull health now:** `python3 gh_sync.py pull`
- **Process food logs:** say *"process my inbox"* in a Claude session.

## Files
- `tracker.csv` — permanent time-series · `food-log.md` — itemized meals
- `CLAUDE.md` — operating playbook (auto-loads) · `gh_sync.py` + `sync_cron.sh` — health sync
- `tracker_ui/` — input web app · logs gitignored · Private repo: **github.com/zyrxun/body-and-mind**
