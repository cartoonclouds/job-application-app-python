from itertools import count, islice
from typing import Any, Callable, TypeVar, Iterable

T_co = TypeVar("T_co", covariant=True)
S_co = TypeVar("S_co", covariant=True)


def first(iterable: Iterable[T_co]) -> T_co | None:
    """Returns the first item"""
    return next(iter(iterable or []), None)


def first_where(
    iterable: Iterable[T_co],
    predicate: Callable[[T_co], bool],
    default: S_co | None = None,
) -> T_co | S_co | None:
    "Returns the first item which passes a condition or a default value"
    return next((n for n in iterable if predicate(n)), default)


def nth(
    iterable: Iterable[T_co], n: int, default: S_co | None = None
) -> T_co | S_co | None:
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def wrap_iter(obj: Any) -> Iterable[Any]:
    """If not an iterable, wraps the object in one"""
    try:
        iter(obj)
    except TypeError:
        return [obj]
    return obj

    # debug(
    #     isinstance(wrap_iter(None), Iterable),
    #     isinstance(wrap_iter(True), Iterable),
    #     isinstance(wrap_iter(False), Iterable),
    #     isinstance(wrap_iter("None"), Iterable),
    #     isinstance(wrap_iter(["1", "2", "3"]), Iterable),
    #     isinstance(wrap_iter({"1", "2", "3"}), Iterable),
    #     isinstance(wrap_iter({"1": "1", "2": "2", "3": "3"}), Iterable),
    #     isinstance(wrap_iter(("1", "2", "3")), Iterable),
    # )

    # debug(
    #     type(wrap_iter(None)),
    #     type(wrap_iter(True)),
    #     type(wrap_iter(False)),
    #     type(wrap_iter("None")),
    #     type(wrap_iter(["1", "2", "3"])),
    #     type(wrap_iter({"1", "2", "3"})),
    #     type(wrap_iter({"1": "1", "2": "2", "3": "3"})),
    #     type(wrap_iter(("1", "2", "3"))),
    # )
