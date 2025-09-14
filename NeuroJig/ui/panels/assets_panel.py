from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class AssetsPanel(QWidget):
    """Placeholder panel for asset library management."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Assets"))
