import pandas as pd
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_file = sys.argv[1]
out_file = sys.argv[2]
country = sys.argv[3]

# columns to read
usecols = ["Area", "Year", "Rural population", 
			"Urban population","Food Household Consumption", 
			"total_emission", "Average Temperature °C"]

# Read as CSV file
data = pd.read_csv(data_file, usecols = usecols)

# Filter for "Area" and extract columns
filtered_data = data[data["Area"] == country]
years = filtered_data["Year"]
temperature = filtered_data["Average Temperature °C"]
rural_population = filtered_data["Rural population"]
urban_population = filtered_data["Urban population"]

# temperature on left y-axis
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(years, temperature, marker='o', linestyle='-', label='Temperature (°C)', color='red')
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature (°C)", color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.grid(True)

# rural and urban populations on secondary y-axis (right)
ax2 = ax1.twinx()
ax2.plot(years, rural_population, marker='o', linestyle='-', label='Rural Population', color='blue')
ax2.plot(years, urban_population, marker='o', linestyle='-', label='Urban Population', color='green')
ax2.set_ylabel("Population", color='black')
ax2.tick_params(axis='y', labelcolor='black')

# combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Save plot as PNG
plt.savefig(out_file, format='png', bbox_inches='tight')
plt.close()
