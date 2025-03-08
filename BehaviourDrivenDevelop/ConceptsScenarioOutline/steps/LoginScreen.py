from behave import given, when, then


@given('Launch the App and Click on Login Button')
def launch_app(context):
    print('1 - Launching the app')


@when('Enter {email} UserID')
def enter_userid(context, email):
    context.user_id = email
    print('2 - Enter user:', email)


@when('Enter {pwd} password')
def enter_password(context, pwd):
    print('3 - Enter password:', pwd)


@when('Click on Login Button')
def click_login_btn(context):
    print('4 - Click on Login Button')


@when('Home page opens')
def home_page_open(context):
    print(f'5 - Home page opens for {context.user_id}')


@then('Verify Home Screen')
def verify_home_screen(context):
    print(f'6 - Verify Home Screen for {context.user_id}')


@then('Verify {section} Screen')
def verify_custom_home_screen(context, section):
    print(f'6.1 - Verify {section} Login Page')


@then('Take screenshot')
def take_screenshot(context):
    print('7 - Take screenshot')
