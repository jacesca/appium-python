"""Run
pytest -v -s tests/TestSuitRegression.py
pytest --alluredir reports/allurereports/  tests/TestSuitRegression.py       # noqa
allure serve -h localhost reports/allurereports/
"""
import unittest
from tests.test_contactform import ContactFormTest
from tests.test_entertextpage import EnterTextTest


cf_suit = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
et_suit = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)

regression_test = unittest.TestSuite([cf_suit, et_suit])
unittest.TextTestRunner(verbosity=1).run(regression_test)
