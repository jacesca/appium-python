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


@then('Verify Home Screen')
def verify_home_screen(context):
    print('4 - Verify Home Screen')
