#!/usr/bin/python3
"""Defines function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """returns new matrices with result"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(
            (isinstance(n, (float, int)))
            for n in [e for r in m_a for e in r]
    ):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
            (isinstance(n, (float, int)))
            for n in [e for r in m_b for e in r]
    ):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[0 for i in m_b[0]] for j in m_a]
    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                new_matrix[x][y] += m_a[x][z] * m_b[z][y]

    return new_matrix
