from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PropertiesPanel(QWidget):
    """Placeholder panel for displaying selected object properties."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Properties"))
