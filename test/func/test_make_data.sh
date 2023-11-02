test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run make_data_functional python ../../src/make_data.py --ff ../data/test_data.csv --gf ../data/IMF_GDP_mini.csv --c1 'Query' --c2 'Test1' --c3 'Test2' --q 3
assert_exit_code 0
cd ../data
assert_equal Query.csv $( ls Query.csv)
assert_equal Test1.csv $( ls Test1.csv)
assert_equal Test2.csv $( ls Test2.csv)

run make_data_no_fire_file python ../../src/make_data.py --ff DoesNotExist.txt --gf ../data/IMF_GDP_mini.csv --c1 'Query' --c2 'Test1' --c3 'Test2' --q 3
assert_exit_code 1

run make_data_no_gdp_file python ../../src/make_data.py --ff ../data/test_data.csv --gf DoesNotExist.txt --c1 'Query' --c2 'Test1' --c3 'Test2' --q 3
assert_exit_code 1

run make_data_no_country python ../../src/make_data.py --ff ../data/test_data.csv --gf ../data/IMF_GDP_mini.csv --c1 'DoesNotExist' --c2 'Test1' --c3 'Test2' --q 3
assert_exit_code 0
assert_in_stdout 'Could not find information on country in fires file or gdp file'

run make_data_no_year python ../../src/make_data.py --ff ../data/test_data.csv --gf ../data/IMF_GDP_mini.csv --c1 'Query' --c2 'Test1' --c3 'Test2' --q 3 --y 0
assert_exit_code 0
assert_in_stdout 'Could not find information on country in fires file or gdp file'