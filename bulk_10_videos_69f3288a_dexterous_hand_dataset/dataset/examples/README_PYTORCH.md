# PyTorch loader (optional)

Install: `pip install torch`

Use from the **dataset** directory (same folder as `data.jsonl`) or pass an explicit path.

```python
import json
from pathlib import Path

from torch.utils.data import Dataset


class HandDataset(Dataset):
    def __init__(self, dataset_dir, *, jsonl_name='data.jsonl', jsonl_path=None):
        self.root = Path(dataset_dir)
        self.path = jsonl_path or self.root / jsonl_name
        self.rows = []
        with open(self.path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    self.rows.append(json.loads(line))

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        return self.rows[i]
```

Reference: `hand_dataset.py` in the Quality Vision `motion_dataset_engine` repository.
