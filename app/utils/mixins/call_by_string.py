from typing import Any


class CallByStringMixin:
    def call_func(self, func: str, *args: Any, **kwargs: Any) -> Any:
        """Allows to a class function by passing the name of the function as a string.

        Args:
            func (str): Name of a function
            args: Function arguments

        Returns:
            Any: _description_
        """
        # callable(getattr(self, func)) ??
        if callable(eval(func)):
            if len(args):
                return getattr(self, func)(*args, **kwargs)
            return getattr(self, func)()
