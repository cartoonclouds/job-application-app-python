import sys
import os
import sys
import random
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from app.gui.components.JobApplicationTab import JobApplicationTab
from app.gui.components.SummaryTab import SummaryTab

# https://realpython.com/python-menus-toolbars/
# https://github.com/pythonguis/15-minute-apps/blob/aaf6038ab4b687cf1370ae3c7ca71f46140c5cdb/browser_tabbed/browser_tabbed.py


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Setup window
        self.setWindowTitle('Main Window App GUI')
        self.resize(1500, 800)
        # self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

        # Setup menubar
        self.setup_menubar()

        # Setup statusbar
        self.set_statusbar()

        # Setup initial tabs
        self.setup_tabs()

        # Instance variables
        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # self.button = QPushButton("Click me!")
        # self.text = QLabel(
        #     "Hello World", alignment=Qt.AlignCenter)

        # # self.layout = QVBoxLayout(self)
        # self.addWidget(self.text)
        # self.addWidget(self.button)

        # self.button.clicked.connect(self.magic)
        self.show()

    def resizeEvent(self, event):
        # self.tab1.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tab1.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        return super(MainWindow, self).resizeEvent(event)

    def setup_tabs(self):
        self.tabs = self.setup_tabs_layout()
        self.setCentralWidget(self.tabs)

        self.tab1 = SummaryTab(
            label="&Summary",
            tabs=self.tabs,
            tooltip="Summary tab with stats"
        )
        self.tab2 = JobApplicationTab("Tab 2", self.tabs)
        self.tab3 = JobApplicationTab("Tab 3", self.tabs)

        # self.tab1.setTabText("123456")
        # self.tabs.setTabText(0, "Contact Details")

    def setup_tabs_layout(self):
        tabs = QTabWidget()
        tabs.setTabsClosable(True)
        tabs.setDocumentMode(True)
        tabs.tabCloseRequested.connect(self.close_current_tab)
        tabs.setMovable(True)

        tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        return tabs

    def setup_menubar(self):
        self.menubar = self.menuBar()
        # Uncomment to disable native menubar on Mac
        # self.menubar().setNativeMenuBar(False)

        fileMenu = self.menubar.addMenu("&File")

        exitAction = QAction('&Exit', self)
        exitAction.setToolTip('Exit this program')
        exitAction.setStatusTip('Exit this program')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # new_tab_action = QAction(
        #     QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        # new_tab_action.setStatusTip("Open a new tab")
        # new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        # file_menu.addAction(new_tab_action)

    def set_statusbar(self):
        self.statusbar = self.statusBar()

        # Adding a temporary message
        self.statusbar.showMessage('A status bar update', 0)

        # Adding a permanent message
        self.wcLabel = QLabel(f"100 Words")
        self.statusbar.addPermanentWidget(self.wcLabel)

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def add_new_tab(self):
        pass

    def close_current_tab(self, tabIndex):
        if isinstance(self.tabs.widget(tabIndex), SummaryTab):
            return

        self.tabs.removeTab(tabIndex)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
