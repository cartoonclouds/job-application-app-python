from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtWidgets import QTabBar, QTabWidget, QHBoxLayout, QFrame, QLabel, QFrame
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, QPoint, Qt


class Statistic(QFrame):
    def __init__(self, text: str) -> None:
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
    
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        label = QLabel(text)
        label.setFont(QFont(["Helvetica", "SansSerif"], 18))
        # label.setAlignment(Qt.AlignCenter)


        layout.addWidget(label)
