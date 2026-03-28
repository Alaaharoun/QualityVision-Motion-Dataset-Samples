#!/usr/bin/env python3
"""
Render a 3-panel pose skeleton preview from walking_sample_v1/data.jsonl.
Requires: matplotlib, numpy (stdlib json only otherwise).

Usage (from repo root):
  python scripts/render_pose_preview.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "walking_sample_v1" / "data.jsonl"
OUT = REPO / "images" / "walking_pose_preview.png"

# Minimal skeleton (MediaPipe pose landmark names)
EDGES: list[tuple[str, str]] = [
    ("nose", "left_shoulder"),
    ("nose", "right_shoulder"),
    ("left_shoulder", "right_shoulder"),
    ("left_shoulder", "left_elbow"),
    ("left_elbow", "left_wrist"),
    ("right_shoulder", "right_elbow"),
    ("right_elbow", "right_wrist"),
    ("left_shoulder", "left_hip"),
    ("right_shoulder", "right_hip"),
    ("left_hip", "right_hip"),
    ("left_hip", "left_knee"),
    ("left_knee", "left_ankle"),
    ("right_hip", "right_knee"),
    ("right_knee", "right_ankle"),
]


def load_frames(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def draw_skeleton(ax, kp: dict, title: str) -> None:
    ax.set_title(title, fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlim(0, 1)
    ax.set_ylim(1, 0)
    ax.set_xlabel("x (norm)")
    ax.set_ylabel("y (norm)")
    for a, b in EDGES:
        pa = kp.get(a)
        pb = kp.get(b)
        if not isinstance(pa, dict) or not isinstance(pb, dict):
            continue
        try:
            xa, ya = float(pa["x"]), float(pa["y"])
            xb, yb = float(pb["x"]), float(pb["y"])
        except (KeyError, TypeError, ValueError):
            continue
        ax.plot([xa, xb], [ya, yb], color="#c9a227", linewidth=2, alpha=0.9)
    for name, pt in kp.items():
        if not isinstance(pt, dict):
            continue
        try:
            x, y = float(pt["x"]), float(pt["y"])
        except (KeyError, TypeError, ValueError):
            continue
        vis = float(pt.get("visibility", 1.0))
        c = "#4ade80" if vis > 0.65 else "#f87171"
        ax.scatter([x], [y], s=12, c=c, edgecolors="black", linewidths=0.3, zorder=3)


def main() -> int:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Install matplotlib: pip install matplotlib", file=sys.stderr)
        return 1

    if not DATA.exists():
        print(f"Missing {DATA}", file=sys.stderr)
        return 1

    frames = load_frames(DATA)
    if len(frames) < 3:
        print("Not enough frames", file=sys.stderr)
        return 1

    indices = [0, len(frames) // 2, len(frames) - 1]
    titles = [f"frame_id={frames[i]['frame_id']}" for i in indices]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.0))
    fig.suptitle("QualityVision walking sample — 2D pose (normalized)", fontsize=11)
    for ax, idx, tt in zip(axes, indices, titles):
        kp = frames[idx].get("keypoints") or {}
        if not isinstance(kp, dict):
            kp = {}
        draw_skeleton(ax, kp, tt)

    plt.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
