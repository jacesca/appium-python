# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/ConceptsScenarioOutline
# $ behave login_screen_ex2 .feature
# or
# $ behave login_screen_ex2.feature --no-capture -f plain
# or
# $ behave
# ```

Feature: Fill the Contact Form

    Scenario Outline: User Login Credentials

        Given Launch the App and Click on Login Button
        When Enter <email> UserID
        When Enter <pwd> password
        Then Verify Home Screen

        Examples:
            | email | pwd |
            | student@gmail.com | S12345 |
            | teacher@gmail.com | T12345 |
            | admin@gmail.com   | 12345  |
