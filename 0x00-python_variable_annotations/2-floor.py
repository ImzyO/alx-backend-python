#!/usr/bin/env bash
"""
a module 2-floor.py, with basic annotations 
floor from the math in built module
"""
# python3 -c 'print(__import__("2-floor.py").__doc__)'
import math

def floor(n: float) -> int:
    """
    a type-annotated function floor which takes a float,
    n as argument and returns the floor of the float.
    """
    # python3 -c 'print(__import__("2-floor.py").my_function.__doc__)' and python3 -c
    return math.floor(n)
