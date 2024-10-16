#!/usr/bin/env python3
"""Type Checking
"""
from typing import List, Tuple, Union


def zoom_array(lst: Union[List[int], Tuple[int, ...]],
               factor: int = 2) -> List[int]:
    """
    Creates a new list by repeating each element in the
    input list or tuple a given number of times.

    Parameters:
    lst (Union[List[int], Tuple[int, ...]]): The input list or
    tuple of integers to be zoomed. factor (int, optional):
    The number of times each element in the input list or
    tuple should be repeated in the output list. Defaults to 2.

    Returns:
    List[int]: A new list where each element from the input list or
    tuple is repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
