# Body & Mind — Operating Playbook

Personal health/fitness tracking system for Richard. **This file auto-loads when working in
this folder — follow it whenever you touch this project.** It is the operating manual; a
scheduled weekly agent also reads it to know what to do.

## Goal & current phase
- 19M, 5'7", **~71.9 kg (Jun 19 2026)**, ~15–16% body fat.
- Goal: **single-digit body fat (~9%, ~66–67 kg) by Aug 22, 2026** (returns to Detroit) — the
  healthy way, NO crash.
- Approach: **finish this week of recomp (through Sun Jun 21) to lock true maintenance, then an
  AGGRESSIVE-BUT-HEALTHY CUT, Mon Jun 22 → Aug 22** (~8.5 wks).
  - Target rate **~0.65–0.7 kg/week** — **hard cap ~1% BW/wk; if the scale drops faster, EAT MORE.**
  - Cut calories ≈ maintenance − ~700 (start ~2,200; calibrate weekly from the weight trend).
  - The steep deficit is affordable because maintenance is HIGH (17–24k steps + lifting + added
    cardio) — deficit comes from activity, not starvation.

## Daily targets — full macro + micro dashboard

| Macro | Recomp (now, ~2,550) | Cut (~1,900–1,950 since Wk4 rollup 2026-07-12, was ~2,200) |
|---|---|---|
| Protein | 150–165 g | 170–185 g |
| Fat | 70–90 g (floor 60) | 60–75 g (floor 55) |
| Carbs | ~280–310 g | ~150–190 g |
| Fibre | ≥30 g | ≥30 g |
| Added sugar | <40 g | <30 g |

- **Sugar target is ADDED/free sugar only** (sweets, syrups, soft drink). Natural sugar in his
  fruit/yogurt is fine (comes with fibre/K/protein) — don't flag it.
- **K:Na 4:1** — sodium ≤~1,300 mg, potassium ~4,700–5,500 mg · ☕ 1 black coffee daily
- **Micros (daily):** omega-3 (EPA+DHA) ~500 mg · iron 8 mg · zinc 11 mg · magnesium ~400 mg ·
  calcium 1,000 mg · vit D 600 IU · B12 2.4 µg · vit C 90 mg · water ~3 L.
  Sources: salmon/fish-oil (omega-3); beef/beans/spinach (iron/Mg); beef/eggs/seeds (zinc);
  yogurt/milk (calcium); fruit/veg (vit C).
- **🧠 Brain/cognitive performance (he's a student — wants focus optimized):**
  **DHA** (oily fish 2–3×/wk or fish-oil) · **choline ~550 mg** (whole eggs — KEEP the yolk, beef) ·
  **flavonoids** (blueberries/berries daily) · **iron/B12/folate** (low = brain fog) ·
  **stable glucose** (complex carbs + protein/fat, cap added sugar — prevents post-meal focus dip) ·
  caffeine before 2pm + hydration. Most already covered by his eggs/salmon/blueberries/coffee/beef —
  flag DHA on non-fish days. When recommending food, factor cognition too.
## Hormone & deficiency watch (diet-inferred, no lab data — added 2026-08-15)
No blood/hormone panel exists; everything here is inferred from intake/training/sleep patterns,
never a diagnosis. Biggest risk factors present in the log: sustained deficit + high training +
a sub-10% BF target (classic low-T/RED-S setup for a lean 19M), fat intake often under the 55g
floor, chronic fibre/veg shortfall (zinc/magnesium proxy), no fatty-fish routine (omega-3 gap),
NZ winter = low sun → low vit D, and inconsistent sleep (T release is sleep-dependent — the
single biggest lever, bigger than any micro below). Thyroid: a prolonged deficit can itself
suppress T3, and the low-sodium strategy (avoiding iodized salt/processed food) may also be
cutting iodine — watch for cold intolerance/fatigue/hair thinning beyond normal cut fatigue.
- **Current supplement stack:** creatine 5g/day, whey (1–2 scoops/day), occasional vit C.
- **Added 2026-08-15 (foundational repletion, NOT hormone boosters):** vitamin D3 1,000–2,000
  IU/day (biggest single gap — winter + sparse dietary sources + direct testosterone-receptor
  link), magnesium glycinate/citrate ~300–400mg before bed (sleep + the cramping already flagged
  in lift notes + modest T support when deficient), zinc 15–25mg/day (take away from
  dairy/calcium — competes for absorption), fish oil/omega-3 ~1–2g EPA+DHA/day (already a food
  target that's rarely hit — also covers the cognition goal above). Log these like any other
  item once Richard confirms he's actually taking them.
- **Explicitly NOT recommending:** DHEA, "test boosters," or any other hormone-adjacent
  product — unproven/unregulated and inappropriate to add speculatively for a 19M; foundational
  nutrient repletion first, always.
- **Real answer needs labs, not inference.** If Richard wants ground truth: a basic panel
  (total/free T, TSH + free T4, 25-OH vit D, ferritin) — ideally drawn **after Aug 22**, since
  mid-cut numbers read artificially low and aren't his baseline.
- **Flag in rollups:** libido/mood/cold-intolerance/energy crash (already a guardrail below) is
  the real-world signal in the absence of labs — weight it far more than any single micro number.

- **Cardio:** 12k+ steps/day · 2–3 zone-2 walks + 1–2 VO2 interval sessions/wk · **keep lifting heavy**
- **Diet break:** ~5 days at maintenance around late July
- **Back off (eat more / rest) if:** strength tanking, sleep/mood/energy/libido crash, or always cold
- **Recomp through Sun Jun 21 (done today):** locks the maintenance number; cut starts Mon Jun 22.
- **Fixed daily intake** (breakfast + whey) — see food-log.md
- **When recommending food, check ALL goals** — carbs, **fat ≥floor**, fibre, K:Na, *and* cut-micros
  (omega-3, iron, zinc, magnesium, calcium, B12) — not just protein. Flag if he's low on fat or a
  micro that day, and note how the food fits (e.g. salmon → omega-3 + fat; beans → fibre/iron/Mg).

## Cookbook
- `cookbook_recipes.md` — **128 recipes** extracted from *The Ultimate Anabolic Cookbook 2.0* by Greg Doucette, with per-serving macros + tags (high-protein, low-cal, high-fiber, quick, vegetarian, gluten-free). When recommending meals, **read this file first** and pick from it, or generate a new recipe, or fetch one online — your choice based on what fits the day's macro gaps.

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

## Lift tracking (Google Sheet)
- Public link-shared sheet, ID `1LHBsbA47Hq9KnhW0Gy5SpD6bnLQBLfuqkohJECdD2u0`.
- **Find the current block:** `curl -sL ".../htmlview"` → list `The Great Reset N` tabs + gids
  (regex `name: "(The Great Reset \d+)"[^}]*?gid=(\d+)`) → use the **highest N** (newest week).
- **Export it:** `curl -sL ".../export?format=csv&gid=<GID>"`.
- **Columns:** A Day · B Exercise · C–H coach's prescription (reps/sets/RPE/weight/rest/notes) ·
  **I Actual Weight · J Actual Reps · K Actual Effort · L his notes** ← his real lifts are I–L.
- **New tab each week** (Great Reset 3, 4, …) — always read the highest N. Confirmed Jun 21.
  **Training week resets on WEDNESDAYS** (block began a Wednesday), so a new tab appears each Wed.
  The Sunday rollup lands mid-training-week → current tab is partially filled; that's expected.
- **"History" via snapshot-diff:** save each tab to `lifts/<tab-slug>.csv` (e.g. great_reset_2.csv);
  each check, re-pull the current tab and diff vs its saved snapshot to see what's new this week
  (Google revision history isn't accessible). A brand-new tab = a new week's session.
- **Use it for the cut:** watch main lifts (squat/bench/deadlift) — holding/climbing = muscle safe;
  2+ sessions dropping = deficit too steep, eat more / deload. (Baseline in progress.md.)

## Tone — honest adviser ("Jarvis")
- **Never fabricate data.** E.g., the Fitbit Web API does not expose the real Sleep Score and is
  sunsetting ~Sept 2026 — Richard reports sleep manually.
- Push back on crash-diet / grey-area impulses; keep it sustainable and evidence-based.
