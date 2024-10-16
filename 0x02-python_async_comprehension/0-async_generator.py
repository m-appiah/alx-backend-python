#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields a random float between 0 and 10.

    This generator will loop 10 times, each time asynchronously waiting for
    1 second before yielding a random number. This demonstrates the use of
    async/await syntax for asynchronous programming in Python, combined with
    the use of generators to yield values one at a time.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
