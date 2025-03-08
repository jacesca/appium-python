import pytest
import time
from SeleniumFramework.base.DrivenClass import WebDriverClient
from SeleniumFramework.pages.ContactFormPage import ContactForm
from SeleniumFramework.configurationfiles.GlobalVariables import URL_SITE, URL_SITE_TITLE    # noqa


@pytest.fixture(scope='class')
def before_class(request):
    print('\nStarting suit test cases...')
    driver = WebDriverClient().get_webdriver()
    url = URL_SITE
    cf = ContactForm(driver=driver, url=url)
    cf.launch_webpage(title=URL_SITE_TITLE)
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.url = url
    yield driver, url
    print('Clossing process started...')
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def before_method():
    print('\nStarting test case configuration...')
    yield
    print('\nClosing test case...')
