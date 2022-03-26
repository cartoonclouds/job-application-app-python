from typing import Protocol
from PySide6.QtWidgets import QCompleter


class Placeholderable(Protocol):
    def setPlaceholderText(self, text: str) -> None:
        ...


class InputMaskable(Protocol):
    def setInputMask(self, mask: str) -> None:
        ...


class Completableable(Protocol):
    def setCompleter(self, completer: QCompleter) -> None:
        ...
