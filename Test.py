#! /usr/bin/python3
# Test cases for adding 2 numbers
import unittest

from Prog import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [23,32]
        result = summation(data)
        self.assertEqual(result,55)

if __name == '__main__':
    unittest.main()
