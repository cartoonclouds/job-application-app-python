from enum import Enum, EnumMeta, unique
from typing import Any, Mapping, Sequence, Type, TypeVar


# class Enum(str)
class OrderedEnum(Enum):
    def __init__(self, value, *args, **kwds):
        super().__init__(*args, **kwds)
        self.__order = len(self.__class__)

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.__order >= other.__order
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.__order > other.__order
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.__order <= other.__order
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.__order < other.__order
        return NotImplemented


class NoDuplicateEnum(Enum):
    def __init__(self, *args: Any):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError(
                "aliases not allowed in DuplicateFreeEnum:  %r --> %r" % (a, e)
            )


# Enum union https://gist.github.com/plammens/ab1a2f236b5c6d748f193eb12eefa6dd

# https://docs.python.org/3.11/howto/enum.html
# https://docs.python.org/3/library/enum.html

# https://stackoverflow.com/questions/9048826/what-are-the-differences-amongst-pythons-get-and-del-methods
# https://www.reddit.com/r/programming/comments/1gy49/python_attributes_and_methods/
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

# Generic enums https://github.com/python/typing/issues/535


class EnumByIndexMeta(EnumMeta):
    def __getitem__(self, __i: int | slice) -> str:
        debug("at getitem")
        return super().__getitem__(__i)

    def __setitem__(self, key, value):
        debug("at setitem")
        super().__setitem__(key, value)

    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list?rq=1

    def __index__(self):
        return self.VALUES()[int(self)]

    def __int__(self):
        try:
            return self.VALUES().index(self)
        except:
            return -1


E = TypeVar("E", bound="BaseEnum")


@unique
class BaseEnum(str, Enum):
    def describe(self):
        return self.name, self.value

    @classmethod
    def index(cls: Type[E], type: E) -> int:  # type: ignore Thinks Enum type is str with this overloading str.index
        return cls.VALUES().index(type)

    @classmethod
    def MEMBERS(cls: Type[E]) -> Mapping[str, E]:
        return dict(cls.__members__.items())

    @classmethod
    def VALUES(cls: Type[E]) -> Sequence[E]:
        return [n.value for n in cls]

    @classmethod
    def NAMES(cls: Type[E]) -> Sequence[str]:
        return [n.name for n in cls]

    def __str__(self) -> str:
        return f"{self.name.lower()}({self.value})"


@unique
class PayTypes(BaseEnum):
    SALARY = "salary"
    RATE = "rate"


@unique
class PayUnits(BaseEnum, OrderedEnum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"


@unique
class EmploymentType(BaseEnum):
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    CASUAL = "Casual"
    FIXED_TERM = "Fixed Term"
    SHIFT_WORKER = "Shiftworker"
    DAILY_WEEKLY_HIRE = "Daily/Weekly Hire"
    PROBATION = "Probation"
    APPRENTICE_TRAINEE = "Apprentice/Trainee"
    OUTWORKER = "Outworker"


@unique
class ContactMethod(BaseEnum):
    PHONE_CALL = "Phone call"
    RECEIVED_PHONE_CALL = "Received phone call"
    EMAIL = "E-mail"
    RECRUITER = "Recruiter"
    IN_PERSON = "In-person"
    COMPANY_WEBSITE = "Company website"
    EMPLOYMENT_WEBSITE = "Employment website"
    LETTER = "Letter"
    ONLINE_FORUM = "Online forum"
