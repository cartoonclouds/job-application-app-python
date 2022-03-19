from typing import Any


class ListMixin:
    @staticmethod
    def isstr(o: Any):
        try:
            basestring
        except NameError:
            basestring = (str, bytes)
        return isinstance(o, basestring)

    @staticmethod
    def wrapIter(o: Any):
        if not ListMixin.isstr(o):
            try:
                return iter(o)
            except TypeError:
                pass
        return iter([o])

    @staticmethod
    def wrap(o: Any):
        if not ListMixin.isstr(o):
            try:
                return list(o)
            except TypeError:
                pass
        return [o]
