""" (Reviewing how rerun behaves)
To run
`$ pytest -v -s ConceptsPyTest/pytestConcepts/test_rerun.py --reruns 5 --reruns-delay 1`
"""


def test_method():
    var1 = 1
    var2 = 2
    assert var1 == var2
