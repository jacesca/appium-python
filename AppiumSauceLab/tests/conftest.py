import pytest
import time
from base.DriverClass import CustomDriver


@pytest.fixture(scope='class')
def before_class(request):
    print('\nStarting suit test cases...')
    # driver = CustomDriver().get_local_driver()    # Local driver
    driver = CustomDriver().get_cloud_driver()    # Cloud driver
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
