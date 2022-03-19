import logging
class LoggerMixin:
    @property
    def log(self):
        return logging.getLogger(self.__class__.__module__)
