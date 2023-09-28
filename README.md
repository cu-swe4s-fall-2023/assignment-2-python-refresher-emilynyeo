[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# first commit

Completed the implementation of get_column() in my_utils.py such that
a. get_column() opened the file named file_name and processed it line by line
b. for each line
	i. split the line into an array.
	ii. checked to see if the value in the query_column position of the array matches the value stored in the query_value variable.
	iii. when the above condition was met, added the value in the result_column position to an array.
c. returned the array storing the column values.

# second commit 

Updated print_fires.py to correctly use get_column() to print the number of fires in South Africa (added all 4 fire types together). 

made an sh file to run print_fires.py

# for assignmemt 3, the files were changed the following ways:

1. To my_utils.py:
	- details of the function get_column were explicitly outlined using docstring. 
	- try and except statements added, with errors specified for file not found and errors converting arrays to floats or integers.
	- a main function was specified.

2. To print_fires.py
	- argparse was used to add parser arguments of interest. Including:
		- '--country': Which is where you would specify the country you are interested in
		- '--country_column': The column index of the country
		- '--fires_column': The column index of the number of fires
		- '--file_name': The name of the data file being inspected

3. To run.sh
	 - Updated the file to run the print_fires.py script with:
	 	- an exampple that does work
	 	- two example that do not work