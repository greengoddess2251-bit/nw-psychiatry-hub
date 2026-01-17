"""Settings view for Northwest Psychiatry Hub."""

from __future__ import annotations

from typing import Any

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from northwest_psych_hub.services.config_service import ConfigService


class SettingsView(QWidget):
    """Display and edit user preferences."""

    logout_requested = pyqtSignal()

    def __init__(self, username: str, config_service: ConfigService) -> None:
        super().__init__()
        self._config_service = config_service
        self._build_ui(username)
        self._load_preferences()

    def _build_ui(self, username: str) -> None:
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(16)

        header = QLabel("Settings")
        header.setStyleSheet("font-size: 18px; font-weight: 600;")
        layout.addWidget(header)

        username_label = QLabel(f"Signed in as {username}")
        username_label.setStyleSheet("color: #555555;")
        layout.addWidget(username_label)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)

        self.theme_select = QComboBox()
        self.theme_select.addItems(["System", "Light", "Dark"])
        form_layout.addRow("Theme", self.theme_select)

        self.compact_layout = QCheckBox("Use compact spacing")
        form_layout.addRow("Layout", self.compact_layout)

        self.show_reminders = QCheckBox("Show appointment reminders")
        form_layout.addRow("Notifications", self.show_reminders)

        layout.addLayout(form_layout)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: #0a6e31;")
        self.status_label.setVisible(False)
        layout.addWidget(self.status_label)

        action_row = QHBoxLayout()
        action_row.addStretch()

        self.logout_button = QPushButton("Log out")
        self.logout_button.clicked.connect(self.logout_requested.emit)
        action_row.addWidget(self.logout_button)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self._handle_save_clicked)
        action_row.addWidget(self.save_button)

        layout.addLayout(action_row)
        self.setLayout(layout)

    def _load_preferences(self) -> None:
        preferences = self._config_service.load_preferences()
        self._apply_preferences(preferences)

    def _apply_preferences(self, preferences: dict[str, Any]) -> None:
        theme = preferences.get("theme", "System")
        theme_index = self.theme_select.findText(theme)
        if theme_index == -1:
            theme_index = 0
        self.theme_select.setCurrentIndex(theme_index)

        self.compact_layout.setChecked(bool(preferences.get("compact_layout", False)))
        self.show_reminders.setChecked(bool(preferences.get("show_reminders", True)))

    def _handle_save_clicked(self) -> None:
        preferences = {
            "theme": self.theme_select.currentText(),
            "compact_layout": self.compact_layout.isChecked(),
            "show_reminders": self.show_reminders.isChecked(),
        }
        self._config_service.save_preferences(preferences)
        self.status_label.setText("Preferences saved.")
        self.status_label.setVisible(True)
