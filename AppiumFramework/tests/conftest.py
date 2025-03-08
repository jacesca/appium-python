import pytest
import time
from AppiumFramework.base.DrivenClass import CustomDriver


@pytest.fixture(scope='class')
def before_class(request):
    print('\nStarting suit test cases...')
    driver = CustomDriver().GetDriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print('Clossing process started...')
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def before_method():
    print('\nStarting test case configuration...')
    yield
    print('\nClosing test case...')
