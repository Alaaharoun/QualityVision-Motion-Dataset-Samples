## Use cases

**Export action label:** `Dexterous Hand movements`

This dataset contains **per-frame hand keypoints** (MediaPipe Hands-style names when applicable) and, when enabled, **`dexterous_hand`** / **`motion_intelligence`** fields. See `SCHEMA.md` for the exact record shape. Typical applications:

### 1. Robotics manipulation & teleoperation

Train policies and estimators for **reach-to-grasp**, **in-hand adjustment**, **tool use**, and **imitation learning** from human demonstrations. Wrist trajectories and hand activity classes support **retargeting** to robot end-effectors; grip proxies help classify **pinch vs power** style grasps.

### 2. Gesture recognition & human-computer interaction

Build **command gestures**, **static vs dynamic hand pose** classifiers, and **multimodal** interfaces (vision + speech). Useful for **accessibility** (alternative input) and smart displays.

### 3. AR / VR & spatial computing

Drive **hand-tracked UIs**, **avatar upper-body animation**, and **social presence** in VR. Normalized keypoints integrate with Unity, Unreal, WebXR via your retargeting layer.

### 4. Fine motor control & rehabilitation

Track **movement smoothness**, **range of motion proxies**, and **session-level trends** from `features.json` and per-frame quality scores.

### 5. Animation & digital humans

**Retarget** performer hand motion to rigs; combine with artist rigs or additional mocap for film-quality fingers.

### 6. Industrial ergonomics & safety

Analyze **repetitive hand/wrist paths** and **reach envelopes** for workstation design.

### 7. Research & benchmarking

Use the export as a **standardized JSONL stream** for comparing filters and models on **hand-centric** labels.

---

**Note:** This document targets **dexterous / hand** exports. Full-body **walking / gait** use cases are not the focus here; see other Quality Vision walking samples if you need locomotion data.

