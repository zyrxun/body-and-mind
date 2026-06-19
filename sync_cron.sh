#!/bin/bash
# Health sync — run by launchd (8am + 11:55pm; launchd runs missed jobs when the
# laptop wakes, so a closed-lid 8am won't be skipped like cron did).
# Pulls YESTERDAY (complete day incl. its sleep) and TODAY (overnight sleep + steps).
# Pure script — no Claude, no API credits. Idempotent, safe to run repeatedly.
DIR="/Users/richard/claude-workspace/body and mind"
cd "$DIR" || exit 1
echo "===== $(date) ====="
git pull --rebase --quiet 2>/dev/null
/opt/homebrew/bin/python3 gh_sync.py pull "$(date -v-1d +%F)"   # yesterday (complete)
/opt/homebrew/bin/python3 gh_sync.py pull "$(date +%F)"        # today (overnight + partial)
git add tracker.csv
if git commit -m "auto: health sync" --quiet 2>/dev/null; then
  if git push --quiet 2>/dev/null; then
    echo "synced + pushed"
  else
    echo "committed locally (push blocked from agent — will sync next session)"
  fi
else
  echo "no new data to commit"
fi
