#!/usr/bin/python3
"""Module for Base unit tests."""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_incrementing_id(self):
        # Test if ids are incremented correctly
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id(self):
        # Test if custom id is set correctly
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_to_json_string(self):
        # Test if to_json_string method returns a valid JSON string
        base = Base()
        json_string = Base.to_json_string([base.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_from_json_string(self):
        # Test if from_json_string method converts JSON string to list of dictionaries
        json_string = '[{"id": 1}]'
        objects = Base.from_json_string(json_string)
        self.assertEqual(objects, [{"id": 1}])

    def test_create(self):
        # Test if create method creates an instance with given dictionary attributes
        dictionary = {"id": 1}
        base = Base.create(**dictionary)
        self.assertEqual(base.id, 1)

    def test_draw(self):
        # Test the draw method (this might require manual inspection)
        # Just check if it runs without errors for simplicity
        list_rectangles = []  # Provide a list of rectangles for testing
        list_squares = []     # Provide a list of squares for testing
        Base.draw(list_rectangles, list_squares)

if __name__ == '__main__':
    unittest.main()
