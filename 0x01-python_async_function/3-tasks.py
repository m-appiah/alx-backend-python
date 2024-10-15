#!/usr/bin/env python3
"""
A module for creating asyncio Tasks that run asynchronous functions.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task from the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: The task created from the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
