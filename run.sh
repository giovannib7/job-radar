#!/bin/bash
# Wrapper that launchd calls once a day. Runs the radar and logs the output.
# Using absolute paths because launchd starts with a bare environment.
DIR="/Users/giovanniborraccia/Desktop/PhD research/job_radar"
PYTHON="/Users/giovanniborraccia/anaconda3/bin/python3"
cd "$DIR" || exit 1
echo "===== $(date) =====" >> "$DIR/run.log"
"$PYTHON" "$DIR/job_radar.py" >> "$DIR/run.log" 2>&1
