#!/usr/bin/python3
""" Module for Rectangle unit tests """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    #  create a rectangle with valid width, height, x, y and id
    def test_create_rectangle_with_valid_attributes(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    #  update rectangle attributes using update method with valid arguments
    def test_update_rectangle_attributes_with_valid_arguments(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(2, 8, 12, 4, 6)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 6)
        self.assertEqual(rectangle.id, 2)

    #  get rectangle area using area method
    def test_get_rectangle_area(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.area(), 50)

    #  get rectangle attributes using to_dictionary method
    def test_get_rectangle_attributes_as_dictionary(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        attributes = rectangle.to_dictionary()
        self.assertEqual(attributes['width'], 5)
        self.assertEqual(attributes['height'], 10)
        self.assertEqual(attributes['x'], 2)
        self.assertEqual(attributes['y'], 3)
        self.assertEqual(attributes['id'], 1)

    #  display rectangle using display method
    def test_display_rectangle(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_output = ("\n\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  "
                           "#####\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    #  convert rectangle to string using __str__ method
    def test_convert_rectangle_to_string(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle], (1) 2/3 - 5/10"
        self.assertEqual(str(rectangle), expected_output)

    #  create a rectangle with width or height equal to 0
    def test_create_rectangle_with_zero_width_or_height(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 2, 3, 1)

    #  create a rectangle with negative width or height
    def test_create_rectangle_with_negative_width_or_height(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3, 1)

    #  create a rectangle with negative x or y
    def test_create_rectangle_with_negative_x_or_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 1)

    #  update rectangle attributes using update method with invalid arguments
    def test_update_rectangle_attributes_with_invalid_arguments(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(TypeError):
            rectangle.update(2, "8", 12, 4, 6)
        with self.assertRaises(ValueError):
            rectangle.update(2, -8, 12, 4, 6)

    #  display rectangle with x or y greater than 0
    def test_display_rectangle_with_x_or_y_greater_than_zero(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_output = ("#####\n    #####\n    #####\n    #####\n    #####\n    #####\n    #####\n    #####\n    "
                           "#####\n    #####\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    #  create a rectangle with default id
    def test_create_rectangle_with_default_id(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.id, None)
