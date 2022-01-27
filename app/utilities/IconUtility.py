
from PySide6 import os
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QStyle
from dataclasses import dataclass
from pathlib import Path

# StandardPixmap icons http://srinikom.github.io/pyside-docs/PySide/QtGui/QStyle.html#PySide.QtGui.PySide.QtGui.QStyle.StandardPixmap
# Desktop icons https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
# https://www.pythonguis.com/faq/built-in-qicons-pyqt/


@dataclass
class ICON_TYPE:
    FILE = 0
    DESKTOP = 1
    PIXMAP = 2


class IconUtility:
    _icon_type = ICON_TYPE.FILE
    _FILE_ICON_PATH = "app/assets/icons/"

    @staticmethod
    def set_icon_type(type: ICON_TYPE):
        IconUtility._icon_type = type

    @staticmethod
    def get_icon(name: str) -> QIcon:
        # https://github.com/gvanrossum/patma/blob/master/README.md#tutorial
        match IconUtility._icon_type:
            case ICON_TYPE.PIXMAP:
                return IconUtility.get_sp_icon(name)

            case ICON_TYPE.FILE:
                return IconUtility.get_file_icon(name)

            case ICON_TYPE.DESKTOP:
                return IconUtility.get_desktop_icon(name)

            case _:
                raise Exception('Unknown icon type ' + IconUtility._icon_type)

    @staticmethod
    def get_file_icon(name: str, filetype: str = 'png') -> QIcon:
        # Check if file exists -> exception
        iconPath = f'{IconUtility._FILE_ICON_PATH}{name}.{filetype}'

        # os.path.exists
        if not os.path.exists(iconPath):
            raise Exception(f'Icon not found at path {iconPath}')

        icon: QPixmap = QPixmap()

        if not icon.load(iconPath) or icon.isNull():
            raise Exception(f'Icon cannot be loaded from path {iconPath}')

        return QIcon(icon)

    @staticmethod
    def get_desktop_icon(name: str) -> QIcon:
        return QIcon.fromTheme(name)

    @staticmethod
    def get_sp_icon(name: str) -> QIcon:
        pixmap = getattr(QStyle.StandardPixmap, "SP_" + name)

        return QApplication.style().standardIcon(pixmap)
