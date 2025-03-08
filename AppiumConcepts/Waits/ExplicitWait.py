"""Launch USB Connected Device, Run Demo App, find EnterValue btn by ID
using explicit wait and once it is found, click on it.
Then using explicit wait also, look for Text Field by CLASSNAME and send
some text.
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
ele_id = wait.until(lambda device: device.find_element(
    AppiumBy.ID,
    "com.code2lead.kwad:id/EnterValue"
))
ele_id.click()

time.sleep(2)
ele_classname = wait.until(lambda device: device.find_element(
    AppiumBy.CLASS_NAME,
    "android.widget.EditText"
))
ele_classname.send_keys("Skill2Lead")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
