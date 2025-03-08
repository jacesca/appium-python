# Run
#
# $ cd BehaviourDDFramework
# $ behave 
# $ behave --no-capture -f plain
#
# $ behave -f allure_behave.formatter:AllureFormatter -o "reports/allureReports" login_screen.feature --no-capture -f plain
# $ allure serve "reports/allureReports"

Feature: Fill the data in Edit Box Field

    Scenario: Edit box data

        Given Create the class object
        When Click on Locators menu link
        When Enter the data
        Then Click on submit btn
