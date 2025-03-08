"""
# To Install `pytest`
    `$ pip install pytest`
    `$ pip install pytest-ordering`
    `$ pip install pytest-rerunfailures`

# To execute pytest
    - `$ pytest` >> run every test in all the folders tree.
    - `$ pytest -v -s ConceptsPyTest/pytestConcepts`  >> run all test in specific files
    - `$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestExample1.py` >> run one specific file
    - `$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestExample1.py::test_method` >> run one speecific task

# To rerun a failure test that could be truncated by p.e.
# network issues
    - `$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestExample1.py --reruns 5` >> 5 trais before declaring a failure
    - `$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestExample1.py --reruns 5 --reruns-delay 1` >> 5 trais with 1 second delay between before declaring a failure
# With allure reports
    - `$ pytest -v -s --reruns 5 --reruns-delay 1 --alluredir ConceptsPyTest/Reports/ pytestConcepts/test_pytestExample1.py`
# Generate the allure reports
    - `$ allure serve ConceptsPyTest/Reports/`
"""


def test_method():
    print('This is test_method.')


def test_method2():
    print('This is test_method2.')
