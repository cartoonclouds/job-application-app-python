import enum
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QDataWidgetMapper
from app.typings.types import M, Models
from typing import Callable, TypeAlias

RowIndex: TypeAlias = int
ColumnIndex: TypeAlias = int

# TODO Additional property to pass to addMapping
def generateDataWidgetMapper(
    models: list[M],
    fields: list[str | Callable[[M, RowIndex, ColumnIndex], str]],
    widgets: list[QWidget],
):
    itemModel = QStandardItemModel(len(models), len(fields))
    dataMapper = QDataWidgetMapper()
    dataMapper.setModel(itemModel)

    for row, model in enumerate(models):
        for column, field in enumerate(fields):

            if callable(field):
                text = field(model, row, column)
            else:
                text = getattr(model, field)

            item = QStandardItem(text)
            itemModel.setItem(row, column, item)

    for column, widget in enumerate(widgets):
        dataMapper.addMapping(widget, column)

    return itemModel, dataMapper
