"""
Logging means tracking the events or steps during the execution of programme or software.

Log Levels
==========
Critical
Error
Warning
Info
Debug


29/03/2020 03:48:17 PM Sunday: INFO: Text Entered in edit box
29/03/2020 03:48:17 PM Sunday: ERROR: Unable to click on search button

"""
import logging

logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.critical("This is critical msg")
logging.error("This is a error msg")
logging.warning("this is warning msg")
logging.info("This is a Info msg")
logging.debug("This is a Debug msg")




