
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, QSize, QRect
from app.gui.components.datatable.models.DatatableModel import DatatableModel

from app.utilities.IconUtility import IconUtility


class FollowUpItemDelegate(QStyledItemDelegate):
    requiresFollowUpIconTrue: QPixmap
    requiresFollowUpIconFalse: QPixmap

    def __init__(self, parent: DatatableModel) -> None:
        super(FollowUpItemDelegate, self).__init__(parent)

        self._model: DatatableModel = parent

        self.requiresFollowUpIconTrue = IconUtility.getFileIconAsPixmap(
            "light-bulb-24")
        self.requiresFollowUpIconFalse = IconUtility.getFileIconAsPixmap(
            "light-bulb-off-24")

    def _getCenteredIconCoords(self, option: QStyleOptionViewItem, icon: QPixmap) -> QRect:
        colCoords: QRect = option.rect
        colWidth: int = colCoords.width()
        colHeight: int = colCoords.height()
        colX: int = colCoords.topLeft().x()
        colY: int = colCoords.topLeft().y()

        iconX: int = int(colX + (colWidth / 2) - (icon.width() / 2))
        iconY: int = int(colY + (colHeight / 2) - (icon.height() / 2))

        return QRect(iconX, iconY, icon.width(), icon.height())

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> None:
        """ Paint the items in the table.

            If the item referred to by <index> is a StarRating, we handle the
            painting ourselves. For the other items, we let the base class
            handle the painting as usual.
            In a polished application, we'd use a better check than the 
            column number to find out if we needed to paint the stars, but
            it works for the purposes of this example.
        """
        modelData = self._model.getModelData(index)

        if modelData.value:
            painter.drawPixmap(self._getCenteredIconCoords(
                option, self.requiresFollowUpIconTrue), self.requiresFollowUpIconTrue)
        else:
            painter.drawPixmap(self._getCenteredIconCoords(
                option, self.requiresFollowUpIconFalse), self.requiresFollowUpIconFalse)

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> QSize:
        """ Returns the size needed to display the item in a QSize object. """
        modelData = self._model.getModelData(index)

        if modelData.value:
            return self.requiresFollowUpIconTrue.size()
        else:
            return self.requiresFollowUpIconFalse.size()
