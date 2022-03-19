class ObjectMixin:
    def attrexists(self, __name: str) -> bool:
        try:
            getattr(self, __name)
        except AttributeError:
            return False
        else:
            return True
