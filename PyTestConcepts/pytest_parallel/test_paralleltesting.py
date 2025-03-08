"""
Prerrequisites: To use it:
1. Execute
    ```
    $ pip install pytest-xdist=
    ```
2. Add udid and systemPort in Desired Capabilities
3. Run the file using command as `pytest -n <num process>`

Target: Run multiple devices

Run
`$ pytest -n 2 ConceptsPyTest/pytest_parallel`
`$ pytest -n=2 ConceptsPyTest/pytest_parallel`
`$ pytest -n auto ConceptsPyTest/pytest_parallel`
"""

import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver, GalaxyS23


def get_driver(deviceId, sysPort):
    # Step 1: Create "Desired Capabilities"
    # Step 2: Web Driver Object 
    custom_capabilities = GalaxyS23()
    del custom_capabilities['deviceName']
    custom_capabilities['udid'] = deviceId
    custom_capabilities['systemPort'] = sysPort
    driver = GetDriver(device='custom', desired_caps=custom_capabilities)
    return driver


def enter_text(driver):
    # Step 3: Action to execute
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()
    time.sleep(2)

    ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")  # UiSelector()
    ele_classname.send_keys("Skill2Lead")

    # Step 4: Close the driver object
    time.sleep(5)
    driver.quit()


def test_paralleltesting():
    driver_1 = get_driver(deviceId='RFCXA08HHRA', sysPort=8200)
    driver_2 = get_driver(deviceId='emulator-5554', sysPort=8201)

    enter_text(driver_1)
    enter_text(driver_2)
