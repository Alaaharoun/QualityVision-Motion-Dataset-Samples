import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_jsonl(path: Path, limit: int = 5):
    rows = []
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
            if len(rows) >= limit:
                break
    return rows

if __name__ == '__main__':
    accepted = ROOT / 'examples' / 'sample_rows_accepted.jsonl'
    rejected = ROOT / 'examples' / 'sample_rows_rejected.jsonl'
    if accepted.is_file():
        a = read_jsonl(accepted, limit=2)
        print('accepted sample:', a[0].keys())
    if rejected.is_file():
        r = read_jsonl(rejected, limit=2)
        print('rejected sample:', r[0].keys())
