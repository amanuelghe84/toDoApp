import csv
import json
import logging
import sys
from io import StringIO

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log messages at different levels
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# text format
# create logger
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# console handler
console_handler = logging.StreamHandler()

# Text formatter
text_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(text_formatter )

# Add handler
logger.addHandler(console_handler)

# Log message
logger = logging.info("This is a text log example")

"""
1. create logger | 1. add name  2. set level

    # get logger with name set
    logger = logging.getLogger(__name__)
    # set logger level
    logger.setLevel(logging.DEBUG)


2. create log handler or output mechanism

    # set log terminal or console handler
    console_log_handler = logging.StreamHandler()
    #create log formatter
    custom_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelName)s - %(message)s)
    # set the formatter to be our custom formatter `console_log_formatter`
    console_log_handler.setFormatter(formatter)

3. add console log output handler to our logger


"""

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record: dict[str, Any] = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)



logger = logging.getLogger("json_example")
logger.setLevel(logging.DEBUG)




