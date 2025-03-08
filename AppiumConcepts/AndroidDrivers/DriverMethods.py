"""Launch USB Connected Device, Run Demo App, and
Review some available android methods
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='Pixel3XL')

# Step 3: Action to execute
print(f"""
Is device locked?  : {driver.is_locked()}
Current package    : {driver.current_package}
Current activity   : {driver.current_activity}
Current context    : {driver.current_context}
Current orientation: {driver.orientation}
""")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()