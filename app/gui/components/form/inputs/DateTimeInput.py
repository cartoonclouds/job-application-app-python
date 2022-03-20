from typing import Any
from app.gui.components.form.inputs.Input import Input
from PySide6.QtWidgets import QDateTimeEdit, QDateEdit
from PySide6.QtCore import Slot, QDateTime, QDate, Qt
import datetime
from pendulum import Pendulum

from app.constants import Constants


class DateTimeInput(Input[QDateTimeEdit]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDateTimeEdit.html
    # https://doc.qt.io/qtforpython/PySide6/QtCore/QDateTime.html
    def __init__(self, label: str | None = None):
        super(DateTimeInput, self).__init__(QDateTimeEdit())
        self.setObjectName("Input:DateTimeInput:" + str(label))

        self._isModified: bool = False
        self._input.setCalendarPopup(True)
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

        self._initialPropertyValue = getattr(self._boundObject, self._boundProperty)

        self._input.setDateTime(self._initialPropertyValue)

        self._input.dateTimeChanged.connect(self._onDateTimeChanged)
        self._input.dateTimeChanged.connect(
            lambda: self.modified.emit(self.isModified())
        )

    @Slot(str)
    def _onDateTimeChanged(self, datetime: QDateTime):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, datetime.toPython())

    def isModified(self) -> bool:
        initialDt = Pendulum.instance(self._initialPropertyValue)
        inputDt = Pendulum.instance(self._input.dateTime().toPython())

        return (
            initialDt.to_formatted_date_string() == inputDt.to_formatted_date_string()
        )
