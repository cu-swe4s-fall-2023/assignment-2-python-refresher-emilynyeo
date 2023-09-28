import argparse
from my_utils import *

parser = argparse.ArgumentParser(
    prog='print-fires',
    description='Calculate the total number of fires.',
    epilog='parser argument for printing fires issue')

parser.add_argument('--country',
                    type=str,
                    default='South Africa',
                    help='Name of the country')
parser.add_argument('--country_column',
                    type=int,
                    default=0,
                    help='Column index of the country in the CSV file')
parser.add_argument('--fires_column',
                    type=int,
                    default=23,
                    help='Column index of the fires in the CSV file')
parser.add_argument('--file_name',
                    type=str,
                    default='Agrofood_co2_emission.csv',
                    help='Name of the CSV file')

args = parser.parse_args()
print(args.country)

country = args.country
country_column = args.country_column
fires_column = args.fires_column
file_name = args.file_name

all_fires = get_column(file_name, country_column, country, fires_column)

number_of_fires = sum(all_fires)

print(number_of_fires)
