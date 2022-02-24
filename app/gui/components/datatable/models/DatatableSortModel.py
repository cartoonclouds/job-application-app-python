
from PySide6.QtCore import QObject, QSortFilterProxyModel


class CustomSortModel(QSortFilterProxyModel):
    def __init__(self, parent: QObject | None = None) -> None:
        """
        Custom QSortFilterProxyModel to allow sorting and filtering of our custom data model.
        :param parent: parent so that this model is deleted properly upon close.
        """
        super().__init__(parent)

        self.countAllColumns = False
        self._sortingColumn = 0

    def filterAcceptsRow(self, sourceRow, sourceParent):
        """
        Overriding how we choose what rows match our input filter text.

        :param sourceRow: row index in question
        :param sourceParent: QModelIndex
        :return: bool (accepted or not)
        """
        txt = ''

        if self.countAllColumns:
            for x in range(len(self.sourceModel().headers)):
                txt += self.sourceModel().intGetData(sourceRow, x).toString()

        else:
            txt = self.sourceModel().intGetData(sourceRow, self._sortingColumn).toString()

        if self.filterRegExp().pattern():
            b = bool(re.search(str(self.filterRegExp().pattern()), str(txt)))
        else:
            b = bool(re.search('.*', str(txt)))

        return b

    def setFilterKeyColumn(self, col):
        """
        Sets which column index you want the filter to apply to. -1 or less means we search all columns - otherwise,
        the filter rules apply to the column index given.
        :param col: signed int
        :return:
        """
        if col <= -1:
            self.countAllColumns = True
            return

        self.countAllColumns = False
        self._sortingColumn = col
        super(CustomSortModel, self).setFilterKeyColumn(col)
