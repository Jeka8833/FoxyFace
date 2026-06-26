import sys

from PySide6.QtWidgets import QApplication

from src.ui.windows.GraphPreviewWindow import GraphPreviewWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphPreviewWindow()
    window.set_graph(None, None)
    window.show()
    sys.exit(app.exec())