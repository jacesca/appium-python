# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/ConceptsScenarioOutline
# $ behave login_screen_ex3 .feature
# or
# $ behave login_screen_ex3.feature --no-capture -f plain
# or
# $ behave
# ```

Feature: Fill the Contact Form

    Scenario Outline: User Login Credentials

        Given Launch the App and Click on Login Button
        When Enter <email> UserID
        When Enter <pwd> password
        Then Verify <section> Screen

        Examples:
            | email             | pwd    | Section     |
            | student@gmail.com | S12345 | StudentHome |
            | teacher@gmail.com | T12345 | TeacherSite |
            | admin@gmail.com   | 12345  | AdminPage   |
