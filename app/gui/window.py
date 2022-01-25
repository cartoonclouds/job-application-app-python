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
        self.resize(800, 600)
        # self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

        # Setup menubar
        self.setupMenuBar()

        # Setup statusbar
        self.setupStatusBar()

        # Setup initial tabs
        self.tabs = self.setupTabs()
        self.setCentralWidget(self.tabs)

        self.tab1 = SummaryTab(
            tabs=self.tabs,
            label="&Summary",
            tooltip="Summary tab with stats"
        )
        self.tab2 = JobApplicationTab(self.tabs, "Tab 2")
        self.tab3 = JobApplicationTab(self.tabs, "Tab 3")

        # self.tab1.setTabText("123456")
        # self.tabs.setTabText(0, "Contact Details")

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

    def setupMenuBar(self):
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

    def setupStatusBar(self):
        self.statusbar = self.statusBar()

        # Adding a temporary message
        self.statusbar.showMessage('A status bar update', 0)

        # Adding a permanent message
        self.wcLabel = QLabel(f"100 Words")
        self.statusbar.addPermanentWidget(self.wcLabel)

    def setupTabs(self):
        tabs = QTabWidget()
        tabs.setTabsClosable(True)
        tabs.setDocumentMode(True)
        tabs.tabCloseRequested.connect(self.closeCurrentTab)
        tabs.setMovable(True)

        tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        return tabs

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def add_new_tab(self):
        pass

    def closeCurrentTab(self, tabIndex):
        if isinstance(self.tabs.widget(tabIndex), SummaryTab):
            return

        self.tabs.removeTab(tabIndex)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
