import sys
sys.path.insert(0, '../../UsingLibraries')  # noqa

import dataFunctions as dfs
import pandas as pd
import unittest
from pandas.testing import assert_frame_equal
import random
import os


class TestDataFunctions(unittest.TestCase):

    def test_collect_fire_years_data_no_file(self):
        no_file_code = -1
        output = dfs.collect_fire_years_data('NoFile.txt', 'Area', 'Query',
                                             ['Savanna fires', 'Forest fires'])
        self.assertEqual(output, no_file_code)

    def test_collect_fire_years_data_success(self):
        expected = {'Year': [1972, 1973, 1975, 1953, 1992],
                    'Savanna fires': [14.7237, 14.7237, 14.7237, 1, 1],
                    'Forest fires': [0.0557, 0.0557, 0.0557, 2, 2]}
        expected_df = pd.DataFrame(expected)
        output = dfs.collect_fire_years_data('../data/test_data.csv',
                                             'Search', 'Query',
                                             ['Savanna fires', 'Forest fires'])
        self.assertEqual(expected_df.size, output.size)

    def test_destroy_commas(self):
        output = dfs.destroy_commas('1,234.0')
        self.assertEqual(output, 1234.0)

    def test_clean_data_no_file(self):
        no_file_code = -1
        output = dfs.clean_data('NoFile.txt')
        self.assertEqual(output, no_file_code)


if __name__ == "__main__":
    unittest.main()
