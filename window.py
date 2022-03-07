# Framework imports
import os
import sys
from PySide6.QtGui import QAction, QIcon, QKeySequence, QGuiApplication
from PySide6.QtWidgets import QLabel, QMainWindow, QTabWidget, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlDriver
import logging

# Third party imports
import qtawesome as qta

# Application imports
from app.gui.components.pages.JobApplicationTab import JobApplicationTab
from app.gui.components.pages.SummaryTab import SummaryTab
from app.gui.components.tabs.TabBar import TabBar
from app.gui.services.StatusBarService import StatusBarService
from app.gui.services.TabService import TabService
from app.models.JobApplication import JobApplication
from app.storage import Storage
from app.utils.IconUtility import IconUtility

# https://realpython.com/python-menus-toolbars/
# https://github.com/pythonguis/15-minute-apps/blob/aaf6038ab4b687cf1370ae3c7ca71f46140c5cdb/browser_tabbed/browser_tabbed.py


# https://stackoverflow.com/questions/61394268/difference-between-subclassing-qmainwindow-and-qapplication
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupLogging()

        # Setup window
        self.setWindowTitle("Main Window App GUI")
        self.resize(Storage.WINDOW_WIDTH, Storage.WINDOW_HEIGHT)

        fa5_icon: QIcon = qta.icon("fa5.flag")
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

        # TODO Utility function to create JAA/empty tab, given JAA ID/random
        testJaa = JobApplication.find(1)

        TabService.addTab(
            JobApplicationTab(
                f"{testJaa.title}, {testJaa.company.name} (ID {testJaa.id})",
                model=testJaa,
                icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
            )
        )

        # TabService.addTab(
        #     JobApplicationTab(
        #         f"New Application {TabService.tabCount() + 1}",
        #         icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
        #     )
        # )

        # https://www.pythonguis.com/tutorials/pyside6-widgets/

        self.show()

    # def resizeEvent(self, event: QResizeEvent) -> None:
    # return super(MainWindow, self).resizeEvent(event)

    def setupTabs(self):
        TabService.initTabs(TabBar())

        TabService.addTab(
            SummaryTab(
                "&Summary",
                tooltip="Summary tab with stats",
                closable=False,
                movable=False,
                icon=IconUtility.getFileIconAsPixmap("gear"),
            )
        )

    def setupMenubar(self):
        menubar = self.menuBar()
        # Uncomment to disable native menubar on Mac
        # menubar().setNativeMenuBar(False)

        fileMenu = menubar.addMenu("&File")

        exitAction = QAction("&Exit", self)
        exitAction.setShortcut(QKeySequence.Quit)
        exitAction.setToolTip("Exit this program")
        exitAction.setStatusTip("Exit this program")
        exitAction.triggered.connect(self.close)

        fileMenu.addAction(exitAction)

        # https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful
        #  GUI mixin to show alerts?

        # new_tab_action = QAction(
        #     QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        # new_tab_action.setStatusTip("Open a new tab")
        # new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        # file_menu.addAction(new_tab_action)
        return menubar

    def setupLogging(self):

        # kwargs.pop("datefmt", None)

        # https://docs.python.org/3/library/string.html#formatstrings

        # https://docs.python.org/3/howto/logging.html
        # https://docs.python.org/3/library/logging.html
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        # https://docs.python.org/3/howto/logging.html#useful-handlers
        # If debug to file => do on different thread
        # https://docs.python.org/3/howto/logging-cookbook.html#a-qt-gui-for-logging
        # Need to filter out Orator logging
        # https://www.programcreek.com/python/example/3364/logging.Filter
        # https://gist.github.com/acdha/9238791
        """
        Level    |   When it's used
        ===========================
        DEBUG    |   Detailed information, typically of interest only when diagnosing problems.
        INFO     |   Confirmation that things are working as expected.
        WARNING  |   An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
        ERROR    |   Due to a more serious problem, the software has not been able to perform some function.
        CRITICAL |   A serious error, indicating that the program itself may be unable to continue running.
        """
        logging.basicConfig(
            format="%(asctime)s %(levelname)-8s %(name)-12s.%(funcName)s:%(lineno)d %(message)s",
            handlers=[
                logging.FileHandler(filename="debug.log", encoding="utf-8", mode="a"),
                logging.StreamHandler(),
            ],
            datefmt="%d/%m/%Y %H:%M:%S%z",
            level=logging.DEBUG,
            force=True,
        )
