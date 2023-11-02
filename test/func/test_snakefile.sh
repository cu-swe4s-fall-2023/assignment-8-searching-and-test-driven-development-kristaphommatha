test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src
run snaketest snakemake --cores all
assert_equal France.png $ls France.png
assert_equal Canada.png $ls Canada.png
assert_equal Germany.png $ls Germany.png