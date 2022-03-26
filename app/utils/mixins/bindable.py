from typing import Any, Type

from app.models.Model import Model


class Bindable:
    def __init__(self):
        self._boundObject: Model | None = None
        self._boundProperty: str | None = None
        self._updateProperty: str | None = None

        self._boundUpdateObject: Model | None = None
        self._boundUpdateProperty: str | None = None

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ) -> None:
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

    def setUpdateBinding(self, object: Model, property: str):
        self._boundUpdateObject = object
        self._boundUpdateProperty = property

    def isModified(self) -> bool:
        assert self._boundObject is not None

        return self._boundObject.is_dirty()  # type: ignore

    @property
    def isPropertyBound(self) -> bool:
        return self._boundProperty is not None and self._boundObject is not None

    @property
    def isUpdatePropertyBound(self) -> bool:
        return (
            self._boundUpdateProperty is not None
            and self._boundUpdateObject is not None
        )

    def updateBoundObject(self, value: Any):
        value = value if value != None else ""

        if self.isPropertyBound:
            updateObject = self._boundObject
            updateProperty = self._boundProperty
        elif self.isUpdatePropertyBound:
            updateObject = self._boundUpdateObject
            updateProperty = self._boundUpdateProperty
        else:
            raise Exception("Bound object or property not set")

        assert updateProperty is not None

        setattr(updateObject, updateProperty, value)

        debug(updateObject, dict(zip([updateProperty], [value])))

    def boundValue(self, default: Any = None) -> Any:
        if self.isPropertyBound:
            return getattr(self._boundObject, self._boundProperty, default)
        else:
            return default
