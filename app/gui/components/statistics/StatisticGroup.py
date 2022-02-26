from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtWidgets import (
    QTabBar,
    QTabWidget,
    QHBoxLayout,
    QWidget,
    QLabel,
    QFrame,
    QGridLayout,
)
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, QPoint, Qt

from app.gui.components.statistics.Statistic.Statistic import Statistic


class StatisticGroup(QFrame):
    def __init__(self) -> None:
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        stat1 = Statistic("Statistic section 1!")
        stat2 = Statistic("Statistic section 2!")
        stat3 = Statistic("Statistic section 3!")
        stat4 = Statistic("Statistic section 4!")
        stat5 = Statistic("Statistic section 5!")

        layout.addWidget(stat1)
        layout.addStretch(1)
        layout.addWidget(stat2)
        layout.addStretch(1)
        layout.addWidget(stat3)
        layout.addStretch(1)
        layout.addWidget(stat4)
        layout.addStretch(1)
        layout.addWidget(stat5)
