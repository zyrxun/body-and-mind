#!/usr/bin/env python3
"""Tiny local server for the Body & Mind logging UI.

Serves index.html and queues entries to inbox.jsonl, which Claude processes later
in a normal Claude Code session. NO external APIs, NO API credits — pure local capture.
Binds to 127.0.0.1 ONLY (Richard is on shared wifi — never 0.0.0.0).

Run:  python3 server.py      then open the http://127.0.0.1:<port> it prints (8642+)
"""
import csv, json, os, socketserver, http.server
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(HERE, "inbox.jsonl")
TRACKER = os.path.join(os.path.dirname(HERE), "tracker.csv")
PORT = 8642  # base port; auto-increments if busy


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=HERE, **k)

    def log_message(self, *a):  # quiet
        pass

    def do_POST(self):
        if self.path != "/log":
            self.send_error(404); return
        length = int(self.headers.get("Content-Length", 0))
        try:
            entry = json.loads(self.rfile.read(length).decode())
        except Exception:
            self.send_error(400, "bad json"); return
        entry["ts"] = datetime.now().isoformat(timespec="seconds")
        with open(INBOX, "a") as f:
            f.write(json.dumps(entry) + "\n")
        self._json({"ok": True, "pending": self._pending()})

    def do_GET(self):
        if self.path == "/today":
            self._json(self._today())
        else:
            super().do_GET()

    def _json(self, obj):
        data = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _pending(self):
        if not os.path.exists(INBOX):
            return 0
        with open(INBOX) as f:
            return sum(1 for ln in f if ln.strip())

    def _today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        row = {}
        try:
            with open(TRACKER) as f:
                for r in csv.DictReader(f):
                    if r.get("Date") == today:
                        row = r
        except Exception:
            pass
        return {"date": today, "row": row, "pending": self._pending()}


if __name__ == "__main__":
    os.chdir(HERE)
    httpd = None
    for port in range(PORT, PORT + 10):
        try:
            httpd = socketserver.TCPServer(("127.0.0.1", port), Handler)
            break
        except OSError:
            continue  # port busy — try the next one
    if httpd is None:
        raise SystemExit(f"No free port in {PORT}-{PORT + 9}. Close other servers and retry.")
    print(f"Body & Mind UI  →  http://127.0.0.1:{port}   (Ctrl-C to stop)")
    httpd.serve_forever()
