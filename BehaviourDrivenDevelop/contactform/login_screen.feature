# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/contactform
# $ behave login_screen.feature
# or
# $ behave login_screen.feature --no-capture -f plain
# or
# $ behave
# ```

Feature: Verify the Home Screen Data

    Scenario: User Login Credentials

        Given Launch the App and Click on Login Button
        When Enter UserID
        When Enter password
        When Click on Login Button
        And Home page opens
        Then Verify Home Screen
        Then Take screenshot

    Scenario: Enter the data in ContactForm

        Given Launch the app and click on ContactForm
        When Enter name
        When Enter Email
        When Enter Mobile Number
        And We need to ckick on submit button 
        Then Click on submit
        Then Take screenshot of contact form
