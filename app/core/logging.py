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



logger = logging.getLogger("json_Example")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
json_formatter = JsonFormatter()
console_handler.setFormatter(json_formatter)

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(json_formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)

logging.Logger.info("This is a JSON example")





