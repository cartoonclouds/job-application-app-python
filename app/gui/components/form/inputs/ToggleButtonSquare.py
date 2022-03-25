# Framework imports
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QPushButton

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class ToggleButtonSquare(Input[QPushButton]):
    _checkedStyles = "background-color: lightblue"
    _uncheckedStyles = "background-color: lightgrey"

    def __init__(self, checkedText: str, uncheckedText: str | None = None):
        super(ToggleButtonSquare, self).__init__(QPushButton(), checkedText)

        self._checkedText: str = checkedText
        self._uncheckedText: str = checkedText

        if uncheckedText is not None:
            self._uncheckedText = uncheckedText

        self._input.setCheckable(True)
        self._input.setCursor(Qt.PointingHandCursor)
        self._input.setText(checkedText)
        self._input.setStyleSheet(ToggleButtonSquare._uncheckedStyles)

        # TOOLTIP "#36373d", "#8a95aa"

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        self._input.setChecked(bool(getattr(self._boundObject, self._boundProperty)))
        self._updateButton()

        self._input.clicked.connect(self._onButtonToggled)

    def _hasUpdatingText(self) -> bool:
        return self._uncheckedText is not None

    @Slot(str)
    def _onButtonToggled(self):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, self._input.isChecked())

        if self._hasUpdatingText():
            self._updateButton()

    def _updateButton(self):
        if self._input.isChecked():
            self._input.setText(self._checkedText)
            self._input.setStyleSheet(ToggleButtonSquare._checkedStyles)
        else:
            self._input.setText(self._uncheckedText)
            self._input.setStyleSheet(ToggleButtonSquare._uncheckedStyles)

    # https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/blob/7a58b37247870f5b0425a5c1c633dfdef56e73ae/gui/widgets/py_icon_button/py_icon_button.py#L228
    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    # ///////////////////////////////////////////////////////////////
    # def enterEvent(self, event=None):
    #     debug("in enterEvent")
    #     self.move_tooltip()
    #     self._tooltip.show()

    # # MOUSE LEAVE
    # # Event fired when the mouse leaves the BTN
    # # ///////////////////////////////////////////////////////////////
    # def leaveEvent(self, event=None):
    #     debug("in leaveEvent")
    #     self.move_tooltip()
    #     self._tooltip.hide()

    # # MOVE TOOLTIP
    # # ///////////////////////////////////////////////////////////////
    # def move_tooltip(self):
    #     debug("in move_tooltip")
    #     # GET MAIN WINDOW PARENT
    #     gp = self.parentWidget().mapToGlobal(QPoint(0, 0))

    #     # SET WIDGET TO GET POSTION
    #     # Return absolute position of widget inside app
    #     pos = self.mapFromGlobal(gp)

    #     # FORMAT POSITION
    #     # Adjust tooltip position with offset
    #     pos_x = pos.x()
    #     # (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2)
    #     pos_y = pos.y()  # + 200

    #     # SET POSITION TO WIDGET
    #     # Move tooltip position
    #     self._tooltip.move(pos_x, pos_y)
