---
license: cc-by-nc-4.0
language:
- en
tags:
- pose-estimation
- walking
- 2d-pose
- mediapipe
- motion-dataset
- quality-vision
pretty_name: QualityVision Bulk Walking (24 sources, 2D pose)
size_categories:
- 1K<n<10K
---

# QualityVision Bulk Walking Sample (24 videos)

**High-quality 2D pose** export from the [Quality Vision Motion Dataset Engine](https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples): **HQ filtering**, **Gaussian smoothing** on accepted frames, optional **horizontal flip** and **keypoint noise** augmentations in the merged `data.jsonl`.

## Numbers (this revision)

| Metric | Value |
|--------|--------|
| HQ-accepted frames (pre-augmentation) | **967** (see `run_diagnostics.json` → sum of `per_video[].frames_accepted`) |
| Rows in merged `data.jsonl` | **2901** (includes augmentations) |
| Mean quality score (accepted) | **~0.82** |
| Source clips | **24** |

## Files

Same layout as the GitHub folder [`bulk_24_videos_6a173caf_dataset/dataset/`](https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples/tree/main/bulk_24_videos_6a173caf_dataset/dataset):

| Path | Description |
|------|-------------|
| `data.jsonl` | Merged HQ rows (one JSON object per line). |
| `per_video/` | Per-source `video_*.jsonl` and `rejected_*.jsonl`. |
| `features.json`, `global_stats.json` | Sequence / batch aggregates. |
| `manifest.json`, `bulk_combined_manifest.json` | Export metadata. |
| `run_diagnostics.json`, `runtime_config.json` | Engine diagnostics (stride, caps, per-video counts). |
| `export_quality_report.json` | HQ threshold summary. |

## Usage

```python
from datasets import load_dataset

ds = load_dataset(
    "Alaaharoun/QualityVision-bulk-24v-walking",
    data_files="data.jsonl",
    split="train",
)
```

Replace `repo_id` with the dataset you created on the Hub if it differs.

## License

**CC BY-NC 4.0** — see [`LICENSE` on GitHub](https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples). Commercial use outside NC terms requires a separate agreement.

## Citation

```bibtex
@misc{qualityvision_bulk_24_walking,
  title = {QualityVision Bulk Walking Sample (2D Pose, 24 sources)},
  author = {Alaaharoun},
  howpublished = {\url{https://huggingface.co/datasets/Alaaharoun/QualityVision-bulk-24v-walking}},
  year = {2026},
}
```

(Adjust the URL if your Hub dataset name differs.)
