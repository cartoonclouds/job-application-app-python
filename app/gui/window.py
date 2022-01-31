
# from PySide6.QtCore import *
from PySide6.QtGui import QResizeEvent, QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QLabel
import qtawesome as qta

from app.gui.components.tabs.JobApplicationTab import JobApplicationTab
from app.gui.components.tabs.SummaryTab import SummaryTab
from app.gui.components.tabs.Tabs import Tabs
from app.storage import Storage
from app.utilities.IconUtility import IconUtility

# https://realpython.com/python-menus-toolbars/
# https://github.com/pythonguis/15-minute-apps/blob/aaf6038ab4b687cf1370ae3c7ca71f46140c5cdb/browser_tabbed/browser_tabbed.py


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup window
        self.setWindowTitle('Main Window App GUI')
        self.resize(Storage.WINDOW_WIDTH, Storage.WINDOW_HEIGHT)

        fa5_icon = qta.icon('fa5.flag')
        self.setWindowIcon(fa5_icon)
        # self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

        # Setup menubar
        self.menubar = self.setupMenubar()

        # Setup statusbar
        self.statusbar = self.setupStatusbar()

        # Setup initial tabs
        self.tabs = self.setupTabs()
        self.setCentralWidget(self.tabs)

        # https://www.pythonguis.com/tutorials/pyside6-widgets/

        self.show()

    def resizeEvent(self, event: QResizeEvent) -> None:

        # self.tab1.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tab1.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        return super(MainWindow, self).resizeEvent(event)

    def setupTabs(self):
        tabs = Tabs()

        tabs.addNewTab(
            SummaryTab(
                "&Summary", tooltip="Summary tab with stats", closable=False, icon=IconUtility.getFileIcon("gear"))
        )
        tabs.addNewTab(JobApplicationTab(
            "Tab 2", icon=IconUtility.getFileIcon("blue-folder-32")))
        tabs.addNewTab(JobApplicationTab(
            "Tab 3", icon=IconUtility.getFileIcon("blue-folder-32")))

        # self.tab1.setTabText("123456")
        # self.tabs.setTabText(0, "Contact Details")
        return tabs

    def setupMenubar(self):
        menubar = self.menuBar()
        # Uncomment to disable native menubar on Mac
        # menubar().setNativeMenuBar(False)

        fileMenu = menubar.addMenu("&File")

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut(QKeySequence.Quit)
        exitAction.setToolTip('Exit this program')
        exitAction.setStatusTip('Exit this program')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # new_tab_action = QAction(
        #     QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        # new_tab_action.setStatusTip("Open a new tab")
        # new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        # file_menu.addAction(new_tab_action)
        return menubar

    def setupStatusbar(self):
        statusbar = self.statusBar()

        # Adding a temporary message
        statusbar.showMessage('A status bar update', 0)

        # Adding a permanent message
        self.wcLabel = QLabel(f"100 Words")
        statusbar.addPermanentWidget(self.wcLabel)

        return statusbar
