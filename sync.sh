#!/bin/bash
# Health sync (Linux port of the old macOS launchd script) — systemd --user timer
# runs this at 08:00 and 23:55. Pulls YESTERDAY (complete day incl. its sleep) and
# TODAY (overnight sleep + steps) from Google Health into tracker.csv, then commits
# + pushes. Pure script — no Claude, no API credits. Idempotent, safe to re-run.
DIR="/home/zyxun/projects/body-and-mind"
cd "$DIR" || exit 1
echo "===== $(date) ====="
git pull --rebase --quiet 2>/dev/null
python3 gh_sync.py pull "$(date -d yesterday +%F)" || echo "pull(yesterday) failed — auth tokens missing/expired? run: python3 gh_sync.py authurl"
python3 gh_sync.py pull "$(date +%F)"        || echo "pull(today) failed — see above"
git add tracker.csv
if git commit -m "auto: health sync" --quiet 2>/dev/null; then
  if git push --quiet 2>/dev/null; then
    echo "synced + pushed"
  else
    echo "committed locally (push failed — will sync next run)"
  fi
else
  echo "no new data to commit"
fi
