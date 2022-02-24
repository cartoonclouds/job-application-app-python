
from typing import Type, TypeAlias, TypeVar
import typing


from app.gui.components.tabs import Tab as TabComponent


# Mypy is a static type checker for Python 3
# https://mypy.readthedocs.io/en/stable/introduction.html
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# https://realpython.com/python-type-checking/

# https://docs.python.org/3/library/typing.html
# https://python.github.io/peps/pep-0484/
# https://python.github.io/peps/pep-0484/#generics
# https://mypy.readthedocs.io/en/stable/generics.html


# Tabs: TypeAlias = TabsComponent.Tabs
Tab: TypeAlias = TabComponent.Tab

Id = str

T = TypeVar('T')  # Declare type variable. Use for generics

ColumnName: TypeAlias = str
TableHeader: TypeAlias = str

TableHeaders: TypeAlias = typing.Sequence[TableHeader]
ColumnNames: TypeAlias = typing.Sequence[ColumnName]

ColumnHeaders: TypeAlias = typing.Mapping[ColumnName, TableHeader]


# You can use a ClassVar[t] annotation to explicitly declare that a particular attribute should not be set on instances:
#  https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations


# https://mypy.readthedocs.io/en/stable/literal_types.html#parameterizing-literals
