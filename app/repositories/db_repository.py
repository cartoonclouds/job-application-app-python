# Standard Library
from abc import ABC, ABCMeta, abstractmethod
from collections import defaultdict
from typing import (
    Any,
    Generic,
    MutableMapping,
    MutableSequence,
    TypeAlias,
    TypeVar,
    ClassVar,
    Type,
    Sequence,
    cast,
)

# Application imports
from app.interfaces.repository import T, IRepository, Id
from app.models.Model import Model
from app.typings.types import M

# from app.Ms.M import M
from app.utils.Metaclasses.Singleton import Singleton

# ChainMap(class) Self


# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


# https://github.com/sdispater/backpack


class DBRepository(IRepository[M], metaclass=Singleton):
    """
    Repository serves as a collection of entites (get, add, update, remove) with underlying
    persistence layer. Via its factory class, it knows how to construct an instance of the entity,
    serialize it and get its id.
    Developers of repos for concrete entites are encouraged to subclass and put a meaningful
    query and command methods along the basic ones.
    """

    def __init__(self, factory: Type[M]):
        self.factory = factory
        self.container: dict[str, M] = {}

    def load_all(self) -> dict[str, M]:
        entities = self.factory.allKeyedBy("id")

        if len(entities) > 0:
            self.container = entities

        return self.container

    def count(self) -> int:
        return len(self.container)

    def items(self) -> list[M]:
        if self.count() == 0:
            self.load_all()

        return list(self.container.values())

    def keys(self) -> list[Id]:
        if self.count() == 0:
            self.load_all()

        return list(self.container.keys())

    def find(self, id_: Id) -> M | None:
        return self.container.get(id_)

    def contains(self, id_: Id) -> bool:
        return id_ in self.container

    def create(self, **kwargs: Any) -> M:
        entity = self.factory(**kwargs)

        entity.save()
        entity.push()

        return entity

    def create_and_add(self, **kwargs: Any) -> M:
        entity = self.create(**kwargs)

        self.add(entity)

        return entity

    def add(self, entity: Model) -> Id:
        entityId = entity.get_key()

        self.container |= [(entityId, entity)]

        return entityId

    def update(self, entity: Model) -> None:
        self.container[entity.get_key()] = entity

    def remove(self, entity: Model) -> None:
        self.container.pop(entity.get_key())
