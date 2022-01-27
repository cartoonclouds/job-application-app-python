

from typing import Iterable, TypeVar


T = TypeVar("T")


class CollectionUtility:

    @staticmethod
    def keyBy(key: str, collection: Iterable[T]) -> list[tuple[str, T]]:
        """Keys a collection by a string value.

            Args:
                key (str): The string to key by
                collection (Iterable[T]): The collection to grab the keys from

            Returns:
                (list[tuple[str, T]]): A list of tuples with entries key, elemment
        """
        keys = collection.pluck(key)

        return zip(keys, collection)
