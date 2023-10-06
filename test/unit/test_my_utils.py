import unittest
import statistics
import math
import os
import random
import numpy as np
from my_utils import *
sys import

sys.path.insert(0, 'ls ../../src') #noqa

#  To test this file: python -m unittest test_my_utils.py


class TestMyUtils(unittest.TestCase):

    def setUp(self):
        self.file_name = 'test_data.csv'
        try:
            with open(self.file_name, 'w') as file:
                file.write("Country, Fires, Population\n")
                file.write("Jamaica, 25, 92.5\n")
                file.write("South Africa, 30, 88.0\n")
                file.write("Mozambique, 22, 95.5\n")
        except FileNotFoundError:
            pass

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_get_column(self):
        result = get_column(self.file_name, 0, 'South Africa', 1)
        self.assertEqual(result, [30])

    def test_should_fail(self):
        self.assertEqual(get_column("wrong_name", 2, "SA", 3), None)

    def test_median(self):
        result = []
        for i in range(10):
            random_integer = random.randrange(1, 10)
            result.append(random_integer)
        self.assertEqual(median(result), statistics.median(result))
        self.assertEqual(median([]), None)

    def test_mean(self):
        result = []
        for i in range(10):
            random_integer = random.randrange(1, 10)
            result.append(random_integer)
        self.assertEqual(mean(result), statistics.mean(result))
        self.assertEqual(mean([]), None)

    def test_std_dev(self):
        result = []
        for i in range(10):
            random_integer = random.randrange(1, 10)
            result.append(random_integer)
        self.assertTrue(abs(std_dev(result) - statistics.stdev(result)) <= 0.5)
        self.assertEqual(std_dev([]), None)


if __name__ == '__main__':
    unittest.main()
