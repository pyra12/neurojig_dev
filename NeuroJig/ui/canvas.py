from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor, QPen, QWheelEvent, QMouseEvent
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene


class LayoutCanvas(QGraphicsView):
    """Simple QGraphicsView with pan/zoom and grid background."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self._panning = False
        self._pan_start = QPoint()

    def wheelEvent(self, event: QWheelEvent) -> None:  # pragma: no cover - Qt
        factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(factor, factor)

    def mousePressEvent(self, event: QMouseEvent) -> None:  # pragma: no cover - Qt
        if event.button() == Qt.RightButton:
            self._panning = True
            self._pan_start = event.pos()
            self.setCursor(Qt.ClosedHandCursor)
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:  # pragma: no cover - Qt
        if self._panning:
            delta = event.pos() - self._pan_start
            self._pan_start = event.pos()
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:  # pragma: no cover - Qt
        if event.button() == Qt.RightButton and self._panning:
            self._panning = False
            self.setCursor(Qt.ArrowCursor)
        else:
            super().mouseReleaseEvent(event)

    def drawBackground(self, painter: QPainter, rect) -> None:  # pragma: no cover - Qt
        super().drawBackground(painter, rect)
        painter.save()
        grid = 50
        left = int(rect.left()) - (int(rect.left()) % grid)
        top = int(rect.top()) - (int(rect.top()) % grid)
        pen = QPen(QColor(200, 200, 200))
        painter.setPen(pen)
        x = left
        while x < rect.right():
            painter.drawLine(x, rect.top(), x, rect.bottom())
            x += grid
        y = top
        while y < rect.bottom():
            painter.drawLine(rect.left(), y, rect.right(), y)
            y += grid
        painter.restore()
