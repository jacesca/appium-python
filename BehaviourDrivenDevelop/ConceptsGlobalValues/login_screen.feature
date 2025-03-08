# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/ConceptsGlobalValues
# $ behave login_screen.feature
# or
# $ behave login_screen.feature --no-capture -f plain
# or
# $ behave
# ```

Feature: Verify the Home Screen Data

    Scenario: User Login Credentials

        Given Launch the App and Click on Login Button
        When Enter "admin@gmail.com" UserID
        When Enter "12345" password
        When Click on Login Button
        And Home page opens
        Then Verify Home Screen
        Then Take screenshot
