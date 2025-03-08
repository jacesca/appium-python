import time
from base.DrivenClass import WebDriverClient
from pages.ContactFormPage import ContactForm
from configurationfiles.GlobalVariables import URL_SITE, URL_SITE_TITLE    # noqa
from utilities import CustomLogger as cl


logger = cl.custom_logger()


def before_all(context):
    msg = 'Automation Started.'
    print(msg)
    logger.info(msg)

    context.test_variable = 'This is a context variable'
    context.driver = WebDriverClient().get_webdriver()
    context.url = URL_SITE
    context.cf = ContactForm(driver=context.driver, url=context.url)

    context.cf.launch_webpage(title=URL_SITE_TITLE)


def after_all(context):
    time.sleep(5)
    context.driver.quit()

    msg = 'Automation Ended.'
    print(msg)
    logger.info(msg)
