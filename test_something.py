import numpy as np
import pytest

def test_arithmatic():
	assert 1+2 == 3

def test_len():
	x = ['a', 'b', 'c']
	assert len(x) == 3


def test_float():
	assert np.isclose(1.1 + 2.2, 3.3)

def test_array():
	x = np.array([1.1, 1.1])
	y = np.array([2.2, 2.2])
	z = np.array([3.3, 3.3])
	assert np.allclose(x + y, z)

def test_whatever():
	with pytest.raises(ValueError):
		int('xyz')

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_whatever_filip():
	1 / 0
