from behave import given, when, then


@given("Launch the profile page")
def launch_profile(context):
    print("profile-1: Launch the profile page")


@when("Change profile pic")
def update_profile(context):
    print("profile-2: Change profile pic")


@then("Verify profile pic")
def verify_profile(context):
    print("profile-3 - Verify profile pic")
