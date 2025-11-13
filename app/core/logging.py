import csv
import json
import logging
import sys
from io import StringIO
from typing import Any

from app.core.config import settings

#logging.basicConfig(level=logging.WARNING,
            # format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log messages at different levels
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
    # settings.LOG_LEVEL
    # "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # if settings.log.format == "json":
    #     from pythonjsonlogger import jsonlogger

    #     formatter = jsonlogger.JSONFormatter()
    # elif settings.log.format == "csv":
    #     formatter = logging.Formatter(
    #         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    #     )
    # else:
    #     None

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

    # logging.basicConfig(
    #     filename=LOG_FILE,
    #     level=logging.INFO,
    #     format=JSONFormatter(),
    #     handlers=[logging.StreamHandler()],
    # )

# print("test")

# logger = logging.getLogger("LOGGER TEST")
# logger.setLevel(logging.DEBUG)

# console_handler = logging.StreamHandler()
# text_formatter = JsonFormatter()
# console_handler.setFormatter(text_formatter)

# file_handler = logging.FileHandler("/var/log/app.log")
# file_handler.setFormatter(text_formatter)


# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# logging.getLogger("LOGGER TEST").info(
#     "Logging configured successfully using %s format at %s level. ",
#     settings.log_format,
#     settings.log_level,
# )
# return logger