#!/usr/bin/env python3
"""
an async routine called wait_n that takes
in 2 int arguments (in this order)
"""
import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines at the same time with async"""
    todos = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await todo for todo in asyncio.as_completed(todos)]
