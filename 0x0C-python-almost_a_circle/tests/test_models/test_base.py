#!/usr/bin/python3
""" Module for Base tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    #  create an instance of Base with no arguments and check that id is incremented by 1
    def test_create_instance_no_arguments(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    #  create an instance of Base with an argument and check that id is set correctly
    def test_create_instance_with_argument(self):
        base = Base(5)
        self.assertEqual(base.id, 5)

    #  call to_json_string with a list of dictionaries and check that the output is a JSON string
    def test_to_json_string(self):
        base1 = Base(1)
        base2 = Base(2)
        dict_list = [base1.to_dictionary(), base2.to_dictionary()]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')

    #  call save_to_file with a list of objects and check that a file with
    #  the correct name is created and contains the correct JSON string
    def test_save_to_file(self):
        base1 = Base(1)
        base2 = Base(2)
        dict_list = [base1.to_dictionary(), base2.to_dictionary()]
        Base.save_to_file([base1, base2])
        with open("Base.json", "r") as file:
            json_string = file.read()
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')

    #  call from_json_string with a JSON string and check that the output is a list of dictionaries
    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        dict_list = Base.from_json_string(json_string)
        self.assertEqual(dict_list, [{"id": 1}, {"id": 2}])

    #  call create with a dictionary and check that the output is an instance of the
    #  correct class with the correct attributes
    def test_create(self):
        dictionary = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        rectangle = Base.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    #  call to_json_string with an empty list and check that the output is "[]"
    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    #  call from_json_string with an empty string and check that the output is an empty list
    def test_from_json_string_empty_string(self):
        dict_list = Base.from_json_string("")
        self.assertEqual(dict_list, [])

    #  call from_json_string with None and check that the output is an empty list
    def test_from_json_string_none(self):
        dict_list = Base.from_json_string(None)
        self.assertEqual(dict_list, [])

    #  call create with an empty dictionary and check that the output is an instance
    #  of the correct class with default attributes
    def test_create_empty_dictionary(self):
        dictionary = {}
        rectangle = Base.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 1)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    #  call load_from_file with a non-existent file and check that the output is an empty list
    def test_load_from_file_non_existent_file(self):
        obj_list = Base.load_from_file()
        self.assertEqual(obj_list, [])

    #  call load_from_file_csv with a non-existent file and check that the output is an empty list
    def test_load_from_file_csv_non_existent_file(self):
        obj_list = Base.load_from_file_csv()
        self.assertEqual(obj_list, [])
