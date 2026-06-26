# Session Handoff — 2026-06-27

### 🎯 What We Were Working On
Continuing the **"Body & Mind" cut tracking** — daily food logging, macro estimation, lift tracking, and health sync for Richard's Jun 22 → Aug 22 aggressive-but-healthy cut. This session covered Days 2–4 of the cut (Jun 23–25) plus a sick day (Jun 26).

### 🌿 Branch & Environment
- **Git:** `zyrxun/body-and-mind`, branch `main`. All changes committed + pushed each session.
- **Secrets (gitignored):** `.gh_config.json`, `.gh_tokens.json` (Google Health OAuth).
- **Automation:** launchd `com.bodymind.healthsync` (8am + 11:55pm) runs `sync_cron.sh`.
- **Google OAuth:** "Testing" mode — refresh token expires ~weekly. Re-auth: `gh_sync.py authurl` → `auth "<code>"`. Due around Sun Jun 28 rollup.
- **No package deps** — Python stdlib only.

### ✅ What Was Completed
- [x] **Jun 23 (Day 2):** Full day logged — breakfast (oats bowl), lunch (John West salmon + wedges + avocado), dinner (Chinese family: tofu+beef mince dish + pumpkin + Hainanese chicken rice + pork ribs). Totals: ~1,827 kcal / 126g P (short — no post-WO whey) / 69g F / 22g fibre. Na over from Chinese cooking.
- [x] **Jun 24 (Day 3):** Full day logged — breakfast (yogurt/berries/egg/banana/½ whey/oats/honey/sourdough pre-WO), MuscleTech Shatter pre-WO, lunch (springwater tuna + gizzard 203g + soup 400g), C4 post-WO whey, dinner (galbi 223.4g edible + broccoli + leftover soup). Totals: ~2,048 kcal / 178g P ✅ / 74g F ✅ / 20g fibre / Na over (family galbi).
- [x] **Great Reset 3 (Week 3) lift sheet pulled + snapshotted** (`lifts/great_reset_3.csv`). Day 1 lifts confirmed: squat 102.5kg×8 ✅ bench 75kg×4 ✅ — all targets hit on cut. Leg press/hamstring/leg extension/lat-pulldown accessories done.
- [x] **Jun 25 (Day 4):** Breakfast logged (yogurt/berries/½ whey/banana/egg — ~392 kcal / 34g P). Steps 13,126 ✅. Food untracked rest of day — session credits ran out.
- [x] **Jun 26:** Sick day. Rest, no training. Steps 1,357. Sleep 8.63h. Food untracked.
- [x] **Health data synced** for Jun 25 + Jun 26 via gh_sync.py.
- [x] **Tonsil stones discussed** — diagnosed likely cause: dairy residue from thick whey shakes sitting in throat crypts. Fix: gargle/rinse with water immediately after every shake and yogurt. He's already at 3L/day so dehydration ruled out.
- [x] **Coffee vs pre-workout resolved:** Pre-WO (200mg caf) replaces coffee on training days. Rest days = 1 black coffee before 2pm. Stop flagging "no coffee" on gym days.

### 🔧 Decisions Made
| Decision | Why |
|---|---|
| Pre-WO Shatter counts as daily caffeine source on training days | 200mg caf from Shatter > double-shot coffee; stacking both unnecessary and jittery |
| Tuna mercury: 2 cans of John West skipjack = fine | Skipjack is lowest-mercury tuna (~0.012 ppm); concern is for pregnant women/kids, not healthy adult males |
| Wang Korean BBQ sauce Na: calculated per-serving not per-100g | 1/3 bottle for 2kg meat; his ~223g = 11% of total → ~11.6g sauce absorbed → ~220mg Na from sauce |
| Sick day (Jun 26): don't stress deficit | Illness + undereating accelerates muscle loss — eat enough protein, rest, hydrate |
| Skip tuna cans on high-Na days | Springwater tuna ~250mg Na/can; reserve for days with fresh Na budget |

### ⚠️ Known Issues / Blockers
- [ ] **Jun 25 food log incomplete** — only breakfast logged before credits ran out. Macro row in tracker.csv is blank for the full day. Pick up tomorrow as a new day; don't try to reconstruct.
- [ ] **Jun 26 food log blank** — sick day, intentionally skipped. Note in tracker says "Sick day; rest; food untracked."
- [ ] **Google OAuth re-auth due ~Jun 28** (weekly expiry). Run `gh_sync.py authurl` → `auth "<code>"` during Sunday rollup.
- [ ] **Week 1 summary block in food-log.md** still shows "0/7 days logged" — stale placeholder, never updated.
- [ ] **Sleep score Jun 26** — not yet captured (was sick). Ask at next session.
- [ ] **Weekly rollup due Sun Jun 28** — first cut-week rollup. Need to recalculate maintenance from weight trend and decide if 2,200 kcal target needs adjusting.
- [ ] **Great Reset 3 Day 2+ lifts** — only Day 1 filled in. Pull updated snapshot when he next trains.

### 📂 Key Files Touched
- `body and mind/food-log.md` — Days 2–4 logged (Jun 23–25); Week 2 section added starting Jun 24
- `body and mind/tracker.csv` — rows Jun 23–26 updated with macros/health data/sleep scores
- `body and mind/lifts/great_reset_3.csv` — new file; Week 3 lift sheet snapshotted + Day 1 actuals saved
- `body and mind/handoff-notes.md` — this file

### 🔜 Next Steps
1. **Jun 27 (today):** Fasted weigh-in + breakfast report — resume normal logging. He's still a bit sick so keep meals light/nourishing. Don't push hard training.
2. **Sun Jun 28 — weekly rollup:** Pull tracker.csv rows Jun 22–28, compute 7-day avg weight + avg daily kcal, derive implied maintenance, adjust cut target if needed. Update progress.md Weekly Log. Re-auth Google OAuth.
3. **Pull Great Reset 3 sheet again** when he next trains — diff against snapshot to see new Day 2+ lifts.
4. **Tonsil stones follow-up** — ask if gargle-after-shakes routine is helping after ~1 week.
5. **Salmon** — 822g was marinated (lemon/garlic/ginger/honey/olive oil, zero added salt) for family dinner Jun 25. May or may not have been eaten; ask.

### 🧠 Brain Dump

**Weight trend (cut so far):**
- Cut start: 71.10 kg fasted (Jun 22)
- Jun 24: 70.75 kg fasted ✅
- Jun 25: 70.50 kg fasted ✅
- Jun 26: sick day, weight unknown
- 7-day avg as of Jun 25: ~71.19 kg (slow movement = correct; daily drops are water noise)
- Target rate: 0.65–0.7 kg/wk. Trend is healthy — don't adjust calories until Sunday rollup.

**Macro patterns observed:**
- Fat floor (55g) is hard to hit without olive oil or fatty fish — gizzard/tuna are too lean alone. Always need an oil source or fatty fish.
- Fibre consistently short (20–22g vs 30g target) — needs beans/lentils at lunch or dinner daily.
- Protein easy to hit on training days with whey; hard on rest days with only family food.
- Sodium busts on Chinese family dinner nights — unavoidable; compensate next day.

**Sodium cheat sheet (from this session):**
- John West springwater tuna 95g can: ~250mg Na
- John West Wild Alaskan Pink Salmon 210g drained: ~577mg Na; omega-3 1,665mg ✅
- Wang Korean BBQ sauce: ~1,900mg Na/100g (contains soy sauce despite mum saying "no soy" — it's in the ingredients)
- Galbi with homemade Wang sauce (1/3 bottle / 2kg meat, ~223g serving): ~354mg Na total
- MuscleTech Shatter 1 scoop: ~40mg Na, 200mg caffeine
- C4 Hershey's whey 1 scoop: ~130 kcal, 25g protein, 110mg Na
- Aoraki cold-smoked salmon: 980mg Na/100g — HIGH, flag always

**Food preferences / family meal patterns:**
- Mum cooks Chinese family dinners regularly (tofu+beef mince, Hainanese chicken rice, galbi, pork+pumpkin soup)
- Family has salt-reduced chicken broth on hand (~150mg Na/100ml)
- He has: Greek yogurt (The Collective More-Than-Protein), frozen blueberries, eggs, bananas, whey (C4 + Ugly Face), oats as fixed daily items
- He likes: Korean food, Chinese family meals, sushi, poke bowls, Nando's, GYG

**Mental model:** Richard logs food/weight/coffee/sleep-score in chat. Claude estimates macros (per-gram from labels × weight; `~` for restaurant/label-less), updates food-log.md + tracker.csv, commits+pushes each time. Health data auto-syncs via launchd. Lifts read from Google Sheet "The Great Reset N" (highest tab = current week; cols I–L = actuals). Judge everything on 7-day averages.

**The Hack Log:**
- Use semicolons not commas in tracker.csv Notes field
- Jun 23 weight (71.35) was post-few-bites — flagged as noise, not clean fasted
- Steps undercounted Jun 22 (Fitbit off during walk)
- Wang sauce "no soy" claim from mum — the product DOES contain soy sauce in ingredients; sodium calculated from label anyway

**Last successful prompt:**
"70.50kg fasted. 155.2g greek yogurt, 51.7 frozen blueberries, 1/2 scoop of c4 whey 176.8 banana and 1 boiled egg" → Claude logged breakfast, pulled health sync, gave remaining targets for the day.
