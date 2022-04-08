# Standard Library
from typing import Any, Sequence

# Framework imports
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

# Application imports
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.models.ListModel import ListModel
from app.models.Profession import Profession
from app.repositories.profession_repository import ProfessionRepository


class ProfessionListModel(ListModel[Profession]):
    def __init__(self, parentWidget: SelectBox, *args: Any, **kwargs: Any):
        data = ProfessionRepository.items()

        super(ProfessionListModel, self).__init__(parentWidget, data, *args, **kwargs)

    def data(
        self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole
    ) -> Any:

        # debug(self._data)

        profession = self._data[index.row()]

        match role:
            case Qt.DisplayRole:
                return profession.profession

            case Qt.EditRole:
                return profession.profession

            case Qt.UserRole:
                return profession
