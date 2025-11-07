import logging

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s - %(name)s - %(levelName)s - %(message)s")

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_log_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelName)s - %(message)s")
console_log_handler.setFormatter(formatter)

logger.addHandler(console_log_handler)
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
    # set the formatter to be our custom formatter `formatter`
    console_log_handler.setFormatter(formatter)

3. add console log output handler to our logger


"""

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

