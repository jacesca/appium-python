from behave import given, when, then


@given('Launch the App and Click on Login Button')
def launch_app(context):
    print('1 - Launching the app')


@when('Enter UserID')
def enter_userid(context):
    print('2 - Enter user')


@when('Enter password')
def enter_password(context):
    print('3 - Enter password')


@when('Click on Login Button')
def click_login_btn(context):
    print('4 - Click on Login Button')


@when('Home page opens')
def home_page_open(context):
    print('5 - Home page opens')


@then('Verify Home Screen')
def verify_home_screen(context):
    print('6 - Verify Home Screen')


@then('Take screenshot')
def take_screenshot(context):
    print('7 - Take screenshot')
