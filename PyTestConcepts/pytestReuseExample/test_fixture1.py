"""
To run
`$ pytest -v -s ConceptsPyTest/pytestReuseExample/test_fixture1.py`
or
`$ pytest -v -s ConceptsPyTest/pytestReuseExample`
"""
# # This is no required as we mantain the required componentes in
# # the conftest.py file
# import pytest
# from pytestReuseExample.conftest import before_after_module, setup


def test_method1(before_after_module, setup):
    print('This is test 1 in fixture 1.')


def test_method2(before_after_module, setup):
    print('This is test 2 in fixture 1.')
