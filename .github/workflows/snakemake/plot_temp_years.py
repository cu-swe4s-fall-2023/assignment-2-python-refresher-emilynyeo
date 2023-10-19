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

# line plot
plt.figure(figsize=(10, 6))
plt.plot(years, temperature, marker='o', linestyle='-')
plt.title(f"Average Temperature in {country}")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)

# Save plot as PNG
#plt.savefig(f'{country}_ty.png', format='png')
plt.savefig(out_file, format='png',bbox_inches='tight')
plt.close()