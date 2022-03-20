from typing import Any
from app.gui.components.form.inputs.Input import Input
from PySide6.QtWidgets import QDateTimeEdit, QDateEdit
from PySide6.QtCore import Slot, QDateTime, QDate, Qt

from app.constants import Constants


class DateTimeInput(Input[QDateTimeEdit]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDateTimeEdit.html
    # https://doc.qt.io/qtforpython/PySide6/QtCore/QDateTime.html
    def __init__(self, label: str | None = None):
        super(DateTimeInput, self).__init__(QDateTimeEdit())
        self.setObjectName("Input:DateTimeInput:" + str(label))

        self._isModified: bool = False
        self._input.setCalendarPopup(True)
        self._input.dateTimeChanged.connect(lambda: self.modified.emit(True))
        # self._input.setDate(QDateTime.currentDateTime().date())
        self._input.setDisplayFormat(Constants.DATE_FORMAT)
        # setMinimumDateTime (dt: QDateTime)

        if label:
            self.setLabel(label)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        self._input.setDateTime(getattr(self._boundObject, self._boundProperty))

        self._input.dateTimeChanged.connect(self._onDateTimeChanged)

    @Slot(str)
    def _onDateTimeChanged(self, datetime: QDateTime):
        self.updateBoundObject(self._boundObject, datetime.toPython())

        self._isModified = True

    def isModified(self) -> bool:
        return self._isModified
