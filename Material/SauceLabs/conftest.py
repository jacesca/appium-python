import pytest
import time
from AppiumFrameWork.base.DrivenClass import Driver
import AppiumFrameWork.configurationfiles.DeviceConfig as dc


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    # driver = driver1.getDriverMethod()
    driver = driver1.cloudDriver(dc.platformVersion, dc.pName)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
