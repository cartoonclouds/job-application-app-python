from typing import Any, Generic, Mapping, Sequence, TypeAlias, TypeVar, Iterable, Type

# from app.Ts.T import T

T = TypeVar("T")
Id: TypeAlias = str
Ids = Iterable[Id]


# Memoization https://python-course.eu/advanced-python/memoization-decorators.php


class IRepository(Generic[T]):
    """
    Repository serves as a collection of entites (with methods such as get, add, update, remove)
    with underlying persistence layer. Should know how to construct an instance, serialize it
    and get its id.

    Developers of repos for concrete entites are encouraged to subclass and put a meaningful
    query and command methods along the basic ones.
    """

    def load_all(self) -> Mapping[str, T]:
        """
        Loads all Ts from the database.

        NB: This will clear any existing Ts
        """
        raise NotImplementedError

    def items(self) -> Sequence[T]:
        """Loads all Ts from the database."""
        raise NotImplementedError

    def keys(self) -> Sequence[Id]:
        """Loads all Ts from the database."""
        raise NotImplementedError

    def find(self, id_: Id) -> T | None:
        """Returns object of given id or None"""
        raise NotImplementedError

    def contains(self, id_: Id) -> bool:
        """Checks whether an entity of given id is in the repo."""
        raise NotImplementedError

    def count(self) -> int:
        """Returns a count of all loaded objects in the repo."""
        raise NotImplementedError

    def create(self, **kwargs: Any) -> T:
        """
        Creates an object compatible with this repo. Uses repo's factory
        or the klass iff factory not present.

        NB: Does not inserts the object to the repo. Use `create_and_add` method for that.
        """
        raise NotImplementedError

    def create_and_add(self, **kwargs: Any) -> T:
        """Creates an object compatible with this repo and adds it to the collection."""
        raise NotImplementedError

    def add(self, entity: T) -> Id:
        """Adds the object to the repo to the underlying persistence layer via its DAO."""
        raise NotImplementedError

    def update(self, entity: T) -> None:
        """Updates the object in the repo."""
        raise NotImplementedError

    def remove(self, entity: T) -> None:
        """Removes the object from the underlying persistence layer via DAO."""
        raise NotImplementedError
