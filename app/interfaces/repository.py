from typing import Any, Generic, TypeAlias, TypeVar, Iterable
from app.models.Model import Model

T = TypeVar("T")
Id: TypeAlias = str
Ids = Iterable[Id]

ModelEntity = TypeVar("ModelEntity", bound=Model, covariant=True)

# Memoization https://python-course.eu/advanced-python/memoization-decorators.php


class IRepository(Generic[ModelEntity]):
    """
    Repository serves as a collection of entites (with methods such as get, add, update, remove)
    with underlying persistence layer. Should know how to construct an instance, serialize it
    and get its id.

    Developers of repos for concrete entites are encouraged to subclass and put a meaningful
    query and command methods along the basic ones.
    """

    def load_all(self) -> dict[str, ModelEntity]:
        """Loads all models from the database."""
        raise NotImplementedError

    def items(self) -> list[ModelEntity]:
        """Loads all models from the database."""
        raise NotImplementedError

    def keys(self) -> list[Id]:
        """Loads all models from the database."""
        raise NotImplementedError

    def find(self, id_: Id) -> ModelEntity | None:
        """Returns object of given id or None"""
        raise NotImplementedError

    def contains(self, id_: Id) -> bool:
        """Checks whether an entity of given id is in the repo."""
        raise NotImplementedError

    def create(self, **kwargs: Any) -> ModelEntity:
        """
        Creates an object compatible with this repo. Uses repo's factory
        or the klass iff factory not present.

        NB: Does not inserts the object to the repo. Use `create_and_add` method for that.
        """
        raise NotImplementedError

    def create_and_add(self, **kwargs: Any) -> ModelEntity:
        """Creates an object compatible with this repo and adds it to the collection."""
        raise NotImplementedError

    def add(self, entity: ModelEntity) -> Id:
        """Adds the object to the repo to the underlying persistence layer via its DAO."""
        raise NotImplementedError

    def update(self, entity: ModelEntity) -> None:
        """Updates the object in the repo."""
        raise NotImplementedError

    def remove(self, entity: ModelEntity) -> None:
        """Removes the object from the underlying persistence layer via DAO."""
        raise NotImplementedError
