# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/ConceptsTearDown
# $ behave login_screen.feature
# or
# $ behave login_screen.feature --no-capture -f plain
# or
# $ behave
#
# Generating allure reports
# $ behave -f allure_behave.formatter:AllureFormatter -o allureReports login_screen.feature --no-capture -f plain
# Report server
# $ allure serve "logs_path"
#
# Example:
# $ behave -f allure_behave.formatter:AllureFormatter -o "allureReports" login_screen.feature --no-capture -f plain
# Report server
# $ allure serve "allureReports"
# ```
@regression
Feature: Fill the contact form

    @login @regression
    Scenario: User Login Credentials

        Given Launch the App and Click on Login Button
        When Enter UserID
        When Enter password
        Then Verify Home Screen
