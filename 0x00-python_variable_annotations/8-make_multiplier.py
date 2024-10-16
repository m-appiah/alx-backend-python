#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by a given multiplier.

    Parameters:
    multiplier (float): The multiplier to apply in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
    it multiplied by the multiplier.
    """
    return lambda x: x * multiplier
