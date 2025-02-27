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

    def test_get_index_positive(self):
        result = hash.get_index('test', 10)
        expected = 6
        self.assertEqual(result, expected)

    def test_h_insert_N_equals_0(self):
        self.assertIsNone(hash.h_insert('test', 3, 0))

    def test_h_insert_int_key(self):
        self.assertIsNone(hash.h_insert(1, 3, 10))

    def test_h_insert_positive(self):
        result = hash.h_insert('test', 3, 10)
        expected = [[], [], [], [], [], [], [('test', 3)], [], [], []]
        self.assertListEqual(result, expected)

    def test_h_insert_collision(self):
        input1 = hash.h_insert('betatest', 3, 10)
        input2 = hash.h_insert('test', 4, 10, input1)
        input3 = hash.h_insert('hashbrown', 4, 10, input2)
        expected = [[('betatest', 3), ('hashbrown', 4)], [], [], [],
                    [], [], [('test', 4)], [], [], []]
        self.assertListEqual(input3, expected)


if __name__ == "__main__":
    unittest.main()
