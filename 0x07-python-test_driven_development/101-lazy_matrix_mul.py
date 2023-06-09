#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defining matrix multiplication function using PyNum"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two matrices

    Args:
        m_a (list of lists of ints/floats): First matrix
        m_b (list of lists of ints/floats): Second matrix
    """

    return (np.matmul(m_a, m_b))
