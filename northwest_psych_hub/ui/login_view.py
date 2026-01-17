"""Login view for Northwest Psychiatry Hub."""

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class LoginView(QWidget):
    """Login form for the application."""

    login_requested = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Northwest Psychiatry Hub - Login")
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setSpacing(12)

        header = QLabel("Sign in")
        header.setStyleSheet("font-size: 20px; font-weight: 600;")
        layout.addWidget(header)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: #b00020;")
        self.error_label.setVisible(False)
        layout.addWidget(self.error_label)

        button_row = QHBoxLayout()
        button_row.addStretch()
        self.login_button = QPushButton("Log In")
        self.login_button.clicked.connect(self._handle_login_clicked)
        button_row.addWidget(self.login_button)
        layout.addLayout(button_row)

        layout.addStretch()
        self.setLayout(layout)

    def _handle_login_clicked(self) -> None:
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            self.error_label.setText("Please enter both a username and password.")
            self.error_label.setVisible(True)
            return

        self.error_label.setVisible(False)
        self.login_requested.emit(username)
