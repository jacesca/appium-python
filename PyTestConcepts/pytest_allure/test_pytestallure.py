"""
Run
`$ pytest -v -s --alluredir ConceptsPyTest/Reports/allure_example/ --reruns 5 --reruns-delay 1 pytest_allure/test_pytestallure.py`   # noqa
`$ allure serve ConceptsPyTest/Reports/allure_example/
"""
import pytest
import allure


def test_A():
    allure_logs('Launching the app')
    allure_logs('This is a Method A - Step 1')
    allure_logs('This is a Method A - Step 2')
    allure_logs('This is a Method A - Step 3')
    print('Test A')


def test_B():
    allure_logs('This is a Method B - Step 1')
    allure_logs('This is a Method B - Step 2')
    allure_logs('This is a Method B - Step 3')
    print('Test B')


@pytest.mark.skip
def test_C():
    allure_logs('This is a Method C - Step 1')
    allure_logs('This is a Method C - Step 2')
    print('Test C')


def test_D():
    allure_logs('This is a Method D - Step 1')
    allure_logs('This is a Method D - Step 2')
    print('Test D')
    assert False


def test_E():
    allure_logs('This is a Method E - Step 1')
    allure_logs('This is a Method E - Step 2')
    allure_logs('Close App')
    print('Test E')


def allure_logs(text):
    with allure.step(text):
        pass
