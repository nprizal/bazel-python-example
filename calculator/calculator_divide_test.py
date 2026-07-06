"""Tests focused on calculator division behaviour."""

import unittest

from calculator import calculator


class CalculatorDivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)

    def test_divide_returns_float(self):
        self.assertEqual(calculator.divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            calculator.divide(1, 0)
