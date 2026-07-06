"""A single test file run by multiple targets under different configs.

The behaviour is parameterised by the CALC_MODE env var, which each py_test
target sets to a different value. The same source file therefore "belongs" to
more than one test target.
"""

import os
import unittest

from calculator import calculator

MODE = os.environ.get("CALC_MODE", "int")


class CalculatorModesTest(unittest.TestCase):
    def test_add_under_mode(self):
        if MODE == "float":
            self.assertEqual(calculator.add(1.5, 2.5), 4.0)
        else:
            self.assertEqual(calculator.add(1, 2), 3)

    def test_multiply_under_mode(self):
        if MODE == "float":
            self.assertEqual(calculator.multiply(1.5, 2.0), 3.0)
        else:
            self.assertEqual(calculator.multiply(2, 3), 6)
