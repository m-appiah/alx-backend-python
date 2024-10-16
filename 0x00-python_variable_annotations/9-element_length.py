#!/usr/bin/env python3
"""
Annotates function params and return values
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence from the iterable and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing
    a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
