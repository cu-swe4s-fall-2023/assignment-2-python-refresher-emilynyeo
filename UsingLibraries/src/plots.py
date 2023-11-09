import sys
import pandas as pd
import matplotlib.pyplot as plt

# read in the created datafile
sys.path.insert(0, '../')  # noqa
agro_gdp = pd.read_csv('data/co2_gdp_north.csv', sep='\t')

# Set your panel
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Line plot of Temperature change over Years
colors = {'United States of America': 'blue',
          'Mexico': 'orange',
          'Canada': 'green',
          'Guatemala': 'red'}

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

# Scatter plot of GDP vs Total Emissions
for country in agro_gdp['Area'].unique():
    country_data = agro_gdp[agro_gdp['Area'] == country]
    ax3.scatter(country_data['United States_GDP'],
                country_data['total_emission'],
                label=country,
                color=colors[country])

# Line plot of total population change over the Years
for country in agro_gdp['Area'].unique():
    country_data = agro_gdp[agro_gdp['Area'] == country]
    ax4.plot(country_data['Year'],
             country_data['total_population'],
             label=country,
             color=colors[country])

# Set titles and labels for all the plots
ax1.set_title('A. Temperature Change Over the Years')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Temperature °C')
ax1.legend()

ax2.set_title('B. Total Emissions Over the Years')
ax2.set_xlabel('Year')
ax2.set_ylabel('Total Emissions')
ax2.legend()

ax3.set_title('C. GDP vs Total Emissions')
ax3.set_xlabel('GDP (United States)')
ax3.set_ylabel('Total Emissions')
ax3.legend()

ax4.set_title('D. Total Population over the Years')
ax4.set_xlabel('Year')
ax4.set_ylabel('Total Population')
ax4.legend()

# Remove top and right borders
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('data/output_plots.png')
