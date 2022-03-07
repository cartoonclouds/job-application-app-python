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
    QObject,
)
from app.gui.components.datatable.DatatableItemDelegate import DatatableItemDelegate

from app.utilities.IconUtility import IconUtility


class JobApplicationDatatableItemDelegate(DatatableItemDelegate):
    requiresFollowUpIconTrue: QPixmap
    requiresFollowUpIconFalse: QPixmap

    def __init__(self) -> None:
        super(JobApplicationDatatableItemDelegate, self).__init__()

        # Sets background to opaque
        # self.datatable.setAutoFillBackground(true)

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
        rightMostColumn = index.siblingAtColumn(self.datatableModel.columnCount(index))

        topLeftX = self.datatable.columnViewportPosition(0)
        topLeftY = self.datatable.rowViewportPosition(index.row())

        bottomRightX = topLeftX + self.datatable.width() - 20
        bottomRightY = topLeftY + self.datatable.rowHeight(index.row())

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

        modelData = self.datatableModel.getModelData(index)

        # self.paintRowBorder(painter, option, index)

        # Hover state
        hoverRow = self.datatable.indexAtCursor

        if not (option.state & QStyle.State_Selected) and index.row() == hoverRow.row():
            # Change background colour
            # painter.fillRect(option.rect, QColor(221, 239, 254))
            # painter.fillRect(option.rect, QColor(171, 204, 252))
            painter.fillRect(option.rect, Qt.white)

            # Change cursor
            self.datatable.setCursor(Qt.PointingHandCursor)

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
        modelData = self.datatableModel.getModelData(index)

        if modelData.column == "requires_follwup":
            if modelData.value:
                return self.requiresFollowUpIconTrue.size()
            else:
                return self.requiresFollowUpIconFalse.size()

        return super().sizeHint(option, index)  # standard processing
