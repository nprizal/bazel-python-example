"""Tests for the listutil library."""

import unittest

from listutil import listutil


class ListUtilTest(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(listutil.flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(listutil.flatten([]), [])

    def test_dedupe(self):
        self.assertEqual(listutil.dedupe([1, 1, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(listutil.dedupe(["a", "b", "a"]), ["a", "b"])

    def test_chunk(self):
        self.assertEqual(listutil.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_chunk_invalid_size_raises(self):
        with self.assertRaises(ValueError):
            listutil.chunk([1, 2, 3], 0)
