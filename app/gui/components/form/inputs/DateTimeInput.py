# Framework imports
from typing import Type
from PySide6.QtCore import QDateTime, Slot
from PySide6.QtWidgets import QDateTimeEdit

# Application imports
from app.constants import DATE_FORMAT_1
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class DateTimeInput(Input[QDateTimeEdit]):
    """
    URL: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDateTimeEdit.html
         https://doc.qt.io/qtforpython/PySide6/QtCore/QDateTime.html
    """

    def __init__(self, label: str | None = None):
        super(DateTimeInput, self).__init__(QDateTimeEdit(), label)

        self.baseWidget.setCalendarPopup(True)
        self.baseWidget.setDisplayFormat(DATE_FORMAT_1)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.baseWidget.setDateTime(self.boundValue(QDateTime.currentDateTime().date()))

        self.baseWidget.dateTimeChanged.connect(self._onDateTimeChanged)

    @Slot(str)
    def _onDateTimeChanged(self, datetime: QDateTime):
        assert self._boundObject is not None
        self.updateBoundObject(datetime.toPython())
