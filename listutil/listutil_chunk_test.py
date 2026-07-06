"""Tests focused on listutil chunking."""

import unittest

from listutil import listutil


class ListUtilChunkTest(unittest.TestCase):
    def test_even_chunks(self):
        self.assertEqual(listutil.chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_uneven_chunks(self):
        self.assertEqual(listutil.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_invalid_size_raises(self):
        with self.assertRaises(ValueError):
            listutil.chunk([1, 2, 3], 0)
