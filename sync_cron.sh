#!/bin/bash
# Daily health sync for the Body & Mind tracker — run by cron.
# Pulls Steps / Sleep_hrs / Resting_HR from Google Health into tracker.csv,
# commits, and best-effort pushes. Safe to run repeatedly (idempotent).
DIR="/Users/richard/claude-workspace/body and mind"
cd "$DIR" || exit 1
echo "===== $(date) ====="
git pull --rebase --quiet 2>/dev/null
ARG="$1"; [ "$ARG" = "today" ] && ARG=$(date +%F)   # no arg → yesterday; "today" → today's date
/opt/homebrew/bin/python3 gh_sync.py pull $ARG
git add tracker.csv
if git commit -m "cron: daily health sync" --quiet 2>/dev/null; then
  if git push --quiet 2>/dev/null; then
    echo "synced + pushed"
  else
    echo "committed locally (push blocked from cron — will sync next session)"
  fi
else
  echo "no new data to commit"
fi
