#!/usr/bin/env python3
"""
This module contains the function safely_get_value.
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value for a given key from a dictionary.
    If the key does not exist, returns a default value.

    Parameters:
    dct (Mapping): The dictionary from which to retrieve the value.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None], optional): The default value
    to return if the key is not found. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key in the
    dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
