import argparse
from my_utils import *

# Create a custom action for the 'country' argument
class CountryAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser(
    prog='print-fires',
    description='Calculate the total number of fires.',
    epilog='parser argument for printing fires issue')

parser.add_argument('--country',
                    type=str,
                    action=CountryAction,
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
parser.add_argument('--stats',
                    type=str,
                    help='Column index for fires Column',
                    required=False,
                    default=None)
parser.add_argument('--command',
                    type=str,
                    help='which stat tool you want to run',
                    required=False,
                    default=None)

args = parser.parse_args()
print(args.country)

country = args.country
country_column = args.country_column
fires_column = args.fires_column
file_name = args.file_name
command = args.command

all_fires = get_column(file_name, country_column, country, fires_column)
if command == "mean":
    print(mean(all_fires))
elif command == "median":
    print(median(all_fires))
elif command == "std_dev":
    print(std_dev(all_fires))
else:
    print(sum(all_fires))
