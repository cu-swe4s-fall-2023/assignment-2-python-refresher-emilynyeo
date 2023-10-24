import sys
from my_utils import get_column
import matplotlib.pyplot as plt

country_column = 0
year_column = 1
temp_column = 30
emission_column = 29
file_name = sys.argv[1]
out_file = sys.argv[2]
country = sys.argv[3]

year_data = get_column(file_name, country_column, country, year_column)
temp_data = get_column(file_name, country_column, country, temp_column)
emission_data = get_column(file_name, country_column, country, emission_column)


if not year_data or not temp_data or not emission_data:
    print(f"No data found for {country_of_interest}.")
else:
    plt.figure(figsize=(10, 6))

    # plot emission data in grey on left y axis
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(year_data,
             emission_data,
             marker='o',
             linestyle='-',
             label='Emissions Total',
             color='grey')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Emissions Total", color='grey')
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.grid(True)

    # plot temp data in red on the right y axis
    ax2 = ax1.twinx()
    ax2.plot(year_data,
             temp_data,
             marker='o',
             linestyle='-',
             label='Temperature',
             color='red')
    ax2.set_ylabel("Temperature",
                   color='black')
    ax2.tick_params(axis='y',
                    labelcolor='black')

    # combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.title(f"Emission and Temperature Trends over the Years")
    plt.grid(True)
    plt.savefig(out_file, format='png', bbox_inches='tight')
    plt.close()
