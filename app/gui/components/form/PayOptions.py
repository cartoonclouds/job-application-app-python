# Standard Library
from functools import partial

# Framework imports
from PySide6.QtCore import QMargins, Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QSplitter,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from app.gui.components.form.inputs.Input import Input

# Application imports
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextInput import TextInput
from app.models.Job import Job
from app.constants import Constants
from app.utils.EnumUtility import PayTypes, PayUnits


class PayOptions(QWidget):
    modified = Signal(bool)

    def __init__(
        self, label: str, model: Job, initialOption: PayTypes = PayTypes.RATE
    ) -> None:
        super().__init__()

        self._model = model
        self._initialOption = initialOption
        self.setObjectName("Input:PayOptions:" + label)

        layout = QHBoxLayout()
        layout.setContentsMargins(Constants.ZERO_MARGINS)
        layout.setSpacing(Constants.WIDGET_SPACING)

        stackWidget = self._setupStacks()
        self._stacks: QStackedLayout = stackWidget.layout()
        self._stacks.setCurrentIndex(PayTypes.atIndex(initialOption))

        self._label = Input.createLabel(label, self)
        # self._label.setStyleSheet("border: 2px solid red;")

        optionsLayout = QVBoxLayout()
        optionsLayout.setContentsMargins(0, Constants.WIDGET_SPACING / 2, 0, 0)
        optionsStack = self._setupOptions()
        optionsFrame = QWidget()
        optionsFrame.setLayout(optionsLayout)

        optionsLayout.addWidget(optionsStack)
        optionsLayout.addWidget(stackWidget)

        # optionsFrame.setStyleSheet("border: 2px solid red;")
        # optionsStack.setStyleSheet("border: 2px solid green;")
        # stackWidget.setStyleSheet("border: 2px solid blue;")

        # layout.addWidget(labelWidget)
        layout.addWidget(optionsFrame)

        self.setLayout(layout)

    def setLabel(self, label: str):
        self._label.setText(label)
        self._label.show()

    def getLabel(self) -> QLabel | None:
        return self._label

    def _setupOptions(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Constants.ZERO_MARGINS)
        frame = QWidget()
        frame.setLayout(layout)

        salaryOption = QRadioButton("Salary")
        rateOption = QRadioButton("Rate")

        salaryOption.setChecked(self._initialOption == PayTypes.SALARY)
        rateOption.setChecked(self._initialOption == PayTypes.RATE)

        salaryOption.toggled.connect(partial(self._setOption, PayTypes.SALARY))
        rateOption.toggled.connect(partial(self._setOption, PayTypes.RATE))

        salaryOption.toggled.connect(lambda: self.modified.emit(self.isModified()))
        rateOption.toggled.connect(lambda: self.modified.emit(self.isModified()))

        layout.addWidget(salaryOption)
        layout.addWidget(rateOption)

        return frame

    def _setupStacks(self):
        layout = QStackedLayout()
        frame = QWidget()

        salaryContainer, self.salaryInput = self._setupSalary()
        rateContainer, self.rateInput, self.rateUnits = self._setupRate()

        self.salaryInput.modified.connect(lambda: self.modified.emit(self.isModified()))
        self.rateInput.modified.connect(lambda: self.modified.emit(self.isModified()))
        self.rateUnits.modified.connect(lambda: self.modified.emit(self.isModified()))

        layout.addWidget(salaryContainer)
        layout.addWidget(rateContainer)

        frame.setLayout(layout)

        return frame

    def _setupRate(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Constants.ZERO_MARGINS)
        rateWidget = QWidget()
        rateWidget.setLayout(layout)

        input = TextInput("Rate")
        input.setBinding(self._model, "rate")
        input.setPrefix("$")
        input.setInputMask("##.##")
        input.setPlaceholderText("##.##")

        label = QLabel("per")
        label.setAlignment(Qt.AlignBottom)
        labelMargin = label.contentsMargins()
        labelMargin.setBottom(6)  # TODO Make dynamic to text height
        label.setContentsMargins(labelMargin)

        unitInput = SelectBox("Rate Units")
        unitInput.setAlignment(Qt.AlignBottom)

        unitInput.addItems(PayUnits.AS_LIST())
        unitInput.setBinding(self._model, "rate_unit")
        unitInputMargin = unitInput.contentsMargins()
        unitInputMargin.setBottom(0)  # TODO Make dynamic to text height
        unitInput.setContentsMargins(unitInputMargin)

        layout.addWidget(input)
        layout.addWidget(label)
        layout.addWidget(unitInput)

        return rateWidget, input, unitInput

    def _setupSalary(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Constants.ZERO_MARGINS)
        salaryWidget = QWidget()
        salaryWidget.setLayout(layout)

        salaryInput = TextInput()
        salaryInput.setBinding(self._model, "salary")
        salaryInput.setPrefix("$")
        salaryInput.setSuffix("per year")
        salaryInput.setInputMask("##.##")
        salaryInput.setPlaceholderText("$##.##")

        label = QLabel("per year")
        label.setAlignment(Qt.AlignBottom)
        labelMargin = label.contentsMargins()
        labelMargin.setBottom(6)  # TODO Make dynamic to text height
        label.setContentsMargins(labelMargin)

        layout.addWidget(salaryInput)
        layout.addWidget(label)

        return salaryWidget, salaryInput

    def _setOption(self, payType: PayTypes, checked: None | bool = None):
        stackIndex = PayTypes.atIndex(payType)
        self._stacks.setCurrentIndex(stackIndex)

        setattr(self._model, "pay_option", payType)

        debug(self._model, dict(zip(["pay_option"], [payType])))

    def isModified(self) -> bool:
        return (
            PayTypes.atIndex(self._initialOption) != self._stacks.currentIndex()
            or self.salaryInput.isModified()
            or self.rateInput.isModified()
            or self.rateUnits.isModified()
        )
