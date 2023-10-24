# Exploring changes in Populations and Temperatures in Southern Africa. 

One might consider an area with a more urban population as more detrimental to the environment than rural areaa, as modern transport, food packaging and household consumption is generally greater in these populations. However, rural populations usually have more intensive agriculture practices with their own environmental foes ...  
This analysis seaks to identify the shifts between urban and rural populations over the years in Southern Africa, as well as assess correlated changes in CO2 emissions and temperature changes. 

## Results 

- 1. The plots below show the changes in population trends over the years in each of the countries bordering South Africa. As you can see, there has been a rise in Urban population numbers (red) across all 4 countries and a rise in rural populations (green) for all except Botswana (bottom right). 

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <img src="/doc/Namibia_py.png" alt="Image 1" style="width: 40%; margin: 2px;">
  <img src="/doc/Lesotho_py.png" alt="Image 2" style="width: 40%; margin: 2px;">
  <img src="/doc/Mozambique_py.png" alt="Image 3" style="width: 40%; margin: 2px;">
  <img src="/doc/Botswana_py.png" alt="Image 4" style="width: 40%; margin: 2px;">
</div>

- 2. The plots below show the change in CO2 emission and average annual temperature changr for each of the countries. There seems to have been a rise in emissions and temperature in recent years. 

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <img src="/doc/Namibia_pt.png" alt="Image 1" style="width: 40%; margin: 2px;">
  <img src="/doc/Lesotho_pt.png" alt="Image 2" style="width: 40%; margin: 2px;">
  <img src="/doc/Mozambique_pt.png" alt="Image 3" style="width: 40%; margin: 2px;">
  <img src="/doc/Botswana_pt.png" alt="Image 4" style="width: 40%; margin: 2px;">
</div>

- 3. The plots below show how the changes in population trends correlate to changes in annual temperature changes:

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <img src="/doc/Namibia_ty.png" alt="Image 1" style="width: 40%; margin: 2px;">
  <img src="/doc/Lesotho_ty.png" alt="Image 2" style="width: 40%; margin: 2px;">
  <img src="/doc/Mozambique_ty.png" alt="Image 3" style="width: 40%; margin: 2px;">
  <img src="/doc/Botswana_ty.png" alt="Image 4" style="width: 40%; margin: 2px;">
</div>


## Methods and Usage:

- Input:
	- A CSV file containing the data for use. This assignment used Agrofood_co2_emission.csv from https://drive.google.com/drive/folders/15dnNnOEjDZDvwzM-_tGGtWjTbNL669i7?usp=drive_link

- Clone the repository using `git clone <this repo>`
	- Ensure python, wget and snakemake are installed on your device too. The snakefile requires python3 to run. 

- Run the snakefile from the src directory
	- The figures of this analysis were created by running `snakemake -c1`, which runs all the rules. Descriptions of the files utilized by snakemake are included under the src section below. 

	**note**: Should you run this same analysis on seperate countries, simply include them to the names listed in the first line of the snakefile and rerun it. 


This is very much a work in progress, as this repository has also been used over the weeks to learn about best coding practices, unit and functional tests, writing funtions, opening and closing files, file paths and much more. Below is an outline of the directories and files included, and how they have changed over time. 

### src
This contains the main code files, excluding data and tests. These files must be run from this directory. 

- **snakefile** : a workflow to create the analysis figures. The expectation is that snakemake and python 3 are installed. It utilizes the script below:  

  - **plot_temp_years.py** 
  - **trends_pt.py**
  - **pop_years.py**

- **my_utils.py** : Includes definitions of functions and their intended usage. Details of the functions explicitly outlined using docstring. Try and except statements added, with errors specified for file not found and errors converting arrays to floats or integers. And a main function was specified. 

- **print_fires.py**: A script that utilizes functions defined in my_utils.py. This can be run from the src directory using 

- **run.sh**: A bash script to submit and run print_fires.py with examples of what will and wont work specified. 

### test
This directory contains the unit and functional tests for the files in the src. This also contains test data. Each of these files should be run from the directory in which they are located. 

- **/data/Agro2_co2_subset.csv** : Example test file on which functional tests can be run.
  
- **/unit/test_my_utils.py** : A file containing unit tests for each of the functions in my_utils.py. Includes randomness and positive and negative test cases. This can be run by using `python -m unittest unit/test_my_utils.py` from the test directpry.
  
- **/function/test_print_fires.sh** : A bash script using the Stupid Simple Bash Testing framework to  for print_fires.py using a test file. This can be tested by running `bash func/test_print_fires.sh` from the test directory.

- ### .github/workflow/
This continuous integration folder was created and an initial workflow for 
branch pushes and pull requests was made in `a5.yaml`. The following will occur every time a branch is pushed or a pull request is made:

	- Unit tests will be run.

    - Functional tests will be run.

    - Style checks will be run using pycodestyle and PEP8.
