# Quality Vision — Hand Motion Dataset

**Train your AI on real hand motion data — ready in minutes.**

> Unlike many academic datasets, Quality Vision B2B exports are intended for commercial use under your agreed license terms — see LICENSE_EXPORT.txt in the ZIP and manifest.license / dataset_license (not limited to research-only).

## 1. Features
- 21-point hand keypoints (MediaPipe-style)
- Temporal sequences with timestamps
- Per-frame action field + metadata/actions.csv (optional per-frame taxonomy via job payload)
- Hand–object interaction metadata when hq.object_interaction is configured
- Optional camera_pov: first_person | third_person (manual)
- JSONL + optional COCO-like keypoints export
- PyTorch loader guide: examples/README_PYTORCH.md

## 2. Use cases
- 🤖 Robotics
- 🥽 AR/VR
- ✋ Gesture recognition
- 🧠 Human behavior AI

## 3. What's inside (dataset/)
```
dataset/
├── data.jsonl
├── metadata/
│   ├── actions.csv
│   └── dataset_meta.json
├── per_video/
├── features.json
├── global_stats.json   # includes buyer_marketing for hand jobs
└── examples/
    └── README_PYTORCH.md
```

## Dataset snapshot (metrics)
- Job ID: `bulk_9_videos_933d5ad5`
- Action label: `Dexterous Hand movements`
- Videos processed: 9
- Exported frames (HQ, incl. augmentations): 9112
- Accepted frames (pre-augmentation): 2278
- Sampled candidate frames: 3962
- Rejected frames: 1684
- Acceptance rate (pre-aug / sampled): 57.5%

## Quality Metrics (Accepted Frames)
- Mean quality score: 0.9715
- Mean landmark visibility: 0.9430
- Mean lower-body visibility: 0.0000
- Mean motion_local: 1.0000

## Processing
- Gaussian temporal smoothing: window=5 (x/y/z only; visibility not smoothed)
- Keypoints: MediaPipe Hands (21 landmarks per frame when detected)
- Dexterous block: `finger_angles_deg`, `grip_type_proxy`, tip velocities, `hand_visibility_mean`, `dexterous_quality_proxy`, hand `motion_intelligence` (v3)
- Augmentations: horizontal flip + keypoint noise
- Motion intelligence: hand-centric (v3) — wrist speed, finger-tip motion, grip heuristic, activity class

## Hand motion intelligence (dexterous)
- Mean finger-tip speed: 0.6318
- Mean wrist speed (norm/sec): 0.4500
- Frames with hand MI: 2278
- Hand activity histogram: {"finger_active": 2240, "hand_translating": 1, "manipulation": 24, "static": 13}
- Grip type histogram: {"neutral": 3, "open": 1444, "pinch": 227, "power": 33, "precision": 571}

## Deliverables (inside this ZIP)
- data.jsonl
- per_video/video_*.jsonl
- per_video/rejected_*.jsonl
- features.json
- export_quality_report.json
- manifest.json
- global_stats.json
- runtime_config.json
- SCHEMA.md
- examples/
- examples/sample_rows_accepted.jsonl
- examples/sample_rows_rejected.jsonl
- examples/sample_features.json
- examples/LOAD_EXAMPLE.py
- examples/README_PYTORCH.md
- metadata/actions.csv
- metadata/dataset_meta.json
- SHA256SUMS

## Quality Score Definition
- Per frame: frame_quality_score = 0.5 * avg_landmark_visibility + 0.0 * lower_body_visibility + 0.5 * motion_local.

https://qvision.space/
