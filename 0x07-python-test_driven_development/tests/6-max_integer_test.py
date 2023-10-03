#!/usr/bin/python3
"""Unittests to check max_integer()"""

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test class defining test cases for max_integer()
    """
    def test_max_end(self):
        """Tests max at end"""
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_start(self):
        """test max at the beginning"""
        test_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_middle(self):
        """test max in the middle"""
        test_list = [2, 3, 5, 4, 1]
        self.assertEqual(max_integer(test_list), 5)

    def test_one_negative(self):
        """tests one negative number in list"""
        test_list = [-1, 1, 2, 3]
        self.assertEqual(max_integer(test_list), 3)

    def test_only_negative(self):
        """tests only negative numbers in list"""
        test_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), -1)

    def test_one_element(self):
        """tests list of one element"""
        test_list = [5]
        self.assertEqual(max_integer(test_list), 5)

    def test_empty_list(self):
        """tests empty list"""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

if __name__ == '__main__':
    unittest.main()
