"""Main application window for Northwest Psychiatry Hub."""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Primary application window with navigation and content pages."""

    def __init__(self, username: str) -> None:
        super().__init__()
        self.setWindowTitle("Northwest Psychiatry Hub")
        self._pages = {}
        self._build_ui(username)

    def _build_ui(self, username: str) -> None:
        container = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.navigation = QListWidget()
        self.navigation.setFixedWidth(200)
        self.navigation.setSpacing(4)
        self.navigation.setStyleSheet("QListWidget { padding: 8px; }")
        self.navigation.currentRowChanged.connect(self._handle_navigation_changed)

        self.stack = QStackedWidget()

        for page_name in [
            "Dashboard",
            "Patients",
            "Billing",
            "Claims",
            "Email Hub",
            "Settings",
        ]:
            self._add_page(page_name, username)

        layout.addWidget(self.navigation)
        layout.addWidget(self.stack)
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.navigation.setCurrentRow(0)

    def _add_page(self, name: str, username: str) -> None:
        page = QWidget()
        page_layout = QVBoxLayout()
        page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        heading = QLabel(f"{name}")
        heading.setStyleSheet("font-size: 18px; font-weight: 600;")

        subtitle = QLabel(f"Welcome {username}. {name} content goes here.")
        subtitle.setWordWrap(True)
        subtitle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        page_layout.addWidget(heading)
        page_layout.addWidget(subtitle)
        page.setLayout(page_layout)

        item = QListWidgetItem(name)
        self.navigation.addItem(item)

        self.stack.addWidget(page)
        self._pages[name] = page

    def _handle_navigation_changed(self, index: int) -> None:
        if index < 0:
            return
        self.stack.setCurrentIndex(index)
