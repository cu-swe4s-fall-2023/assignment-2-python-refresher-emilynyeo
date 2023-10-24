import sys
import matplotlib.pyplot as plt
from my_utils import get_column

country_column = 0
year_column = 1
temp_column = 30
rural_column = 25
urban_column = 26
file_name = sys.argv[1]
out_file = sys.argv[2]
country = sys.argv[3]

year_data = get_column(file_name, country_column, country, year_column)
temp_data = get_column(file_name, country_column, country, temp_column)
urban_data = get_column(file_name, country_column, country, urban_column)
rural_data = get_column(file_name, country_column, country, rural_column)

if not year_data or not temp_data or not rural_data or not urban_data:
    print(f"No data found for {country_of_interest}.")
else:

    # temperature on left y-axis
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(year_data,
             temp_data,
             marker='o',
             linestyle='-',
             label='Temperature (°C)',
             color='red')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Temperature (°C) change", color='red')
    ax1.tick_params(axis='y', labelcolor='red')
    ax1.grid(True)

    # rural and urban populations on secondary y-axis (right)
    ax2 = ax1.twinx()
    ax2.plot(year_data,
             rural_data,
             marker='o',
             linestyle='-',
             label='Rural Population',
             color='blue')
    ax2.plot(year_data,
             urban_data,
             marker='o',
             linestyle='-',
             label='Urban Population',
             color='green')
    ax2.set_ylabel("Population",
                   color='black')
    ax2.tick_params(axis='y',
                    labelcolor='black')

    # combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    # Save plot as PNG
    plt.savefig(out_file, format='png', bbox_inches='tight')
    plt.close()
