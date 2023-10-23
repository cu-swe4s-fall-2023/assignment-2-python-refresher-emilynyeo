import sys
import pandas as pd
import matplotlib.pyplot as plt

input_files = sys.argv[1]
output_file = sys.argv[2]
countries = sys.argv[3]

# Define colors for each country
colors = ['b', 'g', 'r', 'c']

# Create a plot for each country
for i, (input_file, country) in enumerate(zip(input_files, countries)):
    country_data = pd.read_csv(input_file, sep='\t')
    plt.plot(country_data['Year'],
             country_data['Temperature'],
             label=f'{country}',
             color=colors[i])

# Customize the plot
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature Changes Over the Years')
plt.legend()

# Save the plot to the output file
plt.savefig(out_file, format='png', bbox_inches='tight')
plt.close()
