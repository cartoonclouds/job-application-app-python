from typing import Any, Iterable, Sequence, Type, TypeVar, Generic, TypeAlias, Union
from app.gui.components.EditableLabel.EditableLabel import EditableLabel
from app.gui.components.form.PayOptions import PayOptions
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.NumberInput import NumberInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.form.inputs.ToggleButton import ToggleButton
from app.gui.components.form.inputs.ToggleButtonSquare import ToggleButtonSquare

from app.models.Model import Model
from PySide6.QtCore import QAbstractTableModel

from app.models.Profession import Profession
from app.models.Job import Job
from app.models.Action import Action
from app.models.Company import Company
from app.models.JobApplication import JobApplication

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QDateTimeEdit,
    QDoubleSpinBox,
    QComboBox,
    QPlainTextEdit,
    QCheckBox,
    QPushButton,
)


InputT: TypeAlias = (
    DateTimeInput
    | EditableLabel
    | NumberInput
    | PayOptions
    | SelectBox
    | TextAreaInput
    | TextInput
    | ToggleButton
    | ToggleButtonSquare
)


InputTVar = TypeVar("InputTVar", bound=QWidget)

InputTTVar = TypeVar(
    "InputTTVar",
    DateTimeInput,
    EditableLabel,
    NumberInput,
    PayOptions,
    SelectBox,
    TextAreaInput,
    TextInput,
    ToggleButton,
    ToggleButtonSquare,
    QWidget,
)

PySide6Input = TypeVar(
    "PySide6Input",
    bound=Union[
        QWidget,
        QLineEdit,
        QDateTimeEdit,
        QDoubleSpinBox,
        QComboBox,
        QPlainTextEdit,
        QCheckBox,
        QPushButton,
    ],
)
M = TypeVar("M", bound=Model, covariant=True)
DTM = TypeVar("DTM", bound=QAbstractTableModel, covariant=True)

# ModelT = TypeVar(
#     "ModelT",
#     models.JobApplication.JobApplication,
#     models.Profession.Profession,
#     models.Job.Job,
#     models.Action.Action,
#     models.Company.Company,
# )
Models = TypeVar("Models", JobApplication, Profession, Job, Action, Company)


# Mypy is a static type checker for Python 3
# https://mypy.readthedocs.io/en/stable/introduction.html
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# https://realpython.com/python-type-checking/

# https://docs.python.org/3/library/typing.html
# https://python.github.io/peps/pep-0484/
# https://python.github.io/peps/pep-0484/#generics
# https://mypy.readthedocs.io/en/stable/generics.html


# You can use a ClassVar[t] annotation to explicitly declare that a particular attribute should not be set on instances:
#  https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations


# https://mypy.readthedocs.io/en/stable/literal_types.html#parameterizing-literals
