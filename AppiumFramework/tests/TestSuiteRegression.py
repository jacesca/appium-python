"""
Run
`$ pytest --alluredir AppiumFramework/reports/allurereports/  AppiumFramework/tests/TestSuiteRegression.py`   # noqa
`$ allure serve -h localhost AppiumFramework/reports/allurereports/
"""
import unittest
from AppiumFramework.tests.test_loginform import LoginFormTest
from AppiumFramework.tests.test_contactform import ContactFormTest


lf = unittest.TestLoader().loadTestsFromTestCase(LoginFormTest)
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)

regression_test = unittest.TestSuite([cf, lf])
unittest.TextTestRunner(verbosity=1).run(regression_test)
