
from re import S
from typing import Type, TypeVar
import typing

from PySide6 import QtGui

# Mypy is a static type checker for Python 3
# https://mypy.readthedocs.io/en/stable/introduction.html
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# https://realpython.com/python-type-checking/

# https://docs.python.org/3/library/typing.html
# https://python.github.io/peps/pep-0484/
# https://python.github.io/peps/pep-0484/#generics
# https://mypy.readthedocs.io/en/stable/generics.html

Id = str

T = TypeVar('T')  # Declare type variable. Use for generics

ColumnName = str
TableHeader = str

TableHeaders = typing.Sequence[TableHeader]
ColumnNames = typing.Sequence[ColumnName]

ColumnHeaders = typing.Mapping[ColumnName, TableHeader]

TabDetails = typing.Dict[str, str | bool | QtGui.QIcon]


# You can use a ClassVar[t] annotation to explicitly declare that a particular attribute should not be set on instances:
#  https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations


# https://mypy.readthedocs.io/en/stable/literal_types.html#parameterizing-literals

#

# Pydantic - validation / Using Types at Runtime
# https://pypi.org/project/pydantic/
# https://medium.com/swlh/cool-things-you-can-do-with-pydantic-fc1c948fbde0
# https://pydantic-docs.helpmanual.io/


# https://pypi.org/project/parse/
