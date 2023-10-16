#!/usr/bin/python3
"""Module for Square unit tests."""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(10, 5, 5, 1)

    def test_size(self):
        self.assertEqual(self.square.size, 10)

    def test_x(self):
        self.assertEqual(self.square.x, 5)

    def test_y(self):
        self.assertEqual(self.square.y, 5)

    def test_id(self):
        self.assertEqual(self.square.id, 1)

    def test_area(self):
        self.assertEqual(self.square.area(), 100)

    def test_display(self):
        expected_output = "\n" * 5 + (" " * 5 + "#" * 10 + "\n") * 10
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        expected_str = "[Square] (1) 5/5 - 10"
        self.assertEqual(str(self.square), expected_str)

    def test_update(self):
        self.square.update(2, 15, 10, 10)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 15)
        self.assertEqual(self.square.x, 10)
        self.assertEqual(self.square.y, 10)

    def test_update_kwargs(self):
        self.square.update(id=2, size=15, x=10, y=10)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 15)
        self.assertEqual(self.square.x, 10)
        self.assertEqual(self.square.y, 10)

    def test_to_dictionary(self):
        expected_dict = {"id": 1, "size": 10, "x": 5, "y": 5}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
