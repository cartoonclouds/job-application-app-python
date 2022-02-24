
# from PySide6.QtCore import *

import qtawesome as qta
from app.gui.components.tabs.TabBar import TabBar
from app.gui.services.StatusBarService import StatusBarService
from app.gui.services.TabService import TabService
from app.gui.components.pages.JobApplicationTab import JobApplicationTab
from app.gui.components.pages.SummaryTab import SummaryTab
from app.storage import Storage
from app.utilities.IconUtility import IconUtility
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QLabel, QMainWindow, QTabWidget

# https://realpython.com/python-menus-toolbars/
# https://github.com/pythonguis/15-minute-apps/blob/aaf6038ab4b687cf1370ae3c7ca71f46140c5cdb/browser_tabbed/browser_tabbed.py


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup window
        self.setWindowTitle('Main Window App GUI')
        self.resize(Storage.WINDOW_WIDTH, Storage.WINDOW_HEIGHT)

        fa5_icon: QIcon = qta.icon('fa5.flag')
        self.setWindowIcon(fa5_icon)
        # self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

        # Setup menubar
        self.menubar = self.setupMenubar()

        # Setup statusbar
        StatusBarService.init(self)

        # Setup initial tabs
        self.setupTabs()
        self.setCentralWidget(TabService.tabs)
        self.setContentsMargins(1, 1, 1, 1)

        # https://www.pythonguis.com/tutorials/pyside6-widgets/

        self.show()

    # def resizeEvent(self, event: QResizeEvent) -> None:
        # return super(MainWindow, self).resizeEvent(event)

    def setupTabs(self):
        TabService.initTabs(TabBar())

        TabService.openTab(
            SummaryTab(
                "&Summary", tooltip="Summary tab with stats", closable=False, movable=False, icon=IconUtility.getFileIcon("gear"))
        )

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
