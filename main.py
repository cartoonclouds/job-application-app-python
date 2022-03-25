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

# Standard Library
import sys
import logging

# Framework imports
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import ClassInfo
from PySide6.QtGui import QFontDatabase, QFont


# Application imports
from app.ui_main import UI_MainWindow
from app.utils.IconUtility import IconUtility

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
# @ClassInfo(Author="CHRIS TUDHOPE", URL="http://www.website.com")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP LOGGING
        # ///////////////////////////////////////////////////////////////
        self.__setupLogging()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow(self)

        # Setup menubar
        self.ui.setupMenubar(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        # settings = Settings()
        # self.settings = settings.items

        # TESTING - AUTO-OPEN JAA
        self.openTestTab()

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    def openTestTab(self):
        from app.gui.components.pages.JobApplicationTab import JobApplicationTab
        from app.gui.services.TabService import TabServiceProvider
        from app.models.JobApplication import JobApplication
        from app.repositories.JobApplicationRepository import JobApplicationRepository

        # TODO Utility function to create JAA/empty tab, given JAA ID/random
        jobApplicationRepo = JobApplicationRepository()

        testJaa = jobApplicationRepo.getAtIndex(1)
        assert isinstance(testJaa, JobApplication)
        testJaaTab = JobApplicationTab(
            f"{testJaa.title}, {testJaa.company.name} (ID {testJaa.id})",
            testJaa,
            icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
        )
        TabServiceProvider.openTab(testJaaTab)

    def __setupLogging(self):
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


# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)

    # app.setApplicationName
    # app.setApplicationVersion
    # app.setOrganizationDomain
    # app.setOrganizationName
    window = MainWindow()

    # QFontDatabase.addApplicationFont("fonts/segoeui.ttf")
    # QFontDatabase.addApplicationFont("fonts/segoeuib.ttf")

    # font = QFont()
    # font.setFamily(u"Segoe UI")
    # window.setFont(font)

    # EXEC APP
    # ///////////////////////////////////////////////////////////////

    # metaObject = app.metaObject()
    # properties = [
    #     metaObject.property(i).name()
    #     for i in range(metaObject.propertyOffset(), metaObject.propertyCount())
    # ]
    # methods = [
    #     metaObject.method(i).signature()
    #     for i in range(metaObject.methodOffset(), metaObject.methodCount())
    # ]
    # debug(properties, methods)

    sys.exit(app.exec())


# app.setStyle("Plastique")
# https://stackoverflow.com/questions/63442415/changing-font-size-of-all-qlabel-objects-pyqt5

# https://www.pythonguis.com/tutorials/pyside6-widgets/
# https://stackoverflow.com/questions/61394268/difference-between-subclassing-qmainwindow-and-qapplication
# custom_font = QFont()
# custom_font.setWeight(18);
# QApplication.setFont(custom_font, "QLabel")

# QApplication.setStyle(QStyleFactory.create("QPlastiqueStyle"))
# QApplication.setStyle(QStyleFactory.create("Cleanlooks"))

# QScreen to get Window information

# https://webgradients.com/

# https://docs.python.org/3/library/configparser.html


# https://realpython.com/python-menus-toolbars/
# https://github.com/pythonguis/15-minute-apps/blob/aaf6038ab4b687cf1370ae3c7ca71f46140c5cdb/browser_tabbed/browser_tabbed.py


# Initalize db + migrations
# https://github.com/sdispater/orator/pull/200

# Validate model on save
# https://github.com/sdispater/orator/pull/371
# https://orator-orm.com/docs/0.9/orm.html#model-events

# debug global access
# https://stackoverflow.com/questions/6965090/how-to-add-builtin-functions
# https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/site/index.html
# https://www.python.org/dev/peps/pep-0648/
#

# Pydantic - validation / Using Types at Runtime
# https://pypi.org/project/pydantic/
# https://medium.com/swlh/cool-things-you-can-do-with-pydantic-fc1c948fbde0
# https://pydantic-docs.helpmanual.io/

# Pylint - checks for errors, coding standard and looks for code smells.
# https://pylint.pycqa.org/en/latest/index.html

# Pyright - static type checker
# https://github.com/microsoft/pyright
# https://github.com/microsoft/pyright/blob/main/docs/configuration.md
# https://devblogs.microsoft.com/python/announcing-pylance-fast-feature-rich-language-support-for-python-in-visual-studio-code/
# https://code.visualstudio.com/docs/python/settings-reference

# Pylance - VSCode extensions for Pyright (plus more features)

# MyPi - static type checker
# http://mypy-lang.org/

# Pydocstyle
# http://www.pydocstyle.org/en/

# PyAutoGUI - allows for control of the mouse and keyboar
# https://pyautogui.readthedocs.io/en/latest/

# Requirements(.txt) / constraints.txt
# https://pip.pypa.io/en/stable/reference/build-system/
# https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
# https://caremad.io/posts/2013/07/setup-vs-requirement/
# https://pip.pypa.io/en/stable/topics/configuration/
# https://pip.pypa.io/en/stable/user_guide/#requirements-files
# https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format
# https://realpython.com/lessons/using-requirement-files/

# https://pypi.org/project/parse/


# INTERFACE
# import abc
# class MixinDependencyInterface(abc.ABC):
#     @abc.abstractmethod
#     def foo(self):
#         pass
