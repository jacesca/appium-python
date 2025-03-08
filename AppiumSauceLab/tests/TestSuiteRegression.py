"""
Run
`$ pytest --alluredir reports/allurereports/  tests/TestSuiteRegression.py`   # noqa
`$ allure serve -h localhost reports/allurereports/
"""
import unittest
from tests.test_loginform import LoginFormTest
from tests.test_contactform import ContactFormTest


lf = unittest.TestLoader().loadTestsFromTestCase(LoginFormTest)
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)

regression_test = unittest.TestSuite([cf, lf])
unittest.TextTestRunner(verbosity=1).run(regression_test)
