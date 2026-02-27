"""Pitch constants, FPS, and path configuration."""

from pathlib import Path

# Pitch dimensions (FIFA standard)
PITCH_LENGTH_M = 105.0
PITCH_WIDTH_M = 68.0

# Origin: bottom-left corner
# x: 0 → 105 (left to right)
# y: 0 → 68 (bottom to top)

# Frame sampling
DEFAULT_FPS = 8  # 5–10 FPS range
MIN_FPS = 5
MAX_FPS = 10

# Detection
DEFAULT_CONFIDENCE_THRESHOLD = 0.5
COCO_PERSON_CLASS_ID = 0

# Paths
def get_projects_dir() -> Path:
    """User projects directory (Projects/ in repo root)."""
    return Path(__file__).resolve().parent.parent.parent / "Projects"


def get_data_dir() -> Path:
    """Sample/data directory."""
    return Path(__file__).resolve().parent.parent.parent / "data"
