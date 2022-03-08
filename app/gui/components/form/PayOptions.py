from functools import partial
from PySide6.QtWidgets import (
    QVBoxLayout,
    QSplitter,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QStackedLayout,
    QWidget,
    QRadioButton,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QMargins
from app.gui.components.form.inputs.SelectBox import SelectBox

from app.gui.components.form.inputs.TextInput import TextInput
from app.models.Job import Job
from app.storage import Storage
from app.utils.EnumUtility import PayTypes, PayUnits


class PayOptions(QWidget):
    def __init__(
        self, label: str, model: Job, initialOption: PayTypes = PayTypes.SALARY
    ) -> None:
        super().__init__()

        self._model = model
        self._initialOption = initialOption

        layout = QVBoxLayout()
        layout.setContentsMargins(Storage.ZERO_MARGINS)
        layout.setSpacing(Storage.WIDGET_SPACING)
        stackWidget = self._setupStacks()
        self._stacks: QStackedLayout = stackWidget.layout()

        labelWidget = QLabel(label)
        labelFont = labelWidget.font()
        labelFont.setPointSize(Storage.FORM_LABEL_SIZE)
        labelFont.setCapitalization(QFont.SmallCaps)
        labelWidget.setFont(labelFont)

        optionsStack = self._setupOptions()

        # labelWidget.setStyleSheet("border: 2px solid red;")
        # optionsStack.setStyleSheet("border: 2px solid green;")
        # stackWidget.setStyleSheet("border: 2px solid blue;")

        layout.addWidget(labelWidget)
        layout.addWidget(optionsStack)
        layout.addWidget(stackWidget)

        self._setOption(initialOption)

        self.setLayout(layout)

    def _setupOptions(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Storage.ZERO_MARGINS)
        frame = QWidget()
        frame.setLayout(layout)

        salaryOption = QRadioButton("Salary")
        rateOption = QRadioButton("Rate")

        # pay_option

        salaryOption.setChecked(self._initialOption == PayTypes.SALARY)
        rateOption.setChecked(self._initialOption == PayTypes.RATE)

        salaryOption.toggled.connect(partial(self._setOption, PayTypes.SALARY))
        rateOption.toggled.connect(partial(self._setOption, PayTypes.RATE))

        layout.addWidget(salaryOption)
        layout.addWidget(rateOption)

        return frame

    def _setupStacks(self):
        layout = QStackedLayout()
        frame = QWidget()

        layout.addWidget(self._setupSalary())
        layout.addWidget(self._setupRate())

        layout.setCurrentIndex(1)

        frame.setLayout(layout)

        return frame

    def _setupRate(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Storage.ZERO_MARGINS)
        rateWidget = QWidget()
        rateWidget.setLayout(layout)

        input = TextInput()  # double('salary', 8)
        input.setBinding(self._model, "rate")
        input.setPrefix("$")
        input.setInputMask("##.##")
        input.setPlaceholderText("##.##")

        label = QLabel("per")
        label.setAlignment(Qt.AlignBottom)
        labelMargin = label.contentsMargins()
        labelMargin.setBottom(6)  # TODO Make dynamic to text height
        label.setContentsMargins(labelMargin)

        unitInput = SelectBox()
        unitInput.setAlignment(Qt.AlignBottom)

        unitInput.addItems(PayUnits.AS_LIST())
        unitInput.setBinding(self._model, "rate_unit")
        unitInputMargin = unitInput.contentsMargins()
        unitInputMargin.setBottom(0)  # TODO Make dynamic to text height
        unitInput.setContentsMargins(unitInputMargin)

        layout.addWidget(input)
        layout.addWidget(label)
        layout.addWidget(unitInput)

        return rateWidget

    def _setupSalary(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Storage.ZERO_MARGINS)
        salaryWidget = QWidget()
        salaryWidget.setLayout(layout)

        salaryInput = TextInput()  # double('salary', 8)
        salaryInput.setBinding(self._model, "salary")
        salaryInput.setPrefix("$")
        # salaryInput.setSuffix("per year")
        salaryInput.setInputMask("##.##")
        salaryInput.setPlaceholderText("$##.##")

        label = QLabel("per year")
        label.setAlignment(Qt.AlignBottom)
        labelMargin = label.contentsMargins()
        labelMargin.setBottom(6)  # TODO Make dynamic to text height
        label.setContentsMargins(labelMargin)

        layout.addWidget(salaryInput)
        layout.addWidget(label)

        return salaryWidget

    def _setOption(self, payType: PayTypes, checked: None | bool = None):
        stackIndex = PayTypes.atIndex(payType)

        self._stacks.setCurrentIndex(stackIndex)
