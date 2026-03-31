# Motion dataset export

- Job: `bulk_2_videos_28fb9459`
- Videos processed: 2
- Exported frames (HQ): 348

## Layout

- `data.jsonl` — all accepted frames from all videos (global `frame_id`).
- Optional additive fields: `keypoints_body_normalized`, `body_normalization`; optional Gaussian on `keypoints` x/y/z when enabled (see manifest `keypoint_post_processing`).
- `per_video/video_NNN.jsonl` — same schema, only frames from source index NNN.
- `per_video/rejected_NNN.jsonl` — low-quality / no-pose for that source.
- `low_quality_frames.jsonl` — all rejected rows across sources.
- `bulk_combined_manifest.json` — index of combined vs per-video files.
