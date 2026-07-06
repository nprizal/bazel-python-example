"""Tests for the calculator library."""

import unittest

from calculator import calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            calculator.divide(1, 0)
