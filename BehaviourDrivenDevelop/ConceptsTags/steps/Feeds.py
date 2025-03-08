from behave import given, when, then


@given("Launch the feed page")
def launch_feed(context):
    print("Feed-1: Launch the feed page")


@when("Publish the feed")
def publish_feed(context):
    print("Feed-2: Publish the feed")


@then("Verify feed")
def ferify_feed(context):
    print("Feed-3 - Verify feed")
