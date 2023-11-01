import sys
sys.path.insert(0, '../../src')  # noqa

import fire_gdp
import unittest
import random
import os


class TestFireGDP(unittest.TestCase):

    def test_get_data_no_file(self):
        no_file_code = -1
        self.assertEqual(fire_gdp.get_data('NoFile.txt', 0, 'query value'),
                         no_file_code)

    def test_get_data_bad_index(self):
        bad_index_code = -2
        self.assertEqual(fire_gdp.get_data('../data/test_data.csv', 10000,
                                           'query value'),
                         bad_index_code)

    def test_get_data_positive_no_header(self):
        test_query_col = 0
        test_query_value = "Query"
        func_return = fire_gdp.get_data('../data/test_data.csv',
                                        test_query_col, test_query_value,
                                        header=False)
        expected = [['Query', '1990', '14.7237', '0.0557', '205.6077', '0'],
                    ['Query', '1991', '14.7237', '0.0557', '0', '0'],
                    ['Query', '1992', '14.7237', '0.0557', '196.5341', '0']]
        self.assertListEqual(func_return, expected)

    def test_get_data_positive_yes_header(self):
        test_query_col = 0
        test_query_value = "Query"
        func_return = fire_gdp.get_data('../data/test_data.csv',
                                        test_query_col, test_query_value)
        expected = [['Search', 'Year', 'Savanna fires', 'Forest fires',
                     'Crop Residues', 'Rice Cultivation'],
                    ['Query', '1990', '14.7237', '0.0557', '205.6077', '0'],
                    ['Query', '1991', '14.7237', '0.0557', '0', '0'],
                    ['Query', '1992', '14.7237', '0.0557', '196.5341', '0']]

        self.assertListEqual(func_return, expected)

    def test_search_negative(self):
        nums = []
        for i in range(100):
            nums.append(random.randint(1, 100))
        search_key = 0
        expected = []

        self.assertListEqual(fire_gdp.search(nums, search_key), expected)

    def test_search_positive(self):
        nums = []
        for i in range(100):
            nums.append(random.randint(1, 100))
        search_key = 0

        nums[0] = search_key
        nums[51] = search_key
        nums[99] = search_key

        expected = [0, 51, 99]

        self.assertListEqual(fire_gdp.search(nums, search_key), expected)

    def test_splitter_mixture(self):
        test_string = 'str,ex,"test,c",tester,"test2"'
        func_return = fire_gdp.splitter(test_string, '"', ',')
        expected = ['str', 'ex', 'test,c', 'tester', 'test2']

        self.assertListEqual(func_return, expected)


if __name__ == "__main__":
    unittest.main()
