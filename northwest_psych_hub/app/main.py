"""Application entry point for Northwest Psychiatry Hub."""

import sys

from PyQt6.QtWidgets import QApplication

from northwest_psych_hub.ui.login_view import LoginView
from northwest_psych_hub.ui.main_window import MainWindow


class WindowManager:
    """Handle switching between the login and main application windows."""

    def __init__(self) -> None:
        self.login_view = LoginView()
        self.login_view.login_requested.connect(self.show_main_window)
        self.main_window: MainWindow | None = None

    def show_login(self) -> None:
        if self.main_window is not None:
            self.main_window.close()
            self.main_window = None
        self.login_view.reset_form()
        self.login_view.show()

    def show_main_window(self, username: str) -> None:
        if self.main_window is None:
            self.main_window = MainWindow(username, self.show_login)
        self.main_window.show()
        self.login_view.hide()


def main() -> None:
    """Run the Northwest Psychiatry Hub application."""
    app = QApplication(sys.argv)
    manager = WindowManager()
    manager.show_login()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
