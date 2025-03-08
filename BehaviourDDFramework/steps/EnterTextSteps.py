import time
from behave import given, when, then
from pages.EnterTextPage import EnterTextPage


class EnterTextStep:

    @given('Create the class object')
    def create_class_object_et(context):
        context.et = EnterTextPage(context.driver, context.url)
        print(context.test_variable)

    @when('Click on Locators menu link')
    def click_locator_menu(context):
        context.et.click_on_locator_menu_option()

    @when('Enter the data')
    def enter_data_et(context):
        context.driver.maximize_window()
        time.sleep(2)
        context.et.enter_text()

    @then('Click on submit btn')
    def click_submit_et(context):
        context.et.submit_enter_text_form()
