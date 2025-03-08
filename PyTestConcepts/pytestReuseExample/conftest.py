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
