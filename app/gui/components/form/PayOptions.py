# Standard Library
from functools import partial
from typing import TypeVar, cast

# Framework imports
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

# Application imports
from app.constants import WIDGET_SPACING, ZERO_MARGINS
from app.enums import PayTypes, PayUnits
from app.gui.components.form.inputs.Input import Input
from app.gui.components.form.inputs.NumberInput import NumberInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextInput import TextInput
from app.models.Job import Job
from app.typings.types import PySide6Input


class PayOptions(Input[QWidget]):
    modified = Signal(bool)

    def __init__(
        self, label: str, model: Job, initialOption: PayTypes = PayTypes.SALARY
    ) -> None:
        self._model = model
        self._initialOption = initialOption
        self._emittingInputs: list[Input[PySide6Input]] = list()

        stackWidget = self._setupStacks()
        self._stacks = cast(QStackedLayout, stackWidget.layout())
        self._stacks.setCurrentIndex(PayTypes.index(initialOption))

        optionsLayout = QVBoxLayout()
        optionsLayout.setContentsMargins(0, int(WIDGET_SPACING / 2), 0, 0)
        optionsStack = self._setupOptions()
        optionsFrame = QWidget()
        optionsFrame.setLayout(optionsLayout)

        optionsLayout.addWidget(optionsStack)
        optionsLayout.addWidget(stackWidget)

        # self._label.setStyleSheet("border: 2px solid red;")
        # optionsFrame.setStyleSheet("border: 2px solid red;")
        # optionsStack.setStyleSheet("border: 2px solid green;")
        # stackWidget.setStyleSheet("border: 2px solid blue;")

        super(PayOptions, self).__init__(optionsFrame, label or "")

        if label is not None:
            self.setLabel(label)

    def _setupOptions(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(ZERO_MARGINS)
        frame = QWidget()
        frame.setLayout(layout)

        salaryOption = QRadioButton("Salary")
        salaryOption.setChecked(self._initialOption == PayTypes.SALARY)
        salaryOption.toggled.connect(partial(self._setOption, PayTypes.SALARY))

        rateOption = QRadioButton("Rate")
        rateOption.setChecked(self._initialOption == PayTypes.RATE)
        rateOption.toggled.connect(partial(self._setOption, PayTypes.RATE))

        layout.addWidget(salaryOption)
        layout.addWidget(rateOption)

        return frame

    def _setupStacks(self):
        layout = QStackedLayout()
        frame = QWidget()

        salaryInput = self._setupSalary()
        rateWidget = self._setupRate()

        self._setupEmittingInputs()

        layout.addWidget(salaryInput)
        layout.addWidget(rateWidget)

        frame.setLayout(layout)

        return frame

    def _setupRate(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(ZERO_MARGINS)
        rateWidget = QWidget()
        rateWidget.setLayout(layout)

        rateInput = NumberInput("Rate")
        rateInput.setBinding(self._model, "rate")
        # rateInput.setPrefix("$")
        rateInput.setDecimals(2)
        rateInput.setSingleStep(0.01)

        label = QLabel("per")
        label.setAlignment(Qt.AlignBottom)
        labelMargin = label.contentsMargins()
        labelMargin.setBottom(6)  # TODO Make dynamic to text height
        label.setContentsMargins(labelMargin)

        unitInput = SelectBox("Rate Units")
        unitInput.setAlignment(Qt.AlignBottom)
        unitInput.addItems(PayUnits.VALUES())
        unitInput.setBinding(self._model, "rate_unit")

        unitInputMargin = unitInput.contentsMargins()
        unitInputMargin.setBottom(0)  # TODO Make dynamic to text height
        unitInput.setContentsMargins(unitInputMargin)

        layout.addWidget(rateInput)
        layout.addWidget(label)
        layout.addWidget(unitInput)

        self._emittingInputs.append(rateInput)
        self._emittingInputs.append(unitInput)

        return rateWidget

    def _setupSalary(self):
        salaryInput = TextInput()
        salaryInput.setBinding(self._model, "salary")
        salaryInput.setPrefix("$")
        salaryInput.setSuffix("per year")
        salaryInput.setInputMask("##.##")
        salaryInput.setPlaceholderText("$##.##")

        self._emittingInputs.append(salaryInput)

        return salaryInput

    def _setOption(self, payType: PayTypes, checked: None | bool = None):
        if checked:
            stackIndex = PayTypes.index(payType)
            self._stacks.setCurrentIndex(stackIndex)

            setattr(self._model, "pay_option", payType)

            self.modified.emit(self.isModified())

            debug(self._model, dict(zip(["pay_option"], [payType])))

    def _setupEmittingInputs(self):
        # Required because form only emits 'modified' on attached components and this
        # is PayOptions - not the inner components. Therefore inner components need to
        # also make PayOptions emit.
        for input in self._emittingInputs:
            input.modified.connect(lambda: self.modified.emit(self.isModified()))

    def isModified(self) -> bool:
        return (
            any([input.isModified() for input in self._emittingInputs])
            or PayTypes.index(self._initialOption) != self._stacks.currentIndex()
        )
