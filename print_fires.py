#Savanna Fires = 3
#Forest Fires = 4
#Fires in organic soils = 21
#Fire in humid tropic forests = 22

from my_utils import *

country='South Africa'
county_column = 1
file_name = 'Agrofood_co2_emission.csv'

savanna_fires = get_column("Agrofood_co2_emission.csv",0,"South Africa",3)
forest_fires = get_column("Agrofood_co2_emission.csv",0,"South Africa",4)
organic_soils_fires = get_column("Agrofood_co2_emission.csv",0,"South Africa",22)
humid_tropic_fires = get_column("Agrofood_co2_emission.csv",0,"South Africa",23)

number_of_fires = 0

for fire in savanna_fires:
    number_of_fires = number_of_fires + float(fire)

for fire in forest_fires:
    number_of_fires = number_of_fires + float(fire) 
    
for fire in organic_soils_fires:
    number_of_fires = number_of_fires + float(fire) 

for fire in humid_tropic_fires:
    number_of_fires = number_of_fires + float(fire)

print(number_of_fires)




