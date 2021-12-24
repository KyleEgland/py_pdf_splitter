#! python
#
# config.py
import logging
import logging.config
import os


appdir = os.getcwd()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s [ %(filename)s ] Line: %(lineno)s "
            "(%(levelname)s) %(name)s:  %(message)s",
            # Example date format: "%Y-%m-%d %H:%M:%S"
            "datefmt": "%H:%M:%S"
        }
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default"
        }
    },
    "loggers": {
        "PyPdfManifpulator": {
            "handlers": ["default"],
            "level": "DEBUG",
        }
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(f"PyPdfManifpulator.{__name__}")
logger.debug("Logger created and running...")


class Config(object):
    def __init__(self, *args):
        self.logger = logging.getLogger("PyPdfManifpulator.ConfigObject")
        self.logger.debug("__init__ started...")

        self.APP_DIR = appdir
        self.logger.debug(f"APP_DIR: {self.APP_DIR}")

        self.APP_ENV = os.environ.get("APP_ENV") or "development"
        self.logger.debug(f"APP_ENV: {self.APP_ENV}")

        self.APP_NAME = os.environ.get("APP_NAME") or "Python PDF Manipulator"
        self.logger.debug(f"APP_NAME: {self.APP_NAME}")

        self.APP_VERSION = os.environ.get("APP_VERSION") or "0.1.1"
        self.logger.debug(f"APP_Version: {self.APP_VERSION}")

        self.logger.debug("...__init__ complete")
