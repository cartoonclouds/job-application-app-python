from typing import Type, TypeAlias, TypeVar
from app.gui.components.datatable.models.DatatableModel import DatatableModel

from app.models import Model as Models


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

T = TypeVar("T")  # Declare type variable. Use for generics

M = TypeVar("M", bound=Models.Model)
DTM = TypeVar("DTM", bound=DatatableModel)
M_co = TypeVar("M_co", bound=Models.Model, covariant=True)

# You can use a ClassVar[t] annotation to explicitly declare that a particular attribute should not be set on instances:
#  https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations


# https://mypy.readthedocs.io/en/stable/literal_types.html#parameterizing-literals
