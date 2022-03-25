from typing import Iterable, TypeVar, Mapping, Type


T = TypeVar("T")  # Any type.
KT = TypeVar("KT")  # Key type.
VT = TypeVar("VT")  # Value type.


class CollectionUtility:
    @staticmethod
    def keyBy(key: str, collection: Iterable[Type[T]]) -> Mapping[str, T]:
        """Keys a collection by a string value.

        Args:
            key (str): The string to key by
            collection (Iterable[T]): The collection to grab the keys from

        Returns:
            (list[tuple[str, T]]): A list of tuples with entries key, elemment
        """
        keys = map(lambda m: getattr(m, key), collection)

        return dict(zip(keys, collection))
