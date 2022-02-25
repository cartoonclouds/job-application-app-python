
from enum import Enum, unique, auto
from typing import Any, overload
from PySide6 import os
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QStyle

# StandardPixmap icons http://srinikom.github.io/pyside-docs/PySide/QtGui/QStyle.html#PySide.QtGui.PySide.QtGui.QStyle.StandardPixmap
# Desktop icons https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
# https://www.pythonguis.com/faq/built-in-qicons-pyqt/


# https://github.com/gvanrossum/patma/blob/master/README.md#tutorial

@unique
class IconType(Enum):
    FILE = auto()
    DESKTOP = auto()
    STANDARD = auto()


@unique
class IconFormat(Enum):
    QIcon = auto()
    QPixmap = auto()


class IconUtility:
    _FILE_ICON_PATH = "app/assets/icons/"

    @staticmethod
    def getFileIconAsIcon(name: str) -> QIcon:
        return IconUtility.getFileIcon(name, IconFormat.QIcon)

    @staticmethod
    def getFileIconAsPixmap(name: str) -> QPixmap:
        return IconUtility.getFileIcon(name, IconFormat.QPixmap)

    @staticmethod
    def getFileIcon(name: str, format: IconFormat) -> Any:
        # Check if file exists -> exception
        filetype = 'png'
        iconPath = f'{IconUtility._FILE_ICON_PATH}{name.strip()}.{filetype}'

        # os.path.exists
        if not os.path.exists(iconPath):
            raise Exception(f'Icon not found at path {iconPath}')

        icon: QPixmap = QPixmap()

        if not icon.load(iconPath) or icon.isNull():
            raise Exception(f'Icon cannot be loaded from path {iconPath}')

        qicon = QIcon(icon)

        if format is IconFormat.QIcon:
            return qicon
        elif format is IconFormat.QPixmap:
            return icon

    @staticmethod
    def getDesktopIcon(name: str, format: IconFormat = IconFormat.QIcon) -> QIcon:
        qicon = QIcon.fromTheme(name.strip())

        # if format is IconFormat.QIcon:
        return qicon
        # elif format is IconFormat.QPixmap:
        #     return qicon.pixmap(qicon.width(), qicon.height())

    @ staticmethod
    def getStandardIcon(name: str, format: IconFormat = IconFormat.QPixmap) -> QIcon | QPixmap:
        iconName = getattr(QStyle.StandardPixmap, "SP_" + name.strip())

        if format is IconFormat.QIcon:
            return QApplication.style().standardIcon(iconName)
        elif format is IconFormat.QPixmap:
            return QApplication.style().standardPixmap(iconName)
