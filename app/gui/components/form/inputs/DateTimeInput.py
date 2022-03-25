# Framework imports
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
        super(DateTimeInput, self).__init__(QDateTimeEdit(), str(label))

        self._input.setCalendarPopup(True)
        self._input.setDisplayFormat(DATE_FORMAT_1)

        if label is not None:
            self.setLabel(label)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        initialDateTime = getattr(
            self._boundObject,
            self._boundProperty,
            QDateTime.currentDateTime().date(),
        )

        self._input.setDateTime(initialDateTime)

        self._input.dateTimeChanged.connect(self._onDateTimeChanged)

    @Slot(str)
    def _onDateTimeChanged(self, datetime: QDateTime):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, datetime.toPython())
