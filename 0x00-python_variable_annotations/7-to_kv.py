#!/usr/bin/env python3
"""
This module contains the function to_kv that
takes a string k and an int OR float v as arguments
and returns a tuple. The first element of the tuple is
the string k, and the second element is the square of
the int/float v as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int/float, and returns a tuple.
    The first element is the string, and the second element
    is the square of the int/float as a float.

    Parameters:
    k (str): The string to be the first element of the tuple.
    v (Union[int, float]): The int or float to be squared and
    be the second element of the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the
    string k, and the second elementis the square of v as a float.
    """
    return (k, float(v**2))
