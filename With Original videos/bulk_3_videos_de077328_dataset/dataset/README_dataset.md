# Dataset export

- **schema_version**: 1.0.0
- **data.jsonl**: one JSON object per line — `video_source_id` (job id), `original_filename` (upload name), `keypoints` (primary person), optional `persons[]` with `person_id` + `keypoints` for multi-person frames, `person_count`, `timestamp_ms`, `action_label`, optional `layer11`. With **HQ export**, `original_frame_id` links to the pre-filter id; `source_video_fps` is the source clip frame rate.
- **low_quality_frames.jsonl** (HQ only): frames that failed the filter, with `reject_reasons` and `quality_metrics`.
- **export_quality_report.json**: thresholds and formula references for this job.
- **features.json**: sequence-level aggregates; **bulk** jobs use schema 1.3.x with `videos[]` + `aggregate`.
- **global_stats.json**: job roll-up; **bulk** adds `totals`, per-video rows under `videos`; **HQ** adds `quality_filter`.
- **manifest.json**: job metadata and augmentation tags.
- Verify integrity with `SHA256SUMS`.
