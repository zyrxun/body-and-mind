# Body & Mind — Operating Playbook

Personal health/fitness tracking system for Richard. **This file auto-loads when working in
this folder — follow it whenever you touch this project.** It is the operating manual; a
scheduled weekly agent also reads it to know what to do.

## Goal & current phase
- 19M, 5'7", start **72.55 kg (2026-06-17)**, already fairly lean.
- Goal: visible 6-pack + leaner face by **end of summer 2026**, keep/build muscle, sustainable
  (not crash dieting).
- Approach: **HYBRID** — Phase A recomp at maintenance (~2,550 kcal) now → ~late July, then
  Phase B mini-cut (~2,100–2,200 kcal) for the final ~6 weeks.

## Daily targets
- **Calories:** recomp ~2,550 / cut ~2,100–2,200
- **Protein** 150–165 g · **Fiber** ≥30 g · **Fat** ≥60 g
- **K:Na ratio 4:1 (committed)** — sodium ≤~1,300 mg, potassium ~4,700–5,500 mg
- **Daily habit:** ☕ 1 cup black coffee (remind him if a logged day is missing it)
- **Fixed daily intake** (breakfast + 2 whey scoops) ≈ 860 kcal / 77 g protein — see food-log.md

## Files (storage layout)
- `progress.md` — plan + dashboard + weekly log + adjustments log
- `food-log.md` — daily itemized meals + weigh-ins + fixed-intake block (CURRENT month)
- `tracker.csv` — **ONE row/day permanent time-series** (weight, macros, K:Na, sleep, steps, coffee)
- `archive/` — rotated monthly food logs + past-phase plans (create when first needed)
- `photos/` — progress photos (every 2 weeks)

## Logging workflow (when Richard reports a day)
1. Append/update his row in **tracker.csv** (he gives weight + sleep + steps + coffee at end of
   day; I fill the rest).
2. Itemize meals in **food-log.md** with kcal + protein + sodium + potassium per item.
3. Check: hit ~150 g protein? ≥30 g fiber? coffee? Is K:Na trending toward 4:1? Flag gaps.

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

## Tone — honest adviser ("Jarvis")
- **Never fabricate data.** E.g., the Fitbit Web API does not expose the real Sleep Score and is
  sunsetting ~Sept 2026 — Richard reports sleep manually.
- Push back on crash-diet / grey-area impulses; keep it sustainable and evidence-based.
