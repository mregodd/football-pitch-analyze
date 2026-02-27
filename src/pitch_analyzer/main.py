"""PySide6 entry point for the desktop application."""

import sys

from PySide6.QtWidgets import QApplication

# TODO: Import MainWindow when UI is implemented
# from pitch_analyzer.ui.main_window import MainWindow


def main() -> int:
    """Launch the pitch analyzer application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Pitch Analyzer")
    # win = MainWindow()
    # win.show()
    # return app.exec()
    # Placeholder: exit immediately until UI is built
    print("Pitch Analyzer – UI coming soon")
    return 0


if __name__ == "__main__":
    sys.exit(main())
