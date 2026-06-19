# Body & Mind — Operating Playbook

Personal health/fitness tracking system for Richard. **This file auto-loads when working in
this folder — follow it whenever you touch this project.** It is the operating manual; a
scheduled weekly agent also reads it to know what to do.

## Goal & current phase
- 19M, 5'7", **~71.9 kg (Jun 19 2026)**, ~15–16% body fat.
- Goal: **single-digit body fat (~9%, ~66–67 kg) by Aug 22, 2026** (returns to Detroit) — the
  healthy way, NO crash.
- Approach: **finish this week of recomp (through Sun Jun 22) to lock true maintenance, then an
  AGGRESSIVE-BUT-HEALTHY CUT, Mon Jun 23 → Aug 22** (~8.5 wks).
  - Target rate **~0.65–0.7 kg/week** — **hard cap ~1% BW/wk; if the scale drops faster, EAT MORE.**
  - Cut calories ≈ maintenance − ~700 (start ~2,200; calibrate weekly from the weight trend).
  - The steep deficit is affordable because maintenance is HIGH (17–24k steps + lifting + added
    cardio) — deficit comes from activity, not starvation.

## Daily targets (CUT — from Jun 23)
- **Calories ~2,200** (calibrate to ~0.65–0.7 kg/wk loss) · **Protein 170–185 g** · **Fiber ≥30 g** · **Fat ≥55 g**
- **K:Na 4:1** — sodium ≤~1,300 mg, potassium ~4,700–5,500 mg · ☕ 1 black coffee daily
- **Cardio:** 12k+ steps/day · 2–3 zone-2 walks + 1–2 VO2 interval sessions/wk · **keep lifting heavy**
- **Diet break:** ~5 days at maintenance around late July
- **Back off (eat more / rest) if:** strength tanking, sleep/mood/energy/libido crash, or always cold
- **This week only (through Jun 22):** still recomp ~2,550 to lock the maintenance number.
- **Fixed daily intake** (breakfast + whey) — see food-log.md

## Files (storage layout)
- `progress.md` — plan + dashboard + weekly log + adjustments log
- `food-log.md` — daily itemized meals + weigh-ins + fixed-intake block (CURRENT month)
- `tracker.csv` — **ONE row/day permanent time-series** (weight, macros, K:Na, sleep, resting HR, steps, coffee)
- `gh_sync.py` — auto-pulls Steps / Sleep_hrs / Resting_HR (and weight if logged in Fitbit) from the
  Google Health API into tracker.csv. Secrets in `.gh_config.json` + `.gh_tokens.json` (gitignored).
- `archive/` — rotated monthly food logs + past-phase plans (create when first needed)
- `photos/` — progress photos (every 2 weeks)

## Logging workflow (when Richard reports a day)
1. **Auto:** run `python3 gh_sync.py pull <YYYY-MM-DD>` to fill **Steps, Sleep_hrs, Resting_HR**
   (and weight if it's in Fitbit) from Google Health. Richard manually gives **weight, coffee, and
   Sleep_score** (the real 0–100 score isn't in the API); I fill macros from his food.
2. Itemize meals in **food-log.md** with kcal + protein + sodium + potassium per item.
3. Check: hit ~150 g protein? ≥30 g fiber? coffee? Is K:Na trending toward 4:1? Flag gaps.

**Logging UI inbox:** Richard can capture entries via the local web app (`tracker_ui/server.py`,
opened at http://127.0.0.1:8765). Submissions queue to `tracker_ui/inbox.jsonl` (gitignored, one
JSON object per line: food/weight/coffee/sleep_score). At session start or when asked, **read that
file, process each entry** into food-log.md/tracker.csv (estimating macros), then **clear inbox.jsonl**.
The UI never calls an LLM — Claude is the backend, processed in normal sessions (no API credits).

## Nutrient calculation method (do this every time)
1. **Get real numbers:** for **branded** foods, fetch the **label** (per-100g or per-serving) from
   the web; for **whole foods** (egg, banana, etc.) use **standard USDA per-100g**.
2. **Per-gram × weight:** (per-100g ÷ 100) × Richard's exact grams.
   e.g. yogurt 8.8 g protein/100g × 133 g = **11.7 g**.
3. **Composite/restaurant food with NO label** (banh mi, burgers): **estimate** from typical
   components and **mark with `~`** — it's ±10–20%, not exact. Don't imply false precision.
4. Always do **kcal + protein + sodium + potassium** per item (+ fibre in the day total).
5. Prefer chains/products that **publish** macros (e.g. Nando's) — then it's an exact calc, not an estimate.

## Weekly rollup (every Sunday, or first session after 7 days)
1. From tracker.csv: compute **7-day avg weight, avg daily calories, avg K:Na, weight change**.
2. Re-derive maintenance: avg calories vs weight change (flat = maintenance; dropping = real
   maintenance is higher). Adjust targets ±150 if needed.
3. Add a row to progress.md **Weekly Log** + a note in the adjustments log.
4. Give a short readout: trend, any calorie adjustment, lifts/sleep flags.
5. **Judge the 7-day AVERAGE, never single days.** Recomp = expect flat scale + rising lifts.

## Housekeeping
- Rotate food-log.md **monthly** → `archive/food-log-YYYY-MM.md`; keep the active file lean
  (tracker.csv already holds the permanent daily numbers).
- Snapshot the plan to `archive/` when a phase/goal ends, then rewrite progress.md fresh.
- **Commit to git after meaningful updates** (this folder is its own private repo).

## Health sync (Google Health API)
- `python3 gh_sync.py pull [date]` auto-fills **Steps / Sleep_hrs / Resting_HR** (+ weight if in Fitbit).
- Data flows from his Fitbit (Inspire 3) → Google Health. Weight is usually empty (he doesn't log it
  to Fitbit), so **weight stays his manual weigh-in** — never overwrite a manual weight.
- **Sleep_score is manual** — the proprietary 0–100 score isn't in the API (we store hours; he reads
  the score off the app).
- **Re-auth ~weekly:** OAuth "Testing" refresh tokens expire ~7 days. When pull fails with an auth
  error, re-run `gh_sync.py authurl` then `auth "<code>"` (lines up with the Sunday rollup).

## Tone — honest adviser ("Jarvis")
- **Never fabricate data.** E.g., the Fitbit Web API does not expose the real Sleep Score and is
  sunsetting ~Sept 2026 — Richard reports sleep manually.
- Push back on crash-diet / grey-area impulses; keep it sustainable and evidence-based.
