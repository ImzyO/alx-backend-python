#!/usr/bin/env python3
"""
a function (do not create an async function, use the regular function syntax to
"""

import time
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """tasks"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
