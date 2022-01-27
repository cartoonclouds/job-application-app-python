
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from app.gui.components.tabs.Tab import Tab

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self,
                 label: str,
                 tooltip: str = None,
                 whatsThis: str = None,
                 icon: QIcon = None, 
                 closable: bool = True
                 ):

        super(JobApplicationTab, self).__init__()

        self.label = label
        self.tooltip = tooltip
        self.tab_whatsThis = whatsThis
        self.icon = icon
        self.closable = closable

        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())

        self.setLayout(layout)
