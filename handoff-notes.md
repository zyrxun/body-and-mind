# Session Handoff — 2026-06-23

### 🎯 What We Were Working On
Built and are now actively running **"Body & Mind"** — a personal health/fitness tracking system for Richard's cut. This session went from designing the diet plan → building the whole tooling stack → daily food/lift/health logging. Currently on **Day 2 of the cut**.

### 🌿 Branch & Environment
- **Git:** two private GitHub repos — `zyrxun/body-and-mind` (health) and `zyrxun/finance` (ledger). Branch `main`.
- **Secrets (gitignored, local only):** `.gh_config.json`, `.gh_tokens.json` (Google Health OAuth).
- **Automation:** launchd agent `com.bodymind.healthsync` (8am + 11:55pm) runs `sync_cron.sh`.
- **Connectors authed:** Google Calendar (weekly reminders), Google Health API (via gh_sync.py).
- **No package deps** — everything is Python stdlib.

### ✅ What Was Completed
- [x] Full diet plan: **aggressive-but-healthy CUT** (Jun 22 → Aug 22) to single-digit BF, ~2,200 kcal, protein 170–185g
- [x] `tracker.csv` (daily time-series), `food-log.md` (itemized), `progress.md` (plan, now in cut mode), `WORKFLOW.md`, `CLAUDE.md` (playbook)
- [x] **Google Health API sync** (`gh_sync.py`) — auto-pulls steps/sleep/resting-HR; launchd 2×/day
- [x] **Lift tracking** — reads Google Sheet (cols I–L) "The Great Reset N" tabs, snapshot-diff
- [x] **Local logging UI** (`tracker_ui/`, port 8642) → queues to inbox.jsonl, Claude processes
- [x] Custom goals baked into playbook: **K:Na 4:1**, fibre ≥30g, brain/cognition nutrients, full macro+micro targets, holistic food-rec rule
- [x] Weekly Sunday calendar reminders (Auckland → Aug 16, Detroit from Aug 23) with embedded prompts
- [x] Logged Jun 17–23; first weekly rollup done Jun 21

### 🔧 Decisions Made
| Decision | Why |
|----------|-----|
| Aggressive cut (~0.65–0.7 kg/wk), hard Aug 22 deadline | Richard chose it after hearing trade-offs; honor "no crash" guardrails |
| Inbox processing kept MANUAL (no auto `claude -p` agent) | Auto-mode blocked a skip-permissions launchd agent; Richard agreed manual is safer |
| Health sync = launchd not cron | Cron misses runs when laptop asleep; launchd catches up on wake |
| Weigh-ins: judge 7-day fasted avg only | Daily scale is water/food noise, esp. early cut |

### 💸 Technical Debt / ⚠️ Known Issues
- [ ] **Google OAuth is "Testing" mode → refresh token expires ~weekly.** Re-auth: `gh_sync.py authurl` → `auth "<code>"` (lines up w/ Sunday rollup).
- [ ] **Steps undercounted some days** (Fitbit Inspire 3 off during part of a session). Jun 22 logged 10,391 but real was higher.
- [ ] **Weight does NOT auto-sync** — Richard doesn't log weight to Fitbit, so weigh-ins are manual.
- [ ] **CSV comma bug (FIXED):** never put unquoted commas in tracker.csv Notes via manual Edit — it overflowed DictReader and dropped a row. gh_sync.py now folds overflow back into Notes. Use semicolons/dashes in notes.
- [ ] `tracker_ui/` Week 1 summary block in food-log.md is stale (says 0/7) — never updated.

### 📂 Key Files Touched (all in `body and mind/`)
- `CLAUDE.md` — operating playbook (auto-loads); cut targets, K:Na, brain nutrients, lift-sheet method, calc method
- `tracker.csv` — daily rows (Jun 17–23)
- `food-log.md` — itemized meals
- `progress.md` — full cut-mode plan + weekly log
- `gh_sync.py` — Google Health sync (hardened against comma bug)
- `sync_cron.sh` + `healthsync.plist` — launchd automation
- `tracker_ui/server.py` + `index.html` — logging UI
- `WORKFLOW.md` — user's daily/weekly routine

### 🔜 Next Steps
1. **Day 2 (Jun 23) in progress:** breakfast logged (oats bowl, 46g protein). Gave a low-sodium lunch rec; **waiting for Richard to report lunch**. Then dinner. Keep today low-sodium (yesterday's smoked salmon blew sodium budget).
2. **New training week starts Wed Jun 24** on the lift sheet (new "Great Reset" tab) — pull + log his session.
3. **Next weekly rollup: Sun Jun 28** — recalc maintenance from the cut's first-week loss rate; adjust calories.
4. Encourage **clean fasted weigh-ins** (before any food) — today's was post-bites.

### 🧠 Brain Dump
**Mental model:** Richard logs food/weight/coffee/sleep-score in chat (or UI inbox). Claude estimates macros (per-gram from labels × weight; `~` for label-less foods), updates food-log.md + tracker.csv, commits/pushes each time. Health data (steps/sleep/HR) auto-syncs via launchd. Lifts read from a public Google Sheet. Everything judged on weekly averages.

**Momentum note:** Just gave a low-sodium lunch rec (chicken + bean + avocado bowl, to fix today's low fat at 12g vs 55 floor). Day 2 status: ~492 kcal, 46g protein, K:Na 3.6:1 so far; ~1,710 cal + ~125g protein left.

**Current cut numbers:** Start 71.10 kg fasted (Jun 22) → target ~66–67 kg single-digit BF by Aug 22. Fasted trend ~71.3. Maintenance est HIGH (~2,700–2,900, from 17–25k steps).

**The Hack Log:** Use semicolons not commas in tracker Notes. Steps may be undercounted. Salmon was smoked (Aoraki, 980mg Na/100g) — flag smoked/cured/brined/pickled as high-sodium always.

**Last successful prompt:** "gimme a low sodium lunch rec" → returned the chicken+bean+avocado bowl with full macro/micro fit.
