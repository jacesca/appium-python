"""
python -m tests.test_contactusform
"""
import time
from base.DrivenClass import WebDriverClient
from pages.ContactFormPage import ContactForm
from configurationfiles.GlobalVariables import URL_SITE, URL_SITE_TITLE    # noqa


driver = WebDriverClient(explicit_webdriver=True).get_webdriver()

cf = ContactForm(driver=driver, url=URL_SITE)
cf.launch_webpage(title=URL_SITE_TITLE)
time.sleep(2)
cf.click_on_form_menu_option()
cf.verify_form_page_is_displayed()
cf.enter_name()
cf.enter_email()
cf.select_female_gender()
cf.enter_technology()
cf.enter_message()
cf.enter_captcha_text()
time.sleep(5)
cf.submit_contact_form()

time.sleep(2)
driver.quit()
