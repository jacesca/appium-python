"""
PyTest execute test in linear order by default
test_A >> test_B >> test_C >> test_D
Run
`$ pytest -v -s ConceptsPyTest/pytestConcepts/test_pytestRunOrder.py`
"""
import pytest


@pytest.mark.run(order=4)
def test_A():
    print('Test A')


@pytest.mark.run(order=3)
def test_B():
    print('Test B')


@pytest.mark.run(order=2)
def test_C():
    print('Test C')


@pytest.mark.run(order=1)
def test_D():
    print('Test D')
