import pytest


def logmap(x, r):
    fx = r * (x*(1-x))
    return fx

@pytest.mark.parametrize('input, expected', [((0.1, 2.2), 0.198), ((0.2, 3.4), 0.544), ((0.75, 1.7), 0.31875)])
def test_logmap(input,expected):
    assert logmap(*input) == expected  