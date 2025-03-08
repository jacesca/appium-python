"""
To run
`$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestExample4.py`
"""
import pytest


@pytest.fixture()
def setup():
    print('\nBefore the test method.')


def test_method7(setup):
    print('This is test_method7.')


def test_method8(setup):
    print('This is test_method8.')
