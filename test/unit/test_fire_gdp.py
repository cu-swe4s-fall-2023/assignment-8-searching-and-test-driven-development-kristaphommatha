import sys
sys.path.insert(0, '../../src')  # noqa

import fire_gdp
import unittest
import random
import os


class TestFireGDP(unittest.TestCase):
    
    def test_get_data_no_file(self):
        no_file_code = -1
        self.assertEqual(fire_gdp.get_data('NoFile.txt', 0, 'query value'), no_file_code)

    def test_get_data_bad_index(self):
        bad_index_code = -2
        self.assertEqual(fire_gdp.get_data('../../data/Agrofood_co2_emission.csv', 10000, 'query value'), bad_index_code)

if __name__ == "__main__":
    unittest.main()