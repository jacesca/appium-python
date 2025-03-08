import time
from behave import given, when, then
from pages.ContactFormPage import ContactForm


class ContactFormPage:

    @given('Create the class object in cfp')
    def create_class_object_cfp(context):
        context.cf = ContactForm(context.driver, context.url)

    @when('Click Contact form')
    def click_contactform_menu(context):
        context.cf.click_on_form_menu_option()

    @then('Verify form page')
    def verify_cfp(context):
        context.cf.verify_form_page_is_displayed()

    @then('Enter data in form')
    def enter_data_cfp(context):
        time.sleep(5)
        context.cf.enter_name()
        context.cf.enter_email()
        context.cf.select_female_gender()
        context.cf.enter_technology()
        context.cf.enter_message()
        context.cf.enter_captcha_text()
        context.cf.submit_contact_form()
