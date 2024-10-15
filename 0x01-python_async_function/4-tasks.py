#!/usr/bin/env python3
"""
A module for creating and running multiple asyncio Tasks concurrently.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `n` instances of `task_wait_random` concurrently,
    each with a `max_delay`.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay (in seconds) for `task_wait_random`.

    Returns:
        List[float]: A list of float values representing the
        delays experienced by each task,
        sorted in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
