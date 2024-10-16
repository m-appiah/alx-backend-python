#!/usr/bin/env python3
"""
Measures the total runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
from time import perf_counter
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.

    This coroutine uses asyncio.gather to run multiple
    instances of async_comprehension concurrently.
    It measures the start and end time to calculate the total runtime.

    Returns:
        float: The total runtime of executing async_comprehension
        four times in parallel.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return perf_counter() - start_time
