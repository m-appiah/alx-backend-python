#!/usr/bin/env python3
"""
This module contains the function sum_list that takes a list of float numbers
as argument and returns the sum of all float numbers in the list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up all float numbers in a list and returns the total.

    Parameters:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of all float numbers in the list.
    """
    return sum(input_list)
