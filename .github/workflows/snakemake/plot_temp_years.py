import pandas as pd
import matplotlib.pyplot as plt

# Defining the columns to read
usecols = ["Area", "Year", "Rural population", 
			"Urban population","Food Household Consumption", 
			"total_emission", "Average Temperature °C"]

# Read the CSV file
data = pd.read_csv("Agro2_co2_emissions.csv", usecols = usecols)

country = "Italy"

# Filter the data for the specific "Area"
filtered_data = data[data["Area"] == country]

# Extract the "Year" and "Average Temperature (°C)" columns for the plot
years = filtered_data["Year"]
temperature = filtered_data["Average Temperature °C"]

# Create a line plot (you can also use scatter, bar, etc.)
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(years, temperature, marker='o', linestyle='-')
plt.title(f"Average Temperature in {country}")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)

# Show the plot or save it to a file
plt.show()
plt.savefig('plot.txt', format='txt')