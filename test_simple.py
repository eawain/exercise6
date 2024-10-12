from simple import numcheck


def test_numcheck():
    assert numcheck(5, 5) == 10
    assert numcheck(2, 2) == 4
    assert numcheck(10, 10) == 20
