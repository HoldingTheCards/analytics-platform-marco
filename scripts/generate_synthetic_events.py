import csv, argparse, random, uuid
from datetime import datetime, timedelta

EVENTS = ['page_view','click','add_to_cart','checkout','purchase']

def rand_ts(days=14):
    now = datetime.utcnow()
    dt = now - timedelta(seconds=random.randint(0, days*86400))
    return dt.isoformat()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='data/events.csv')
    ap.add_argument('--rows', type=int, default=5000)
    args = ap.parse_args()

    rows = []
    for _ in range(args.rows):
        uid = uuid.uuid4().hex[:12]
        sid = uuid.uuid4().hex[:12]
        evt = random.choice(EVENTS)
        consent = random.random() > 0.1
        rows.append({
            'event_id': uuid.uuid4().hex,
            'user_id': uid,
            'session_id': sid,
            'event_name': evt,
            'event_ts': rand_ts(),
            'consent': str(consent).lower()
        })

    import os
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {args.out}")

if __name__ == '__main__':
    main()
