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
from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QMetaObject

# Third party imports
import qtawesome as qta

# Application imports
from app.gui.components.pages.SummaryTab import SummaryTab
from app.gui.components.tabs.TabBar import TabBar
from app.gui.services.settings_service import SettingsServiceProvider
from app.gui.services.statusbar_service import StatusBarServiceProvider
from app.gui.services.tab_service import TabServiceProvider
from app.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from app.repositories.action_repository import ActionRepository
from app.repositories.job_application_repository import JobApplicationRepository
from app.repositories.profession_repository import ProfessionRepository
from app.utils.icon_utility import IconUtility
from app.utils.object_functions import format_object_name
from app.utils.ui_functions import UIFunctions


class UI_MainWindow:
    def __init__(self, window: QMainWindow):
        window.setObjectName(format_object_name(__class__.__name__))

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

        exitAction = UIFunctions.create_new_action(
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
