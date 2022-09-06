import pytest
from math import isclose
import numpy as np
from logistic_iterating.py import logmap, iterate_f


@pytest.mark.parametrize('input, expected', [((0.1, 2.2), 0.198), ((0.2, 3.4), 0.544), ((0.75, 1.7), 0.31875)])
def test_logmap(input,expected):
    assert isclose(logmap(*input),expected)  

def test_logmap_random():
    seed = 42
    # np.random.randint(0, 500)
    assert isclose(iterate_f(20, seed, 1.5), (1/3))

@pytest.mark.parametrize

#assert isclose(iterate_f(100,x,r)[-1],1/3)