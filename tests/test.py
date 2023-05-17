import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 6, 6) == 12

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 6, 3) == 3

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 6, 6) == 36

    def test_division_success(self):
        assert self.calculator.division(self, 6, 3) == 2
