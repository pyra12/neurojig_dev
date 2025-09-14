from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ProjectPanel(QWidget):
    """Placeholder panel for project overview and management."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Project"))
