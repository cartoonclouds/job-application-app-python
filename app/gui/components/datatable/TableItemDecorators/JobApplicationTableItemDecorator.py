
from PySide6.QtWidgets import QTableWidgetItem


class JobApplicationTableItemDecorator(QTableWidgetItem):
    def __init__(self, type: int) -> None:
        super().__init__(type)
