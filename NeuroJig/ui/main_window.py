from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDockWidget, QMainWindow, QStatusBar

from .canvas import LayoutCanvas
from .panels.assets_panel import AssetsPanel
from .panels.circuits_panel import CircuitsPanel
from .panels.properties_panel import PropertiesPanel
from .panels.project_panel import ProjectPanel


class MainWindow(QMainWindow):
    """Main application window with menus, docks and central canvas."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("NeuroJig")
        self.canvas = LayoutCanvas(self)
        self.setCentralWidget(self.canvas)
        self._create_menus()
        self._create_docks()
        self.setStatusBar(QStatusBar(self))

    # ------------------------------------------------------------------
    def _create_menus(self) -> None:
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction(QAction("New", self))
        file_menu.addAction(QAction("Open", self))
        file_menu.addAction(QAction("Save JSON", self))
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        # Tools menu
        tools_menu = menubar.addMenu("Tools")
        select_action = QAction("Select", self)
        tools_menu.addAction(select_action)

        add_node_action = QAction("Add Node", self)
        add_node_action.setShortcut("N")
        tools_menu.addAction(add_node_action)

        tools_menu.addAction(QAction("Add Edge", self))
        tools_menu.addAction(QAction("Add Angle", self))
        tools_menu.addAction(QAction("Add Connector", self))
        tools_menu.addAction(QAction("Add Clip", self))
        tools_menu.addAction(QAction("Add Splice", self))
        tools_menu.addAction(QAction("Add Grommet", self))

        # View menu
        view_menu = menubar.addMenu("View")
        view_menu.addAction(QAction("Layout", self))
        view_menu.addAction(QAction("Circuits", self))

    # ------------------------------------------------------------------
    def _create_docks(self) -> None:
        docks = [
            ("Properties", PropertiesPanel()),
            ("Assets", AssetsPanel()),
            ("Circuits", CircuitsPanel()),
            ("Project", ProjectPanel()),
        ]
        for title, widget in docks:
            dock = QDockWidget(title, self)
            dock.setWidget(widget)
            self.addDockWidget(Qt.RightDockWidgetArea, dock)
