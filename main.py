import sys

from PySide6.QtWidgets import QApplication
from authorization_window import AuthorizationWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    # window = MainWindow()
    authorization_window = AuthorizationWindow()
    authorization_window.show()
    # window.show()

    sys.exit(app.exec())