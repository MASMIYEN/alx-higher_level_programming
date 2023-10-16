#!/usr/bin/python3
"""Module for Rectangle unit tests."""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(10, 20, 5, 5, 1)

    def test_width(self):
        self.assertEqual(self.rect.width, 10)

    def test_height(self):
        self.assertEqual(self.rect.height, 20)

    def test_x(self):
        self.assertEqual(self.rect.x, 5)

    def test_y(self):
        self.assertEqual(self.rect.y, 5)

    def test_id(self):
        self.assertEqual(self.rect.id, 1)

    def test_area(self):
        self.assertEqual(self.rect.area(), 200)

    def test_display(self):
        expected_output = "\n" * 5 + (" " * 5 + "#" * 10 + "\n") * 20
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        expected_str = "[Rectangle], (1) 5/5 - 10/20"
        self.assertEqual(str(self.rect), expected_str)

    def test_update(self):
        self.rect.update(2, 15, 25, 10, 10)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 15)
        self.assertEqual(self.rect.height, 25)
        self.assertEqual(self.rect.x, 10)
        self.assertEqual(self.rect.y, 10)

    def test_update_kwargs(self):
        self.rect.update(id=2, width=15, height=25, x=10, y=10)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 15)
        self.assertEqual(self.rect.height, 25)
        self.assertEqual(self.rect.x, 10)
        self.assertEqual(self.rect.y, 10)

    def test_to_dictionary(self):
        expected_dict = {"id": 1, "width": 10, "height": 20, "x": 5, "y": 5}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
