test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

test_file = ".csv"

run basic_mean \
	python ../../print_fires.py \
	--stats mean \
	--file_name "$.csv"
assert_exit_code 0
assert_equal "ExpectedOutput" "$output"

run basic_median \
	python ../../print_fires.py \
	--stats median 
	--file_name "$.csv"
assert_exit_code 0
assert_equal "ExpectedOutput" "$output"

run basic_std_dev \
	python ../../print_fires.py \
	--stats std_dev
	--file_name "$.csv" 
assert_exit_code 0
assert_equal "ExpectedOutput" "$output"

# this file should be run from the functional test drectory. 
# This ../../ is assuming print_fires.py is in your main
# To run this , you just say bash test_print_fires.sh