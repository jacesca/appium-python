"""
Testing that app can be launched correctly and the first button can be clicked.
Run
`$ pytest ConceptsPyTest/pytest_appium_example`
Using allure reports
`$ pytest -v -s --reruns 5 --reruns-delay 1 --alluredir ConceptsPyTest/Reports/ pytestConcepts/test_pytestExample1.py`
Then  to create the report
`$ allure serve ConceptsPyTest/Reports/`
"""
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


@pytest.mark.flaky(reruns=5)
def test_launchapp():
    # Step 1: Create "Desired Capabilities"
    # Step 2: Web Driver Object 
    driver = GetDriver(device='Pixel3XL')

    # Step 3: Action to execute
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()

    # Step 4: Close the driver object
    time.sleep(5)
    driver.quit()
