import sys
import pandas as pd
import matplotlib.pyplot as plt


#data_file = sys.argv[1]
#out_file = sys.argv[2]
#title = sys.argv[3]
#x=sys.argv[4]
#y=sys.argv[5]

countries = sys.argv[1:-2]
input_files = sys.argv[-2].split()
output_file = sys.argv[-1]  # Split the last argument into a list of countries

# Define colors for each country
colors = ['b', 'g', 'r', 'c']

# Create a plot for each country
for i, (input_file, country) in enumerate(zip(input_files, countries)):
    country_data = pd.read_csv(input_file, sep='\t')
    plt.plot(country_data['Year'], country_data['Temperature'], label=f'{country}', color=colors[i])

# Customize the plot
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature Changes Over the Years')
plt.legend()

# Save the plot to the output file
plt.savefig(output_file)

#D = []
#for l in open(data_file):
#    D.append(float(l))

#fig, ax = plt.subplots()
#ax.hist(D)
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
#ax.set_xlabel(x)
#ax.set_ylabel(y)
#ax.set_title(title)

#plt.savefig(out_file,bbox_inches='tight')
