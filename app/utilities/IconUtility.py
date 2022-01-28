
from enum import Enum, unique, auto
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
    PIXMAP = auto()


class IconUtility:
    _icon_type = IconType.FILE
    _FILE_ICON_PATH = "app/assets/icons/"

    @staticmethod
    def setIconType(type: IconType):
        IconUtility._icon_type = type

    @staticmethod
    def getIcon(name: str) -> QIcon:
        match IconUtility._icon_type:
            case IconType.PIXMAP:
                return IconUtility.getSPIcon(name)

            case IconType.FILE:
                return IconUtility.getFileIcon(name)

            case IconType.DESKTOP:
                return IconUtility.getDesktopIcon(name)

            case _:
                raise Exception(f'Unknown icon type {IconUtility._icon_type}')

    @staticmethod
    def getFileIcon(name: str, filetype: str = 'png') -> QIcon:
        # Check if file exists -> exception
        iconPath = f'{IconUtility._FILE_ICON_PATH}{name}.{filetype}'

        # os.path.exists
        if not os.path.exists(iconPath):
            raise Exception(f'Icon not found at path {iconPath}')

        icon: QPixmap = QPixmap()

        if not icon.load(iconPath) or icon.isNull():
            raise Exception(f'Icon cannot be loaded from path {iconPath}')

        return icon
        return QIcon(icon)

    @staticmethod
    def getDesktopIcon(name: str) -> QIcon:
        return QIcon.fromTheme(name)

    @staticmethod
    def getSPIcon(name: str) -> QIcon:
        pixmap = getattr(QStyle.StandardPixmap, "SP_" + name)

        return QApplication.style().standardIcon(pixmap)
