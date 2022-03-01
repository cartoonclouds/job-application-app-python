from typing import Any
from app.gui.components.form.inputs.Input import Input, UpdateEvent
from PySide6.QtWidgets import QDateTimeEdit, QDateEdit
from PySide6.QtCore import Slot, QDateTime, QDate


class DateTimeInput(Input):
    def __init__(self, label: str | None = None):
        super(DateTimeInput, self).__init__(QDateTimeEdit)

        self._input.setCalendarPopup(True)
        # self._input.setDate(QDateTime.currentDateTime().date())
        # setDisplayFormat()
        # setMinimumDateTime (dt: QDateTime)
    
        if label:
            self.setLabel(label)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateEvent: UpdateEvent = UpdateEvent.ON_CHANGE,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateEvent = updateEvent

        self._input.setDateTime(getattr(self._boundObject, self._boundProperty))
        # self._input.setDateTime(QDateTime.currentDateTime())

        if self._updateEvent == UpdateEvent.ON_CHANGE:
            self._input.dateTimeChanged.connect(self._onDateTimeChanged)

    @Slot(str)
    def _onDateTimeChanged(self, datetime: QDateTime):
        debug(datetime, datetime.toString())
        setattr(self._boundObject, self._boundProperty, datetime.toString())
