"""Tests for the stringutil library."""

import unittest

from stringutil import stringutil


class StringUtilTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(stringutil.reverse("abc"), "cba")
        self.assertEqual(stringutil.reverse(""), "")

    def test_is_palindrome(self):
        self.assertTrue(stringutil.is_palindrome("racecar"))
        self.assertTrue(stringutil.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(stringutil.is_palindrome("hello"))

    def test_shout(self):
        self.assertEqual(stringutil.shout("hi"), "HI!")
