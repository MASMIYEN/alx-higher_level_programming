#!/usr/bin/python3
"""Module for Square unit tests"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    #  create a square with valid size, x, y and id parameters
    def test_create_square_with_valid_parameters(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    #  create a square with only size parameter
    def test_create_square_with_only_size_parameter(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    #  update a square with valid size, x, y and id parameters
    def test_update_square_with_valid_parameters(self):
        square = Square(5)
        square.update(2, 3, 4, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 1)

    #  update a square with only size parameter
    def test_update_square_with_only_size_parameter(self):
        square = Square(5)
        square.update(2)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    #  get the size of a square
    def test_get_square_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    #  set the size of a square
    def test_set_square_size(self):
        square = Square(5)
        square.size = 2
        self.assertEqual(square.size, 2)

    #  create a square with size = 0
    def test_create_square_with_zero_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    #  create a square with negative size
    def test_create_square_with_negative_size(self):
        with self.assertRaises(ValueError):
            square = Square(-5)

    #  create a square with size > 1 and x < 0
    def test_create_square_with_size_greater_than_one_and_negative_x(self):
        with self.assertRaises(ValueError):
            square = Square(5, -2)

    #  create a square with size > 1 and y < 0
    def test_create_square_with_size_greater_than_one_and_negative_y(self):
        with self.assertRaises(ValueError):
            square = Square(5, 2, -3)

    #  update a square with size = 0
    def test_update_square_with_zero_size(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(0)

    #  update a square with negative size
    def test_update_square_with_negative_size(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(-2)
