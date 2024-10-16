#!/usr/bin/env python3
"""
Module for 100-safe_first_element.py
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence of any type of elements.

    Returns:
    Union[Any, None]: The first element of the sequence if it
    exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
