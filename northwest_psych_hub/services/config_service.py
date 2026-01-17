"""Configuration service for application preferences."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_PREFERENCES: dict[str, Any] = {
    "theme": "System",
    "compact_layout": False,
    "show_reminders": True,
}


class ConfigService:
    """Load and save non-sensitive application preferences."""

    def __init__(self, config_path: Path | None = None) -> None:
        if config_path is None:
            base_path = Path(__file__).resolve().parents[1]
            config_path = base_path / "config" / "app_config.json"
        self._config_path = config_path

    def load_preferences(self) -> dict[str, Any]:
        """Return saved preferences or defaults when unavailable."""
        if not self._config_path.exists():
            return DEFAULT_PREFERENCES.copy()

        try:
            with self._config_path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (json.JSONDecodeError, OSError):
            return DEFAULT_PREFERENCES.copy()

        if not isinstance(data, dict):
            return DEFAULT_PREFERENCES.copy()

        merged = DEFAULT_PREFERENCES.copy()
        merged.update({key: value for key, value in data.items()})
        return merged

    def save_preferences(self, preferences: dict[str, Any]) -> None:
        """Persist preferences to the JSON configuration file."""
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        with self._config_path.open("w", encoding="utf-8") as handle:
            json.dump(preferences, handle, indent=2, sort_keys=True)
            handle.write("\n")
