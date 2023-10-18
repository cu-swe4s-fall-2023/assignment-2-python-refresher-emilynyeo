# Assignment 2,3 and 4

This repository has been used over the weeks to learn about best coding practices, unit and functional tests, writing funtions, opening and closing files, file paths and much more. Below is an outline of the directories and files included, and how they have changed over time. 

### src
This contains the main code files, excluding data and tests. These files must be run from this directory. 

- **my_utils.py** : Includes definitions of functions and their intended usage. Details of the functions explicitly outlined using docstring. Try and except statements added, with errors specified for file not found and errors converting arrays to floats or integers. And a main function was specified. 

- **print_fires.py**: A script that utilizes functions defined in my_utils.py. 

- **run.sh**: A bash script to submit and run print_fires.py with examples of what will and wont work specified. 

### test
This directory contains the unit and functional tests for the files in the src. This also contains test data. Each of these files should be run from the directory in which they are located. 

	- **/data/Agro2_co2_subset.csv** : Example test file on which functional tests can be run.
  
	- **/unit/test_my_utils.py** : A file containing unit tests for each of the functions in my_utils.py. Includes randomness and positive and negative test cases. 
  
	- **/function/test_print_fires.sh** : A bash script using the Stupid Simple Bash Testing framework to  for print_fires.py using a test file. 

- ### .github/workflow/
This continuous integration folder was created and an initial workflow for 
branch pushes and pull requests was made in `a5.yaml`.