"""Project metadata and state models."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from pitch_analyzer.models.calibration import HomographyMatrix


@dataclass
class ProjectMetadata:
    """Immutable project metadata."""

    name: str
    path: Path
    created_at: str = ""  # ISO timestamp
    updated_at: str = ""


@dataclass
class ProjectState:
    """Full project state (saveable/loadable)."""

    metadata: ProjectMetadata
    clip_paths: list[Path] = field(default_factory=list)
    calibration: Optional[HomographyMatrix] = None
    reference_frame_index: int = 0  # Which frame was used for calibration

    def add_clip(self, path: Path) -> None:
        """Add a clip path if not already present."""
        if path not in self.clip_paths:
            self.clip_paths.append(path)

    def remove_clip(self, path: Path) -> None:
        """Remove a clip path."""
        if path in self.clip_paths:
            self.clip_paths.remove(path)
