"""Tests focused on stringutil palindrome detection."""

import unittest

from stringutil import stringutil


class StringUtilPalindromeTest(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(stringutil.is_palindrome("racecar"))

    def test_palindrome_ignores_punctuation_and_case(self):
        self.assertTrue(stringutil.is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        self.assertFalse(stringutil.is_palindrome("hello"))
