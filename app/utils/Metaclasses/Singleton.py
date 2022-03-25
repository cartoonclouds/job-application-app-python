# Metaclass typing
# https://stackoverflow.com/questions/66339371/generic-class-variable-in-python-with-metaclass-and-concrete-base-class
from typing import Any

class Singleton(type):
    """A metaclass to transform the attached instance into a singleton

    URL: https://stackoverflow.com/a/33201
         https://stackoverflow.com/a/9887928
    """

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args: Any, **kwargs: Any):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance

    # Intercept class creation to prevent duplicating the singleton instance via copy/deepcopy
    def __new__(cls, name, bases, dict):
        dict["__deepcopy__"] = dict["__copy__"] = lambda self, *args: self
        return (
            getattr(cls, "instance")
            if hasattr(cls, "instance")
            else super(Singleton, cls).__new__(cls, name, bases, dict)
        )
