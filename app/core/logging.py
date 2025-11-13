import csv
import json
import logging
import sys
from io import StringIO
from typing import Any

from app.core.config import settings

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record: dict[str, Any] = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)

class CSVFormatter(logging.Formatter):
    def _init_(self, fmt: str | None = None, datefmt: str | None = None) -> None:
        super()._init_(fmt, datefmt)
        self.output = StringIO()
        self.writer = csv.writer(self.output)

def get_logger(name: str) -> None:
    logger = logging.getLogger(name)
    logger.setLevel(settings.log_level.upper())

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setLevel(settings.log_level.upper())
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.debug("debug message (will go to file)")
    logger.info("info message (will go to file)")
    logger.warning("warning message (will go to file)")
    logger.error("Error message (will go to file)")

    return logger

