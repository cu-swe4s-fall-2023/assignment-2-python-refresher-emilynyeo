#!/bin/bash
sys import
sys.path.insert(0, 'ls ../') #noqa

set -e 
set -u 
set -o pipefail

echo "... running print_fires.py ..."
python3 print_fires.py \
	--file_name Agrofood_co2_emission.csv \
	--country_column 0 \
	--country "South Africa" \
	--fires_column 4

set +e
echo "... running print_fires.py (should give error) ..."
python3 print_fires.py \
	--file_name Agrofood_co2_emission.csv \
	--country_column 0 \
	--country "South Africa" \
	--fires_column th

echo "... running print_fires.py (should give error) ..."
python3 print_fires.py \
	--file_name nofile.csv \
	--country_column 0 \
	--country "South Africa" \
	--fires_column 4
set -e