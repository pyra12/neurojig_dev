from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class CircuitsPanel(QWidget):
    """Placeholder panel for circuit listing and editing."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Circuits"))
