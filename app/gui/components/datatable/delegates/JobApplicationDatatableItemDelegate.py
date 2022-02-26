from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QStyle
from PySide6.QtGui import QPainter, QPixmap, QColor, QCursor, QPainterPath, QPen, QBrush
from PySide6.QtCore import (
    QModelIndex,
    QPersistentModelIndex,
    QSize,
    QRect,
    Qt,
    QPoint,
    QRectF,
)
from app.gui.components.datatable.models.JobApplicationDatatableModel import (
    JobApplicationDatatableModel,
)

from app.utilities.IconUtility import IconUtility


class JobApplicationDatatableItemDelegate(QStyledItemDelegate):
    requiresFollowUpIconTrue: QPixmap
    requiresFollowUpIconFalse: QPixmap

    def __init__(self, parent: JobApplicationDatatableModel) -> None:
        super(JobApplicationDatatableItemDelegate, self).__init__(parent)

        self._model: JobApplicationDatatableModel = parent
        self._model.datatable.setMouseTracking(True)

        # Sets background to opaque
        # self._model.datatable.setAutoFillBackground(true)

        self.requiresFollowUpIconTrue = IconUtility.getFileIconAsPixmap("light-bulb-24")
        self.requiresFollowUpIconFalse = IconUtility.getFileIconAsPixmap(
            "light-bulb-off-24"
        )

    def paintRowBorder(
        self,
        painter: QPainter,
        option: QStyleOptionViewItem,
        index: QModelIndex | QPersistentModelIndex,
    ):
        painter.save()

        BORDER_WIDTH = 3

        painter.setRenderHint(QPainter.Antialiasing)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        # painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        # Create the path
        path = QPainterPath()

        # Create the pen
        pen = QPen(QColor(170, 170, 170), BORDER_WIDTH)
        painter.setPen(pen)

        brush = QBrush(Qt.red)
        painter.setBrush(brush)

        leftMostColumn = index.siblingAtColumn(0)
        rightMostColumn = index.siblingAtColumn(self._model.columnCount(index))

        topLeftX = self._model.datatable.columnViewportPosition(0)
        topLeftY = self._model.datatable.rowViewportPosition(index.row())

        bottomRightX = topLeftX + self._model.datatable.width() - 20
        bottomRightY = topLeftY + self._model.datatable.rowHeight(index.row())

        rowRect = QRectF(QPoint(topLeftX, topLeftY), QPoint(bottomRightX, bottomRightY))

        # Slighly shrink dimensions to account for bordersize
        rowRect.adjust(
            BORDER_WIDTH / 2, BORDER_WIDTH / 2, -BORDER_WIDTH / 2, -BORDER_WIDTH / 2
        )
        # painter.setClipRect(option.rect) # Does the same thing

        # Add the rect to path
        path.addRoundedRect(rowRect, 12, 12)
        painter.setClipPath(path)

        # Fill shape, draw the border and center the text
        painter.fillPath(path, painter.brush())
        painter.strokePath(path, painter.pen())

        painter.restore()

    def paint(
        self,
        painter: QPainter,
        option: QStyleOptionViewItem,
        index: QModelIndex | QPersistentModelIndex,
    ) -> None:
        """Paint the items in the table."""
        painter.save()

        modelData = self._model.getModelData(index)

        # self.paintRowBorder(painter, option, index)

        # Hover state
        hoverRow = self._model.datatable.indexAtCursor

        if not (option.state & QStyle.State_Selected) and index.row() == hoverRow.row():
            # Change background colour
            # painter.fillRect(option.rect, QColor(221, 239, 254))
            # painter.fillRect(option.rect, QColor(171, 204, 252))
            painter.fillRect(option.rect, Qt.white)

            # Change cursor
            self._model.datatable.setCursor(Qt.PointingHandCursor)

        if option.state & QStyle.State_Selected:
            option.state = option.state ^ QStyle.State_Selected

        # Display icon for Requires Followup column
        if modelData.column == "requires_followup":
            if modelData.value:
                painter.drawPixmap(
                    self._getCenteredIconCoords(option, self.requiresFollowUpIconTrue),
                    self.requiresFollowUpIconTrue,
                )
            else:
                painter.drawPixmap(
                    self._getCenteredIconCoords(option, self.requiresFollowUpIconFalse),
                    self.requiresFollowUpIconFalse,
                )

        # Focus state - removes focus state styles
        if option.state & QStyle.State_HasFocus:
            option.state = option.state ^ QStyle.State_HasFocus

        # QColor(255,0,0)
        # Qt.GlobalColor.lightGray
        # option.palette.highlight()
        painter.restore()

        return super().paint(painter, option, index)  # standard processing

    def sizeHint(
        self, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex
    ) -> QSize:
        """Returns the size needed to display the item in a QSize object."""
        modelData = self._model.getModelData(index)

        if modelData.column == "requires_follwup":
            if modelData.value:
                return self.requiresFollowUpIconTrue.size()
            else:
                return self.requiresFollowUpIconFalse.size()

        return super().sizeHint(option, index)  # standard processing

    def _getCenteredIconCoords(
        self, option: QStyleOptionViewItem, icon: QPixmap
    ) -> QRect:
        colCoords: QRect = option.rect
        colWidth: int = colCoords.width()
        colHeight: int = colCoords.height()
        colX: int = colCoords.topLeft().x()
        colY: int = colCoords.topLeft().y()

        iconX: int = int(colX + (colWidth / 2) - (icon.width() / 2))
        iconY: int = int(colY + (colHeight / 2) - (icon.height() / 2)) - 5

        return QRect(iconX, iconY, icon.width(), icon.height())
