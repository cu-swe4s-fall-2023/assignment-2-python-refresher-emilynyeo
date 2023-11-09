import sys
import seaborn as sns
import pandas as pd
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

# read in the created datafile
sys.path.insert(0, '../')  # noqa
agro_gdp = pd.read_csv('data/co2_gdp_north.csv', sep='\t')

# Set your panel
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Line plot of Temperature change over the Years
colors = {'United States of America': 'blue', 'Mexico': 'orange', 'Canada': 'green', 'Guatemala': 'red'}
for country in agro_gdp['Area'].unique():
    country_data = agro_gdp[agro_gdp['Area'] == country]
    ax1.plot(country_data['Year'], 
        country_data['Average Temperature °C'], 
        label=country, 
        color=colors[country])

# Scatter plot of emissions over the years
for country in agro_gdp['Area'].unique():
    country_data = agro_gdp[agro_gdp['Area'] == country]
    ax2.scatter(country_data['Year'], 
    	country_data['total_emission'], 
    	label=country, 
    	color=colors[country])

# Set titles and labels for all the plots 
ax1.set_title('Temperature Change Over the Years')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Temperature °C')
ax1.legend()

ax2.set_title('Total Emissions Over the Years')
ax2.set_xlabel('Year')
ax2.set_ylabel('Total Emissions')
ax2.legend()

# Remove top and right borders
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('output_plots.png')
plt.show()

# Plot B: Scatter plot of Year vs Emissions


# Plot C: Scatter plot of GDP vs Emissions


# Plot D: Line plot of Year, Emissions, Temp and Population


# Create 4 panel output file
