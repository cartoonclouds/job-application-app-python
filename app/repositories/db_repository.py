# Standard Library
from abc import ABC, ABCMeta, abstractmethod
from typing import Any, Generic, TypeVar, ClassVar, Type, Sequence, cast

# Third party imports
import pendulum

# Application imports
from app.interfaces.repository import IRepository, Id, ModelEntity
from app.utils.Metaclasses.Singleton import Singleton

# ChainMap(class) Self


# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


# https://github.com/sdispater/backpack


class GenericABCMeta(ABCMeta):
    pass


class DBRepository(IRepository[ModelEntity], metaclass=Singleton):
    """
    Repository serves as a collection of entites (get, add, update, remove) with underlying
    persistence layer. Via its factory class, it knows how to construct an instance of the entity,
    serialize it and get its id.
    Developers of repos for concrete entites are encouraged to subclass and put a meaningful
    query and command methods along the basic ones.
    """

    def __init__(self, factory: Type[ModelEntity]):
        self.factory = factory
        self.container: dict[str, ModelEntity] = {}

    def load_all(self) -> dict[str, ModelEntity]:
        """
        Loads all models from the database.

        NB: This will clear any existing models
        """
        entities = self.factory.all()

        if len(entities) > 0:
            keys: Sequence[str] = entities.model_keys()  # type: ignore

            self.container = dict(zip(keys, entities))

        return self.container

    def items(self) -> list[ModelEntity]:
        return list(self.container.values())

    def keys(self) -> list[Id]:
        """Loads all models from the database."""
        return list(self.container.keys())

    def find(self, id_: Id) -> ModelEntity | None:
        """Returns object of given id or None"""
        return self.container.get(id_)

    def contains(self, id_: Id) -> bool:
        """Checks whether an entity of given id is in the repo."""
        return id_ in self.container

    def create(self, **kwargs: Any) -> ModelEntity:
        """
        Creates an object compatible with this repo. Uses repo's factory.

        NB: Does not inserts the object to the repo. Use `create_and_add` method for that.
        """
        entity = self.factory(**kwargs)

        entity.save()
        entity.push()

        return entity

    def create_and_add(self, **kwargs: Any) -> ModelEntity:
        """Creates an object compatible with this repo and adds it to the collection."""
        entity = self.create(**kwargs)

        self.add(entity)

        return entity

    def add(self, entity: ModelEntity) -> Id:
        """Adds the object to the repo to the underlying persistence layer via its DAO."""
        entityId = entity.get_key()

        self.container[entityId] = entity

        return entityId

    def update(self, entity: ModelEntity) -> None:
        """Updates the object in the repo."""
        self.container[entity.get_key()] = entity

    def remove(self, entity: ModelEntity) -> None:
        """Removes the object from the underlying persistence layer via DAO."""
        self.container.pop(entity.get_key())
