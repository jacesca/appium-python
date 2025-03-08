from base.DrivenClass import CustomDriver
from pages.ContactUsFormPage import ContactUsForm


driver = CustomDriver().GetDriver()

cf = ContactUsForm(driver=driver)
cf.click_contact_form()
cf.verify_contact_page()
cf.send_name()
cf.send_email()
cf.send_address()
cf.send_mobile()
cf.submit_contact_form()
