from behave import given, when, then


@given("Launch the page")
def launch_page(context):
    print("Page-1: Launch the page")


@when("Update the page data")
def update_page(context):
    print("Page-2: Update the page data")


@then("Verify page")
def verify_page(context):
    print("Page-3 - Verify page")
