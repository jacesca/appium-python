"""
Logging library demo
Format Ex.
2024-12-23 04:09:49 PM Monday: CRITICAL: This is a critical msg!
"""
import logging


# logging configuration
logging.basicConfig(
    filename="Reports/LoggingDemo1.log",
    level=logging.DEBUG,
    format="%(asctime)s: %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d %I:%M:%S %p %A' ,
    filemode="a"  # Use `w` if you want to rewrite log each time.
)

# Message example
logging.critical("This is a critical msg!")
logging.error('This is an error msg!')
logging.warning('This is a warning msg!')
logging.info('This is an info msg!')
logging.debug('This is a debug msg')
