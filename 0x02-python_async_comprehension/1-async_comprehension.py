#!/usr/bin/env python3
"""
An asynchronous comprehension that collects 10 random numbers generated by an
async generator.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers generated by an async generator
    without using async comprehension.

    This coroutine manually iterates over the async_generator function,
    collecting 10 random float numbers between 0 and 10.
    It demonstrates handling asynchronous iteration explicitly,
    providing an alternative to async comprehensions.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
