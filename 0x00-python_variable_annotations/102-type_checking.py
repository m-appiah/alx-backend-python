#!/usr/bin/env python3
"""Type Checking
"""
from typing import List, Tuple, Union


def zoom_array(lst: Union[List[int], Tuple[int, ...]],
               factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Corrected the type of `array` to be explicitly a list or a tuple
# of integers and adjusted the function call accordingly.
array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

# Corrected the type of the factor argument to be an integer.
zoom_3x = zoom_array(array, 3)
