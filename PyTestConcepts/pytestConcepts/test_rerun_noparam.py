""" (Reviewing how can add reruns in code)
To run
`$ pytest -v -s ConceptsPyTest/pytestConcepts/test_rerun_noparam.py`
"""
import pytest


@pytest.mark.flaky(reruns=5)
def test_method():
    var1 = 1
    var2 = 2
    assert var1 == var2
