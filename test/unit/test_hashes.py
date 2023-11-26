import sys
sys.path.insert(0, '../../src')  # noqa

import hash_functions as hash
import unittest
import random
import os


class TestHash(unittest.TestCase):

    def test_get_index_N_equals_0(self):
        self.assertIsNone(hash.get_index('test', 0))

    def test_get_index_int_key(self):
        self.assertIsNone(hash.get_index(0, 0))

    def test_h_insert_N_equals_0(self):
        self.assertIsNone(hash.h_insert('test', 3, 0))

    def test_h_insert_int_key(self):
        self.assertIsNone(hash.h_insert(1, 3, 10))


if __name__ == "__main__":
    unittest.main()
