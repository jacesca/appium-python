"""Run
pytest --alluredir SeleniumFramework/reports/allurereports/  SeleniumFramework/tests/TestSuitRegression.py       # noqa
allure serve -h localhost SeleniumFramework/reports/allurereports/
"""
import unittest
from SeleniumFramework.tests.test_contactform import ContactFormTest
from SeleniumFramework.tests.test_entertextpage import EnterTextTest


cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
et = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)

regression_test = unittest.TestSuite([cf, et])
unittest.TextTestRunner(verbosity=1).run(regression_test)
