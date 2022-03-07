from enum import Enum, unique
from typing import Sequence

# https://docs.python.org/3.11/howto/enum.html


class BaseEnum(str, Enum):
    def describe(self):
        return self.name, self.value

    @classmethod
    def atIndex(cls, type) -> int:
        return cls.ORDER().index(type)

    # TODO Generics?
    @staticmethod
    def ORDER() -> Sequence[str]:
        pass

    @staticmethod
    def AS_LIST() -> Sequence[str]:
        pass

    def __str__(self) -> str:
        return str(self.value)


@unique
class PayTypes(BaseEnum):
    SALARY = "salary"
    RATE = "rate"

    @staticmethod
    def ORDER() -> Sequence["PayTypes"]:
        return [PayTypes.SALARY, PayTypes.RATE]

    @staticmethod
    def AS_LIST() -> Sequence[str]:
        return [str(unit.value) for unit in PayTypes.ORDER()]


@unique
class PayUnits(BaseEnum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"

    @staticmethod
    def ORDER():
        return [PayUnits.MINUTE, PayUnits.HOUR, PayUnits.DAY]

    @staticmethod
    def AS_LIST() -> Sequence[str]:
        return [str(unit.value) for unit in PayUnits.ORDER()]


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

    @staticmethod
    def ORDER():
        return [
            EmploymentType.FULL_TIME,
            EmploymentType.PART_TIME,
            EmploymentType.CASUAL,
            EmploymentType.FIXED_TERM,
            EmploymentType.SHIFT_WORKER,
            EmploymentType.DAILY_WEEKLY_HIRE,
            EmploymentType.PROBATION,
            EmploymentType.APPRENTICE_TRAINEE,
            EmploymentType.OUTWORKER,
        ]

    @staticmethod
    def AS_LIST() -> Sequence[str]:
        return [str(unit.value) for unit in EmploymentType.ORDER()]
