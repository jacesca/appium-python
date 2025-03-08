from behave import given, when, then


@given('Launch the app and click on ContactForm')
def launch_app(context):
    print('1 - Launching the app')


@when('Enter name')
def enter_name(context):
    print('2 - Enter name')


@when('Enter Email')
def enter_email(context):
    print('3 - Enter Email')


@when('Enter Mobile Number')
def enter_mobile(context):
    print('4 - Enter Mobile Number')


@when('We need to ckick on submit button')
def need_click_on_submit_btm(context):
    print('5 - We need to ckick on submit button')


@then('Click on submit')
def click_submit(context):
    print('6 - Click on submit')


@then('Take screenshot of contact form')
def take_screenshot(context):
    print('7 - Take screenshot of contact form')
