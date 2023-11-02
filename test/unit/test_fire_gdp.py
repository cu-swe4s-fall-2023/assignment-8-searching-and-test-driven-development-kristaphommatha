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
        expected = [['Query', '1972', '14.7237', '0.0557', '205.6077', '0'],
                    ['Query', '1973', '14.7237', '0.0557', '0', '0'],
                    ['Query', '1975', '14.7237', '0.0557', '196.5341', '0'],
                    ['Query', '1953', '1', '2', '3', '4'],
                    ['Query', '1992', '1', '2', '3', '4']]
        self.assertListEqual(func_return, expected)

    def test_get_data_positive_yes_header(self):
        test_query_col = 0
        test_query_value = "Query"
        func_return = fire_gdp.get_data('../data/test_data.csv',
                                        test_query_col, test_query_value)
        expected = [['Search', 'Year', 'Savanna fires', 'Forest fires',
                     'Crop Residues', 'Rice Cultivation'],
                    ['Query', '1972', '14.7237', '0.0557', '205.6077', '0'],
                    ['Query', '1973', '14.7237', '0.0557', '0', '0'],
                    ['Query', '1975', '14.7237', '0.0557', '196.5341', '0'],
                    ['Query', '1953', '1', '2', '3', '4'],
                    ['Query', '1992', '1', '2', '3', '4']]

        self.assertListEqual(func_return, expected)

    def test_search_negative(self):
        nums = []
        for i in range(100):
            nums.append(random.randint(1, 100))
        search_key = 0

        self.assertIsNone(fire_gdp.search(nums, search_key))

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

    def test_string_with_comma_to_float_negative(self):
        test_string = ''
        func_return = fire_gdp.string_with_comma_to_float(test_string)
        self.assertEqual(func_return, None)

    def test_string_with_comma_to_float_positive(self):
        test_string = '12,347.01'
        func_return = fire_gdp.string_with_comma_to_float(test_string)
        expected = 12347
        self.assertEqual(func_return, 12347.01)
        self.assertIs(type(func_return), float)

    def test_year_data_get_data_fail(self):
        fires_file = 'DoesNotExist.txt'
        gdp_file = 'AlsoDoesNotExist.txt'
        func_return = fire_gdp.get_fire_gdp_year_data(fires_file, gdp_file,
                                                      'target_country', 0, 0)
        expected_error_code = -1
        self.assertEqual(func_return, expected_error_code)

    def test_year_data_no_year(self):
        fires_file = '../data/test_data.csv'
        gdp_file = '../data/IMF_GDP_mini.csv'
        func_return = fire_gdp.get_fire_gdp_year_data(fires_file, gdp_file,
                                                      'Query', 2, 4)
        expected_error_code = -3
        self.assertEqual(func_return, expected_error_code)

    def test_year_data_no_country(self):
        fires_file = '../data/test_data.csv'
        gdp_file = '../data/IMF_GDP_mini.csv'
        func_return = fire_gdp.get_fire_gdp_year_data(fires_file, gdp_file,
                                                      'NoCountry', 2, 4)
        expected_error_code = -3
        self.assertEqual(func_return, expected_error_code)


if __name__ == "__main__":
    unittest.main()
