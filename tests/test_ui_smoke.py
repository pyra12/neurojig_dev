from NeuroJig.ui.main_window import MainWindow


def test_main_window_smoke(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    assert window.isVisible()
    window.close()
