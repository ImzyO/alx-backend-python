#!/usr/bin/python3
"""
a module 5-sum_list.py, with Complex types - list of floats"""
# python3 -c 'print(__import__("5-sum_list.py").__doc__)'
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    a type-annotated function sum_list which takes a list
    input_list of floats as argument and returns their sum as a float.
    """
    # python3 -c 'print(__import__("5-sum_list.py").my_function.__doc__)'
    return sum(input_list)
