#!/usr/bin/python3
"""Defines that multiplies two matrices with module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns multiplication of two matrices"""
    return (np.matmul(m_a, m_b))
