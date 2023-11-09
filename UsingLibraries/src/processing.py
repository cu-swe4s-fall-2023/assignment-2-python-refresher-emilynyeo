import numpy as np
import pandas as pd
import sys
from scipy import stats

sys.path.insert(0, '../')  # noqa

# import data
co2 = pd.read_csv('data/Agrofood_co2_emission.csv')
gdp = pd.read_csv('data/IMF_GDP.csv')

# replace NA values
gdp = gdp.replace('...', None)
gdp = gdp.replace('-', None)

# remove ',' from numbers


def destroy_commas(x):
    if x is None:
        return None
    return float(x.replace(',', ''))


for col in gdp.columns:
    if col == 'Country':
        continue
    gdp[col] = gdp[col].apply(destroy_commas)


# getting only countries of interest
co2_north = co2[co2['Area'].isin(['Mexico',
                                  'Guatemala',
                                  'United States of America',
                                  'Canada'])]
gdp_north = gdp[gdp['Country'].isin(['United States',
                                     'Mexico',
                                     'Canada',
                                     'Guatemala'])]


# Getting only columns of interest
co2_n = co2_north[['Area', 'Year', 'Average Temperature °C',
                   'total_emission', 'Total Population - Female',
                   'Total Population - Male']]

co2_nc = co2_n.copy()

# Create a new total population column
co2_nc['total_population'] = co2_nc['Total Population - Female'] +
co2_nc['Total Population - Male']


# transpose gdp data to make it mergable to co2_n
gdp_n = gdp_north.T.reset_index()
gdp_n.columns = ['Year', 'Canada_GDP',
                 'Guatemala_GDP', 'Mexico_GDP',
                 'United States_GDP']
gdp_nr = gdp_n.iloc[1:, :]  # remove 1st row

# dealing with mismatched types:
gdp_nrc = gdp_nr.copy()
gdp_nrc['Year'] = gdp_nrc['Year'].astype('int64')

agro_gdp = pd.merge(co2_nc, gdp_nrc,
                    how='inner',
                    left_on='Year',
                    right_on='Year')

# save needed data to a new file to add 
agro_gdp.to_csv('data/co2_gdp_north.csv', sep='\t', index=False)
