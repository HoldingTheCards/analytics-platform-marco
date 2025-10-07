
#!/usr/bin/env python3
import csv, os, subprocess, sys

CSV_FILE = os.environ.get("CSV_FILE", "/mnt/data/GitHub_Issues_Import_Roadmap.csv")
REPO = os.environ.get("REPO")
DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"

if not REPO:
    print("Please export REPO=<owner>/<repo>"); sys.exit(1)

def run(cmd):
    if DRY_RUN:
        print("[DRY-RUN]", " ".join(cmd)); return 0
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("Command failed:", " ".join(cmd))
        print(res.stderr)
    else:
        print(res.stdout.strip())
    return res.returncode

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, 1):
        title = row.get("Title", "").strip()
        body  = row.get("Body", "").strip()
        labels_str = row.get("Labels", "").strip()
        milestone = row.get("Milestone", "").strip()
        cmd = ["gh", "issue", "create", "--repo", REPO, "--title", title, "--body", body]
        labels = [l.strip() for l in labels_str.split(";") if l.strip()]
        for lab in labels:
            cmd.extend(["--label", lab])
        if milestone:
            cmd.extend(["--milestone", milestone])
        print("Creating issue #{}: {}".format(i, title))
        rc = run(cmd)
        if rc != 0:
            print("Retry with DRY_RUN=1 to debug.")
