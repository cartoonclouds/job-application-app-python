from typing import Type, TypeAlias, TypeVar

from app.models.Company import Company
from app.models.Profession import Profession
from app.models.JobApplication import JobApplication
from app.models.Job import Job
from app.models.Action import Action
from typing import Any, Sequence, TypeVar, Generic, TypeAlias

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QPlainTextEdit,
    QComboBox,
    QPushButton,
    QDateTimeEdit,
    QDoubleSpinBox,
    QCheckBox
)
from typing import TypeVar, Generic



# Mypy is a static type checker for Python 3
# https://mypy.readthedocs.io/en/stable/introduction.html
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# https://realpython.com/python-type-checking/

# https://docs.python.org/3/library/typing.html
# https://python.github.io/peps/pep-0484/
# https://python.github.io/peps/pep-0484/#generics
# https://mypy.readthedocs.io/en/stable/generics.html

# # type: IO[str]
# # type: ignore
# @no_type_check, a decorator to disable type checking per class or function (see below)
# @no_type_check_decorator, a decorator to create your own decorators with the same meaning as @no_type_check (see below)

# T = TypeVar("T")  # Declare type variable. Use for generics
# M = TypeVar("M", bound=Models.Model)
# DTM = TypeVar("DTM", bound=DatatableModel)
# M_co = TypeVar("M_co", bound=Models.Model, covariant=True)

# DM = TypeVar("DM", JobApplicationDatatableModel, ActionDatatableModel)


TModel = JobApplication | Profession | Job | Action | Company


M = TypeVar("M", JobApplication, Profession, Job, Action, Company)

T = TypeVar(
    "T",
    QComboBox,
    QPlainTextEdit,
    QLineEdit,
    QDateTimeEdit,
    QPushButton,
    QDoubleSpinBox,
    QCheckBox
)

# You can use a ClassVar[t] annotation to explicitly declare that a particular attribute should not be set on instances:
#  https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations


# https://mypy.readthedocs.io/en/stable/literal_types.html#parameterizing-literals
