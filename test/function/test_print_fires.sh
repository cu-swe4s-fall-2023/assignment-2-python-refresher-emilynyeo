test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

test_file="../data/Agro2_co2_subset.csv"

run basic_mean \
	python ../../src/print_fires.py \
	--stats mean \
	--file_name "$test_file"
assert_exit_code 0
#assert_equal "ExpectedOutput" "$output"

run basic_median \
	python ../../src/print_fires.py \
	--stats median \
	--file_name "$test_file"
assert_exit_code 0
#assert_equal "ExpectedOutput" "$output"

run basic_std_dev \
	python ../../src/print_fires.py \
	--stats std_dev \
	--file_name "$test_file"
assert_exit_code 0
#assert_equal "ExpectedOutput" "$output"
