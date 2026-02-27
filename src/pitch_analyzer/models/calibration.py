"""Calibration and homography models."""

from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass
class CalibrationPoints:
    """Pixel-to-pitch point correspondences for homography."""

    pixel_points: np.ndarray  # Nx2 float32, (x, y) in image coords
    pitch_points: np.ndarray  # Nx2 float32, (x_m, y_m) in pitch coords

    def __post_init__(self) -> None:
        self.pixel_points = np.asarray(self.pixel_points, dtype=np.float32)
        self.pitch_points = np.asarray(self.pitch_points, dtype=np.float32)
        if self.pixel_points.shape != self.pitch_points.shape:
            raise ValueError("pixel_points and pitch_points must have same shape")
        if self.pixel_points.shape[0] < 4:
            raise ValueError("At least 4 point pairs required")

    @property
    def n_points(self) -> int:
        return len(self.pixel_points)


@dataclass
class HomographyMatrix:
    """3x3 homography matrix (pixel -> pitch)."""

    matrix: np.ndarray  # 3x3 float32

    def __post_init__(self) -> None:
        self.matrix = np.asarray(self.matrix, dtype=np.float32)
        if self.matrix.shape != (3, 3):
            raise ValueError("Homography must be 3x3")

    def to_list(self) -> list[list[float]]:
        """Serialize for JSON storage."""
        return self.matrix.tolist()

    @classmethod
    def from_list(cls, data: list[list[float]]) -> "HomographyMatrix":
        """Deserialize from JSON."""
        return cls(matrix=np.array(data, dtype=np.float32))

    def to_dict(self) -> dict[str, Any]:
        """Serialize for project.json."""
        return {"matrix": self.to_list()}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "HomographyMatrix":
        """Deserialize from project.json."""
        return cls.from_list(data["matrix"])
