import pytest
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.base.DrivenClass import WebDrivenClass
import time


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDrivenClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/", "Selenium Template")
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
