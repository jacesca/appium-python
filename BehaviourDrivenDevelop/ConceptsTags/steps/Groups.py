from behave import given, when, then


@given("Launch the group")
def launch_group(context):
    print("Group-1: Launch the group")


@when("Update the group details")
def update_group(context):
    print("Group-2: Update the group details")


@then("Verify group")
def verify_group(context):
    print("Group-3 - Verify group")
