#!/usr/bin/env python
from tkinter import E
import typing
from PySide6 import QtCore, QtGui, QtWidgets

from app.storage import Storage


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
            # self.textChanged.emit(True)

        return QtCore.QObject.eventFilter(self, obj, event)


class EditableLabel(QtWidgets.QWidget):
    """
    Editable label

    URL: https://gist.github.com/mfessenden/baa2b87b8addb0b60e54a11c1da48046
    """

    modified = QtCore.Signal(bool)
    textChanged = QtCore.Signal(str)

    # TODO Add dotted line beneath to signify editable

    def __init__(self, text: str, parent: QtWidgets.QWidget | None = None, **kwargs):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self._editing: bool = False

        self.isEditable: bool = kwargs.get("editable", True)
        self.keyPressHandler = KeyPressHandler(self)

        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.setContentsMargins(Storage.ZERO_MARGINS)
        self.mainLayout.setObjectName("EditableLabel")

        self.label = QtWidgets.QLabel(self)
        self.label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, self.label.sizePolicy().verticalPolicy()
        )
        self.label.setStyleSheet("border-bottom: 3px dotted grey;")  # TODO Not working!

        self.icon = QtWidgets.QLabel()

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setStyleSheet("border: none;")
        self.lineEdit.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, self.lineEdit.sizePolicy().verticalPolicy()
        )
        self.lineEdit.editingFinished.connect(lambda: self.modified.emit(True))

        icon = kwargs.get("icon")

        if icon:
            self.lineEdit.addAction(
                icon, QtWidgets.QLineEdit.ActionPosition.LeadingPosition
            )
            self.icon.setPixmap(icon)

        # hide the line edit initially
        self.lineEdit.setHidden(True)

        self.setText(text)

        # setup signals
        self.create_signals()

        self.mainLayout.addWidget(self.icon)
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.lineEdit)

    def isModified(self) -> bool:
        return self.lineEdit.isModified()

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
        # self.keyPressHandler.textChanged.connect(self.textChangedAction)

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

    def toggleEditing(self, editable: bool | None = None):
        if isinstance(editable, bool):
            self._editing = not editable
        else:
            self._editing = not self._editing

        self.icon.setHidden(not self._editing)
        self.label.setHidden(not self._editing)
        self.label.blockSignals(not self._editing)
        self.lineEdit.setHidden(self._editing)
        self.lineEdit.blockSignals(self._editing)

    def setLabelEditableAction(self):
        """Action to make the widget editable"""
        if not self.isEditable:
            return

        self.toggleEditing(True)
        self.lineEdit.setText(self.label.text())
        self.lineEdit.setFocus(QtCore.Qt.MouseFocusReason)
        self.lineEdit.setCursorPosition(0)

    def labelUpdatedAction(self):
        """Indicates the widget text has been updated"""
        textToUpdate = self.lineEdit.text()

        if textToUpdate != self.label.text():
            self.label.setText(textToUpdate)
            self.textChanged.emit(textToUpdate)

        self.toggleEditing()
        self.lineEdit.setFocus(QtCore.Qt.MouseFocusReason)
        self.lineEdit.selectAll()

    def returnPressedAction(self):
        """Return/enter event handler"""
        self.labelUpdatedAction()

    def escapePressedAction(self):
        """Escape event handler"""
        self.toggleEditing()

    def textChangedAction(self):
        self.labelUpdatedAction()
