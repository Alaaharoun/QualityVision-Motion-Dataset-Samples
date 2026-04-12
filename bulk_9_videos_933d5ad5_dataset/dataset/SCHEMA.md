# Dataset schema & examples

- **Job ID**: `bulk_9_videos_933d5ad5`
- **Action label**: `Dexterous Hand movements`
- **Videos processed**: 9
- **Exported frames (HQ, incl. augmentations)**: 9112
- **Frames accepted (pre-augmentation)**: 2278
- **Frames sampled (candidates)**: 3962
- **Rejected frames**: 1684
- **Acceptance rate (pre-aug / sampled)**: 57.5%
- **Mean quality score (accepted)**: 0.9715
- **Mean landmark visibility (accepted)**: 0.942951
- **Mean lower-body visibility (accepted)**: 0.0
- **Mean motion_local (accepted)**: 1.0
- **Mean FPS**: 34.98001998001998
- **Stride**: 1

## File layout

- `data.jsonl` — accepted frames (merged across sources).
- `low_quality_frames.jsonl` — rejected / no-pose frames (hard examples).
- `per_video/video_*.jsonl` — accepted frames split per source.
- `per_video/rejected_*.jsonl` — rejected frames split per source.
- `features.json` — sequence-level metrics (motion consistency, velocity/accel proxies, etc.).
- `global_stats.json` — global aggregates and per-video rows.
- `export_quality_report.json` — thresholds and quality-score formulas.
- `manifest.json` / `runtime_config.json` — export flags and runtime snapshot.
- `metadata/actions.csv` — `frame_id,action` (mirrors JSONL `action`).
- `metadata/hand_activity.csv` — dexterous: per-frame activity / grip / motion class (when exported).
- `metadata/dataset_meta.json` — optional `camera_pov` and schema notes.

## Per-frame record (JSONL) — accepted frames (`data.jsonl`)

Each line is a JSON object. Key fields (may include additional keys depending on engine version):

- `frame_id` (int): global monotonically increasing id in this export
- `timestamp_ms` (float): timestamp in milliseconds in the source clip
- `video_source_id` (string): job id
- `original_filename` (string): source filename
- `source_video_index` (int): index into `manifest.json` source list (may be omitted in some exports)
- `keypoints` (object): **33** body landmarks (pose) or **21** hand landmarks (MediaPipe Hands), each `x`, `y`, `z`, `visibility`
- `action` (string): per-frame action taxonomy (defaults to job `action_label`; optional `hq.per_frame_actions` overrides by global `frame_id`)
- `action_label` (string): job-level label (same for all frames unless overridden per row)
- `camera_pov` (string, optional): `first_person` | `third_person` | `unknown` when set via `hq.camera_pov` / `payload.camera_pov`
- `object_interaction` (object, optional): `object_type`, `interaction` — simple hand–object hint when `hq.object_interaction` is set (hands + dexterous refines `interaction` from grip heuristic)
- `layer11` (object): fallback vision features (RGB mean/std, brightness, contrast, edge density, hue histogram)
- `keypoints_body_normalized` (object, optional): hip-centered + torso-scale normalized keypoints (pose exports; omitted when hips/shoulders absent)
- `body_normalization` (object, optional): normalization metadata (`origin`, `scale`, etc.)
- `wrist_position` (object, optional): `x`, `y`, `z` of the wrist landmark (image-normalized; **hand exports**)
- `wrist_relative_keypoints` (object, optional): same keys as `keypoints`, coordinates **relative to wrist** (**hand exports**)

## Dexterous Hand Movements (`manifest.dexterous_hand_export`)

When this export flag is true, each accepted row may include a `dexterous_hand` object (hand pipeline / dexterous intent) and top-level `motion_intelligence` mapped from the hand block (version 3, `domain: hand_dexterous`).

### `dexterous_hand` fields

- `schema_version` (string)
- `finger_angles_deg` (object): 2D image-plane flexion/spread proxies (e.g. `thumb_flex_mcp`, per-finger `*_flex_pip` / `*_flex_dip`, `thumb_index_spread_at_wrist_deg`)
- `grip_type_proxy` (string): `pinch` | `precision` | `power` | `open` | `neutral` | `unknown` (heuristic, no object mesh)
- `finger_tip_velocity_norm_per_sec` (object): per-tip speeds in normalized coords/sec (`thumb_tip_speed`, …)
- `finger_tip_speed_mean` (float): mean of tip speeds for the frame
- `hand_visibility_mean` (float): mean landmark visibility (0–1)
- `dexterous_quality_proxy` (float): hand-only quality score (visibility + motion + angle spread)
- `motion_intelligence` (object): `version` 3, `domain` `hand_dexterous`, `wrist_speed_norm_per_sec`, `finger_tip_speed_mean`, `finger_tip_energy`, `grip_type_proxy`, `grip_changed_from_prev_frame`, `hand_activity_class` (`static` | `finger_active` | `hand_translating` | `manipulation`)
- `notes` (string)

### Top-level `motion_intelligence` (dexterous rows)

Mirrors buyer-facing summaries: `speed_combined` (finger-tip mean), `motion_class_rule` (`hand_activity_class`), `wrist_speed_norm_per_sec`, `finger_tip_energy`, grip fields, `notes`.

### `global_stats.json` → `motion_intelligence` (dexterous)

- `domain`: `hand_dexterous`, `hand_activity_histogram`, `grip_type_histogram`, `mean_finger_tip_speed_mean`, `mean_wrist_speed_norm_per_sec`

## Rejected record (JSONL) — rejected frames (`low_quality_frames.jsonl`)

- `reject_reasons` (list[str]): e.g. `no_pose_detected`, `frame_quality_score`
- `quality_metrics` (object): per-frame computed metrics used by the filter
- Rejected frames still include `layer11` (when available).

## Sequence metrics (`features.json`)

Per video, under `videos[].sequence`:

- `motion_consistency` (float)
- `velocity_proxy_available` (bool)
- `velocity_mean` / `velocity_std` (float)
- `acceleration_mean` (float)
- `avg_stride_length` (float, proxy)
- `step_frequency` (float, Hz proxy)

## Quality score definition

- Per frame: frame_quality_score = 0.5 * avg_landmark_visibility + 0.0 * lower_body_visibility + 0.5 * motion_local.

## Examples

See `examples/` for small sample exports you can copy/paste into your pipeline.

## One-page PDF

If the optional Python dependency `reportlab` is available, the engine also writes:
- `Dataset_OnePager.pdf` — a one-page marketing + technical summary for sharing (e.g. Gumroad).
