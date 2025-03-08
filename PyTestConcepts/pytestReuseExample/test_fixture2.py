"""
To run
`$ pytest -v -s ConceptsPyTest/pytestReuseExample/test_fixture2.py`
or
`$ pytest -v -s ConceptsPyTest/pytestReuseExample`
"""


def test_method3(before_after_module, setup):
    print('This is test 3 in fixture 2.')


def test_method4(before_after_module, setup):
    print('This is test 4 in fixture 2.')
