"""Tests for the mathutil library."""

import unittest

from mathutil import mathutil


class MathUtilTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(mathutil.factorial(0), 1)
        self.assertEqual(mathutil.factorial(5), 120)

    def test_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            mathutil.factorial(-1)

    def test_is_prime(self):
        self.assertTrue(mathutil.is_prime(7))
        self.assertFalse(mathutil.is_prime(1))
        self.assertFalse(mathutil.is_prime(9))

    def test_gcd(self):
        self.assertEqual(mathutil.gcd(12, 18), 6)
        self.assertEqual(mathutil.gcd(7, 5), 1)
