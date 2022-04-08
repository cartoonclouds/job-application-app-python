# Standard Library
from typing import Any, Sequence

# Framework imports
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

# Application imports
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.models.ListModel import ListModel
from app.models.Profession import Profession
from app.repositories.profession_repository import ProfessionRepository


class EmploymentTypeListModel(ListModel[Profession]):
    def __init__(self, parentWidget: SelectBox, *args: Any, **kwargs: Any):
        data = ProfessionRepository.items()

        super(EmploymentTypeListModel, self).__init__(
            parentWidget, data, *args, **kwargs
        )

    def data(
        self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole
    ) -> Any:
        profession = self._data[index.row() + 1]

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
