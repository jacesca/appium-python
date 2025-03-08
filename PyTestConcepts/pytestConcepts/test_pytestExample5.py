"""
To run
`$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestExample5.py`
"""
import pytest


@pytest.fixture(scope='module')
def before_after_module():
    print('\n***************************************')
    print('Before module')
    print('***************************************')
    yield
    print('\n***************************************')
    print('After module')
    print('***************************************')


@pytest.fixture()
def setup():
    print('\nBefore the test method.')
    yield
    print('\nAfter the test method.')


def test_method9(before_after_module, setup):
    print('This is test_method9.')


def test_method10(before_after_module, setup):
    print('This is test_method10.')
