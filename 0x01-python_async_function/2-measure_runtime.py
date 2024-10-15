#!/usr/bin/env python3
"""
A module for asynchronous tasks using asyncio.
"""

import asyncio
import time
from 1-concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n coroutine and
    returns the average time per call.

    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay argument for wait_n.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(asyncio.run(measure_time(n, max_delay)))
