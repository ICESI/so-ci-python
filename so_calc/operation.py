"""
Script with operation methods
"""
import numpy as np


def add(val_a, val_b):
    """
    Sum two values
    """
    ans = val_a + val_b
    return ans


def add_numpy(num_list):
    """
    Sum list values
    """
    ans = np.sum(num_list)
    return ans
