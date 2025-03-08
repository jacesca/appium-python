import logging
import inspect
import allure
from configurationfiles.GlobalVariables import LOG_FILE


def custom_logger() -> logging:
    # 1. Get the class / method name from where the custom logger is called
    log_name = inspect.stack()[1][3]

    # 2. Create the logging object and pass the log_name
    logger = logging.getLogger(log_name)

    # 3. Set log level
    logger.setLevel(logging.DEBUG)

    # 4. Create the filehandler
    filehandler = logging.FileHandler(LOG_FILE)

    # 5. Set the log lever for the filehandler
    filehandler.setLevel(logging.DEBUG)

    # 6. Set the log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S %A'
    )

    # 7. Set the filehandler format
    filehandler.setFormatter(formatter)

    # 8. Atach file handler to logging
    logger.addHandler(filehandler)

    # 9. Return the logger object
    return logger


def allureLogs(text: str) -> None:
    with allure.step(text):
        pass
