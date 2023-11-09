test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../UsingLibraries
run snaketest snakemake --cores all
cd ../data
assert_equal CLEAN_IMF_GDP.csv $ls CLEAN_IMF_GDP.csv
assert_equal Homework9.png $ls Homework9.png
