"""Tests focused on mathutil prime detection."""

import unittest

from mathutil import mathutil


class MathUtilPrimeTest(unittest.TestCase):
    def test_primes(self):
        for n in (2, 3, 5, 7, 11, 13):
            self.assertTrue(mathutil.is_prime(n))

    def test_non_primes(self):
        for n in (0, 1, 4, 9, 15):
            self.assertFalse(mathutil.is_prime(n))
