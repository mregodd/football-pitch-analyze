"""Track record and parquet schema models."""

from dataclasses import dataclass
from typing import Optional

# tracks.parquet schema columns (PROJECT_PLAN.md)
TRACK_SCHEMA_COLUMNS = [
    "timestamp",
    "track_id",
    "team_id",
    "x_m",
    "y_m",
    "confidence",
]


@dataclass
class TrackRecord:
    """Single track observation (one row in tracks.parquet)."""

    timestamp: float  # Seconds from clip start
    track_id: int
    team_id: Optional[int]  # Phase 1: always None
    x_m: float
    y_m: float
    confidence: float

    def to_row(self) -> dict:
        """Convert to parquet row (team_id as None for Phase 1)."""
        return {
            "timestamp": self.timestamp,
            "track_id": self.track_id,
            "team_id": self.team_id,
            "x_m": self.x_m,
            "y_m": self.y_m,
            "confidence": self.confidence,
        }
