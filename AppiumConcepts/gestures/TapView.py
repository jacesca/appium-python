"""Perform the following actions, using explicit wait.
- Run Demo App on Android device.
- Click on Login btn using coords. 
"""
import time
from devices.AvailableDevices import GetDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[
        ElementNotVisibleException,
        ElementNotSelectableException,
        NoSuchElementException
    ]
)

# Step 3: Action to execute
driver.execute_script('mobile: clickGesture', {'x': 343, 'y': 1965})    # Login Btn

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
