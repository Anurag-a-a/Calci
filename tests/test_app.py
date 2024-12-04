from src.app import Calculator
import pytest

def test_addition():
    assert Calculator.add(2, 3) == 5

def test_subtraction():
    assert Calculator.subtract(5, 3) == 2

def test_multiplication():
    assert Calculator.multiply(2, 3) == 6

def test_division():
    assert Calculator.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(6, 0)