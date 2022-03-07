class CallByStringMixin:
    def callfunc(self, func: str, *args) -> Any:
        """Allows to a class function by passing the name of the function as a string.

        Args:
            func (str): Name of a function
            args: Function arguments

        Returns:
            Any: _description_
        """
        if isinstance(func, str) and callable(getattr(self, func)):
            if len(args):
                return getattr(self, func)(*args)
            return getattr(self, func)()
