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



logger = logging.getLogger("LOGGER TEST")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
text_formatter = JsonFormatter()
console_handler.setFormatter(text_formatter)

file_handler = logging.FileHandler("/var/log/app.log")
file_handler.setFormatter(text_formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)

logging.getLogger("LOGGER TEST").info(
    "Logging configured successfully using %s format at %s level. ",
    settings.log_format,
    settings.log_level,
)