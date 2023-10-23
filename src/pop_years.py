import matplotlib.pyplot as plt
from my_utils import get_column
import sys

# Specify the file and columns of interest
country_column = 0
year_column = 1
rural_pop = 25
urban_pop = 26
file_name = sys.argv[1]
country_of_interest = sys.argv[3]
out_file = sys.argv[2]

rural_data = get_column(file_name,
                        country_column,
                        country_of_interest,
                        rural_pop)
urban_data = get_column(file_name,
                        country_column,
                        country_of_interest,
                        urban_pop)
year_data = get_column(file_name,
                       country_column,
                       country_of_interest,
                       year_column)

if not rural_data or not urban_data or not year_data:
    print(f"No data found for {country_of_interest}.")
else:
    plt.figure(figsize=(10, 6))

    # Plot rural population in green
    plt.plot(year_data,
             rural_data,
             marker='o',
             linestyle='-',
             color='green',
             label='Rural Population')

    # Plot urban population in red
    plt.plot(year_data,
             urban_data,
             marker='o',
             linestyle='-',
             color='red',
             label='Urban Population')

    plt.title(f"Population Over the Years for {country_of_interest}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.legend()

    plt.savefig(out_file, format='png', bbox_inches='tight')
    plt.close()
