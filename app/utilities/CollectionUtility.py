

from typing import TypeVar
import typing


T = TypeVar('T')  # Any type.
KT = TypeVar('KT')  # Key type.
VT = TypeVar('VT')  # Value type.
Collection = typing.Sequence[typing.Mapping[str, T]]


class CollectionUtility:

    @staticmethod
    # -> typing.Mapping[str, Collection[T]]:
    def keyBy(key: str, collection: Collection[T]): # -> typing.Mapping[str, Collection[T]]:
        """Keys a collection by a string value.

            Args:
                key (str): The string to key by
                collection (Iterable[T]): The collection to grab the keys from

            Returns:
                (list[tuple[str, T]]): A list of tuples with entries key, elemment
        """
        keys: typing.Sequence[str] = collection.pluck(key)
        # keys = CollectionUtility.pluck(key, collection)

        return zip(keys, collection)

    @staticmethod
    def pluck(key: str, collection: Collection[T]):
        r = [x[key] for x in collection]
        return r
