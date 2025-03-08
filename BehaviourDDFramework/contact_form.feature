# Run
#
# $ cd BehaviourDDFramework
# $ behave 
# $ behave --no-capture -f plain
#
# $ behave -f allure_behave.formatter:AllureFormatter -o "reports/allureReports" --no-capture -f plain
# $ allure serve "reports/allureReports"

Feature: Fill the contact form

    Scenario: Contact form page

        Given Create the class object in cfp
        When Click Contact form
        Then Verify form page
        And Enter data in form
