from typing import Any, Sequence
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QPersistentModelIndex
from PySide6.QtWidgets import QWidget, QComboBox
from app.gui.components.models.ListModel import ListModel

from app.models.Profession import Profession


class ProfessionListModel(ListModel[Profession]):
    def __init__(self, parentWidget, *args, **kwargs):
        professions: Sequence[Profession] = (
            Profession.order_by("profession").get().all()
        )

        super(ProfessionListModel, self).__init__(parentWidget, professions, *args, **kwargs)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> Any:
        profession = self._data[index.row()]

        match role:
            case Qt.DisplayRole:
                return profession.profession

            case Qt.EditRole:
                return profession.profession

            case Qt.UserRole:
                return profession

                # case Qt.WhatsThisRole:
                # case Qt.DecorationRole:
                # case Qt.SizeHintRole:
                # case Qt.ToolTipRole:
                # case Qt.StatusTipRole:
