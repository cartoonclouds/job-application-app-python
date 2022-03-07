#!/usr/bin/env python
from typing import overload
import typing
from PySide6 import QtCore, QtGui, QtWidgets


class KeyPressHandler(QtCore.QObject):
    """Custom key press handler"""

    escapePressed = QtCore.Signal(bool)
    returnPressed = QtCore.Signal(bool)
    textChanged = QtCore.Signal(bool)

    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent):
        if event.type() == QtCore.QEvent.KeyPress:
            event_key = event.key()
            if event_key == QtCore.Qt.Key_Escape:
                self.escapePressed.emit(True)
                return True
            if event_key == QtCore.Qt.Key_Return or event_key == QtCore.Qt.Key_Enter:
                self.returnPressed.emit(True)
                return True
            # TODO Only on ASCINUM
            self.textChanged.emit(True)

        return QtCore.QObject.eventFilter(self, obj, event)


class EditableLabel(QtWidgets.QWidget):
    """Editable label"""

    textChanged = QtCore.Signal(str)

    # TODO tidy up
    # TODO Add dotted line beneath to signify editable

    def __init__(self, text: str, parent: QtWidgets.QWidget | None = None, **kwargs):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.isEditable: bool = kwargs.get("editable", True)
        self.keyPressHandler = KeyPressHandler(self)

        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("EditableLabel:MainLayout")

        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet("border-bottom: 3px dotted grey;")

        self.label.setObjectName("EditableLabel:label")
        self.mainLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("EditableLabel:lineEdit")
        self.mainLayout.addWidget(self.lineEdit)
        # hide the line edit initially
        self.lineEdit.setHidden(True)

        self.setText(text)

        # setup signals
        self.create_signals()

    def setFont(self, font: QtGui.QFont | str | typing.Sequence[str]) -> None:
        self.lineEdit.setFont(font)
        self.label.setFont(font)

    def fontMetrics(self) -> QtGui.QFontMetrics:
        return self.label.fontMetrics()

    def create_signals(self):
        self.lineEdit.installEventFilter(self.keyPressHandler)
        self.label.mousePressEvent = self.labelPressedEvent

        # give the lineEdit both a `returnPressed` and `escapedPressed` action
        self.keyPressHandler.escapePressed.connect(self.escapePressedAction)
        self.keyPressHandler.returnPressed.connect(self.returnPressedAction)
        self.keyPressHandler.textChanged.connect(self.textChangedAction)

    def text(self):
        """Standard QLabel text getter"""
        return self.label.text()

    def setText(self, text: str):
        """Standard QLabel text setter"""
        self.label.blockSignals(True)
        self.label.setText(text)
        self.label.blockSignals(False)

    def labelPressedEvent(self, event: QtGui.QMouseEvent):
        """Set editable if the left mouse button is clicked"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.setLabelEditableAction()

    def setLabelEditableAction(self):
        """Action to make the widget editable"""
        if not self.isEditable:
            return

        self.label.setHidden(True)
        self.label.blockSignals(True)
        self.lineEdit.setHidden(False)
        self.lineEdit.setText(self.label.text())
        self.lineEdit.blockSignals(False)
        self.lineEdit.setFocus(QtCore.Qt.MouseFocusReason)
        self.lineEdit.selectAll()

    def labelUpdatedAction(self):
        """Indicates the widget text has been updated"""
        textToUpdate = self.lineEdit.text()

        if textToUpdate != self.label.text():
            self.label.setText(textToUpdate)

        self.label.setHidden(False)
        self.lineEdit.setHidden(True)
        self.lineEdit.blockSignals(True)
        self.label.blockSignals(False)

    def returnPressedAction(self):
        """Return/enter event handler"""
        self.labelUpdatedAction()

    def escapePressedAction(self):
        """Escape event handler"""
        self.label.setHidden(False)
        self.lineEdit.setHidden(True)
        self.lineEdit.blockSignals(True)
        self.label.blockSignals(False)

    def textChangedAction(self):
        self.labelUpdatedAction()
