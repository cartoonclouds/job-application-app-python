# Framework imports
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem

# Application imports
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.models import JobApplicationDatatableModel


class DatatableItemDelegate(QStyledItemDelegate):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QStyledItemDelegate.html
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QItemDelegate.html
    def __init__(self) -> None:
        super(DatatableItemDelegate, self).__init__()

    @property
    def datatable(self) -> Datatable:
        return self.parent()

    @property
    def datatableModel(
        self,
    ) -> JobApplicationDatatableModel.JobApplicationDatatableModel:
        return self.datatable.model()

    def setParent(self, parent: Datatable) -> None:
        parent.setMouseTracking(True)

        return super().setParent(parent)

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
