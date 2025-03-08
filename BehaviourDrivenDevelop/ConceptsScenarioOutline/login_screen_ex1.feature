# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/ConceptsScenarioOutline
# $ behave login_screen_ex1.feature
# or
# $ behave login_screen_ex1.feature --no-capture -f plain
# or
# $ behave
#
# Summary:
# In Summary, "Scenario" is used for individual, non-parameterized test cases, 
# while "Scenario Outline" is used for parameterized test cases where the same 
# steps are executed with different sets of input data.
# ```

Feature: Fill the Contact Form

    Scenario: Student Login Credentials

        Given Launch the App and Click on Login Button
        When Enter "student@gmail.com" UserID
        When Enter "S12345" password
        Then Verify Home Screen

    Scenario: Teacher Login Credentials

        Given Launch the App and Click on Login Button
        When Enter "teacher@gmail.com" UserID
        When Enter "T12345" password
        Then Verify Home Screen
