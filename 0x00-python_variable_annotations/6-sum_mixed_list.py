#!/usr/bin/env python3
"""
This module contains the function sum_mixed_list that takes a list of integers
and floats as argument and returns the sum of all numbers in the list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up all numbers in a list containing both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of all numbers in the list.
    """
    return sum(mxd_lst)
