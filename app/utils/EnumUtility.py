from enum import Enum, unique
from typing import Sequence
from typing_extensions import Self

# https://docs.python.org/3.11/howto/enum.html


class BaseEnum(str, Enum):
    def describe(self):
        return self.name, self.value

    @classmethod
    def atIndex(cls, type) -> int:
        return cls.ORDER().index(type)

    # TODO Generics?
    @classmethod
    def ORDER(cls) -> Sequence[Self]:
        pass

    @classmethod
    def AS_LIST(cls) -> Sequence[str]:
        pass

    def __str__(self) -> str:
        return str(self.value)


@unique
class PayTypes(BaseEnum):
    SALARY = "salary"
    RATE = "rate"

    @classmethod
    def ORDER(cls) -> Sequence[Self]:
        return [cls.SALARY, cls.RATE]

    @classmethod
    def AS_LIST(cls) -> Sequence[str]:
        return [str(unit.value) for unit in cls.ORDER()]


@unique
class PayUnits(BaseEnum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"

    @classmethod
    def ORDER(cls) -> Sequence[Self]:
        return [cls.MINUTE, cls.HOUR, cls.DAY]

    @classmethod
    def AS_LIST(cls) -> Sequence[str]:
        return [str(unit.value) for unit in cls.ORDER()]


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

    @classmethod
    def ORDER(cls) -> Sequence[Self]:
        return [
            cls.FULL_TIME,
            cls.PART_TIME,
            cls.CASUAL,
            cls.FIXED_TERM,
            cls.SHIFT_WORKER,
            cls.DAILY_WEEKLY_HIRE,
            cls.PROBATION,
            cls.APPRENTICE_TRAINEE,
            cls.OUTWORKER,
        ]

    @classmethod
    def AS_LIST(cls) -> Sequence[str]:
        return [str(unit.value) for unit in cls.ORDER()]


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

    @classmethod
    def ORDER(cls) -> Sequence[Self]:
        return [
            cls.PHONE_CALL,
            cls.RECEIVED_PHONE_CALL,
            cls.EMAIL,
            cls.RECRUITER,
            cls.IN_PERSON,
            cls.COMPANY_WEBSITE,
            cls.EMPLOYMENT_WEBSITE,
            cls.LETTER,
            cls.ONLINE_FORUM,
        ]

    @classmethod
    def AS_LIST(cls) -> Sequence[str]:
        return [str(unit.value) for unit in cls.ORDER()]
