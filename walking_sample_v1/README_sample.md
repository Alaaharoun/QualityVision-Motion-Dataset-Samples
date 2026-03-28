# `walking_sample_v1`

| File | Description |
|------|-------------|
| `data.jsonl` | 80 consecutive frames, one JSON object per line (primary person `keypoints`, optional `layer11`, `source_video_fps`, etc.). |
| `features.json` | Sequence-level aggregates (visibility, hip motion, `motion_consistency`, stride proxies). |
| `global_stats.json` | Job-level roll-up for this clip. |
| `manifest.json` | Metadata aligned with the Motion Dataset Engine export format. |
| `export_quality_report.json` | Pilot-oriented summary + pointers to formulas. |

**Coordinate system:** normalized image coordinates (typically ~0–1 for x/y), z relative depth as exported by the engine.

**Not included:** raw video, full ZIP checksums, or rejected frames — this repo is intentionally small for GitHub hosting and feedback collection.

To regenerate a pose preview image, run from the repository root:

```bash
python scripts/render_pose_preview.py
```
