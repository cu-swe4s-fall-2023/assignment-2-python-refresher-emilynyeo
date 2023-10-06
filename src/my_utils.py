import statistics
import math
import numpy as np


def get_column(file_name, query_column, query_value, result_column):
    """
    Extracts specifiec data of interest from CSV file.

    Args:
        file_name (str): The name of the CSV file to read.
        query_column (int): The index of column to check for the query_value.
        query_value (str): The value to match in the specified query_column.
        result_column (int): The index of column from which to extract data.

    Returns:
        list: A list of ints extracted from the result_column of matching rows.

    Raises:
        ValueError: If theres an issue converting an array into a float or int.
        FileNotFoundError: If the specified file_name does not exist.

    Example:
        If a CSV file 'Agrofood_co2_emission.csv' has the following content:
        ```
        Country, Fires, Population
        Jamaica, 25, 92.5
        South Africa, 30, 88.0
        Mozambique, 22, 95.5
        ```

        To extract the 'Fires' from 'Country' equal to 'South Africa',
        you can use this function as follows:
        ```
        result = get_column('Agrofood_co2_emission.csv', 0, 'South Africa', 1)
        # result will be [30]
        ```
    """
    result_array = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                line_array = line.split(",")

                # Check if query_column value matches query_value
                if len(line_array) > query_column and \
                        line_array[query_column] == query_value:
                    try:
                        fire_num = float(line_array[result_column])
                        fire_int = int(fire_num)
                        result_array.append(fire_int)
                    except ValueError:
                        print(f"messed up converting \
                            '{line_array[result_column]}' to float or int")

    except FileNotFoundError:
        print(f"Couldn't find the file '{file_name}'.")
        return None

    return result_array


def mean(array):
    """
    Extracts the mean from an array.

    Args:
        array: List of integers

    Returns:
        Mean of the array/list of integers.
    """
    if len(array) == 0:
        return None
    return sum(array)/len(array)


def median(array):
    """
    Extracts the median from an array

    Args:
        array: list of integers

    Returns:
        Median of the array/list of integers
    """
    if len(array) == 0:
        return None

    array = sorted(array)
    middle = (len(array) - 1) / 2

    if middle == int(middle):
        return array[int(middle)]

    option1 = math.floor(middle)
    option2 = math.ceil(middle)

    option1 = array[option1]
    option2 = array[option2]
    s = option1 + option2

    return s / 2


def std_dev(array):
    """
    Calculates the standard deviation of the array/list of integers.

    Args:
        array: list of integers

    Returns:
        Returns the standard deviation of the array/list of integers.
    """
    if len(array) < 2:
        return None

    s = 0
    m = mean(array)
    for x in array:
        dif = x - m
        s = s + dif*dif
    s = s/(len(array)-1)
    return math.sqrt(s)


def main():
    result = get_column('Agrofood_co2_emission.csv', 0, 'South Africa', 1)

    if result:
        print(f"Mean: {mean(result)}")
        print(f"Median: {median(result)}")
        print(f"Standard Deviation: {std_dev(result)}")


if __name__ == '__main__':
    main()
