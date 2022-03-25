# ///////////////////////////////////////////////////////////////
#
# BY: CHRIS TUDHOPE
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they
# maintain the respective credits.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# Framework imports
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QMetaObject

# Third party imports
import qtawesome as qta

# Application imports
from app.gui.components.pages.SummaryTab import SummaryTab
from app.gui.components.tabs.TabBar import TabBar
from app.gui.services.SettingsService import SettingsServiceProvider
from app.gui.services.StatusBarService import StatusBarServiceProvider
from app.gui.services.TabService import TabServiceProvider
from app.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from app.repositories.ActionRepository import ActionRepository
from app.repositories.JobApplicationRepository import JobApplicationRepository
from app.utils.IconUtility import IconUtility
from app.utils.object_functions import formatObjectName
from app.utils.ui_functions import UIFunctions


class UI_MainWindow:
    def __init__(self, window: QMainWindow):
        window.setObjectName(formatObjectName(__class__.__name__))

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = SettingsServiceProvider()
        self.settings = settings.items

        # LOAD THEME
        # ///////////////////////////////////////////////////////////////
        # TODO

        # SETUP WINDOW PROPERTIES
        # ///////////////////////////////////////////////////////////////
        window.setWindowTitle("Job Application Tracker [*]")
        window.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        fa5_icon: QIcon = qta.icon("fa5.flag")
        window.setWindowIcon(fa5_icon)
        # self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))
        # TODO on window close check if any tab modified, ask to save

        # SETUP STATUSBAR
        # ///////////////////////////////////////////////////////////////
        StatusBarServiceProvider.init(window)

        JobApplicationRepository.load_all()
        ActionRepository.load_all()

        # ADD CENTRAL WIDGET
        # ///////////////////////////////////////////////////////////////
        self.__setupTabs()

        window.setCentralWidget(TabServiceProvider.tabs)

    def __setupTabs(self):
        TabServiceProvider.init(TabBar())

        TabServiceProvider.addTab(
            SummaryTab(
                "&Summary",
                tooltip="Summary tab with stats",
                closable=False,
                movable=False,
                icon=IconUtility.getFileIconAsPixmap("gear"),
            )
        )

        return TabServiceProvider

    def setupMenubar(self, window: QMainWindow):
        menubar = window.menuBar()
        # Uncomment to disable native menubar on Mac
        # menubar().setNativeMenuBar(False)

        exitAction = UIFunctions.createNewAction(
            "&Exit",
            "Exit this program",
            "Exit this program",
            QKeySequence.Quit,
            window.close,
            menubar,
        )

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        # https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful
        #  GUI mixin to show alerts?

        # new_tab_action = QAction(
        #     QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        # new_tab_action.setStatusTip("Open a new tab")
        # new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        # file_menu.addAction(new_tab_action)
        return menubar
