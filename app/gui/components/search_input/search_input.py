from PySide6.QtWidgets import QLabel, QLineEdit
from PySide6.QtCore import QMargins, Qt, Signal, Slot

import qtawesome as qta


class SearchInput(QLineEdit):
    """
    URL: http://bazaar.launchpad.net/~henning-schroeder/%2Bjunk/qtwidgets/annotate/head:/qtwidgets/lineedit.py
    """

    updateSearch = Signal(str)

    def __init__(self):
        super(SearchInput, self).__init__()

        self.addAction(qta.icon("fa5s.search"), QLineEdit.LeadingPosition)
        self.setClearButtonEnabled(True)
        self.setPlaceholderText("Search...")

        self.textChanged.connect(lambda text: self.updateSearch.emit(text))
