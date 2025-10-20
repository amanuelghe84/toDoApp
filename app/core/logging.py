import csv
import json
import logging
import os
import sys

from io import StringIO

from app.core.config import settings


# Custom logging formatters
class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


logger = logging.getLogger("json_log_app")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
json_formatter = JSONFormatter()
console_handler.setFormatter(json_formatter)

logger.addHandler(console_handler)

logger.info("This is a JSON log app ")

class CSVFormatter(logging.Formatter):
    def _init_(self, fmt: str | None = None, datefmt: str | None = None) -> None:
        super()._init_(fmt, datefmt)
        self.output = StringIO()
        self.writer = csv.writer(self.output)

    def format(self, record: logging.LogRecord) -> str:
        self.output.seek(0)
        self.output.truncate(0)
        self.writer.writerow(
            [
                self.formatTime(record, self.datefmt),
                record.levelname,
                record.getMessage(),
            ]
        )
        return self.output.getvalue().strip()

logger = logging.getLogger("csv_my_app")
logger.setLevel(logging.DEBUG)

csv_file = "logs.csv"
if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
    with open(csv_file, "w") as f:
        f.write("timestamp,level,logger,message\n")

console_handler = logging.StreamHandler()
csv_formatter_console = CSVFormatter()
console_handler.setFormatter(csv_formatter_console)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning("This is a CSV log app")
logger.addHandler(file_handler)
