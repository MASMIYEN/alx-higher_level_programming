# The ``100-matrix_mul`` module
from jsonschema._keywords import required
===============================
How to 100-matrix_mul.py
===============================

The module defines one function
``matrix_mul`` multiplies 2 matrices i mean matrix*

Usage
=====

Importing function from module:
>>> matrix_mul = __import__("100-matrix_mul").matrix_mul

Testing regular arguments:
>>> matrix_mul([[1, 1], [1, 1]], [[2, 2], [2, 2]])
[[4, 4], [4, 4]]

Testing m_a string:
>>> matrix_mul("alx", [[1, 1], [1, 1]])
Traceback (most recent call last):
TypeError: m_a must be a list

Testing m_b string:
>>> matrix_mul([[1, 1], [1, 1]], "alx")
Traceback (most recent call last):
TypeError: m_b must be a list

Testing m_a list of integers:
>>> matrix_mul([1, 2, 3, 4], [[1, 1], [1, 1]])
Traceback (most recent call last):
TypeError: m_a must be a list of lists

Testing m_b list of integers:
>>> matrix_mul([[1, 1], [1, 1]], [1, 2, 3, 4])
Traceback (most recent call last):
TypeError: m_b must be a list of lists

Testing m_a empty:
>>> matrix_mul([[]], [[1, 1], [1, 1]])
Traceback (most recent call last):
ValueError: m_a can't be empty

Testing m_b empty:
>>> matrix_mul([[1, 1], [1, 1]], [[]])
Traceback (most recent call last):
ValueError: m_b can't be empty

Testing m_a list of lists of not number:
>>> matrix_mul([['a', 'b'], ['c', "ddd"]], [[1, 1], [1, 1]])
Traceback (most recent call last):
TypeError: m_a should contain only integers or floats

Testing m_b list of lists of not number:
>>> matrix_mul([[1, 1], [1, 1]], [['a', 'b'], ['c', "ddd"]])
Traceback (most recent call last):
TypeError: m_b should contain only integers or floats

Testing m_a list of lists of number various size:
>>> matrix_mul([[1, 1], [1, 1, 1]], [[2, 2], [2, 2]])
Traceback (most recent call last):
TypeError: each row of m_a must be of the same size

Testing m_b list of lists of number various size:
>>> matrix_mul([[1, 1], [1, 1]], [[2, 2, 2], [2, 2]])
Traceback (most recent call last):
TypeError: each row of m_b must be of the same size

Testing m_b list of number but not correct:
>>> matrix_mul([[2, 2, 2], [2, 2, 2]], [[1, 1], [1, 1]])
Traceback (most recent call last):
ValueError: m_a and m_b cannot be multiplied

Testing missing one argument:
>>> matrix_mul([[1, 1]])
Traceback (most recent call last):
TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

Testing no arguments:
>>> matrix_mul()
Traceback (most recent call last):
TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'