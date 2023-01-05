#!/usr/bin/env python3
"""a module 6-sum_mixed_list.py, with Complex types - mixed list"""
# python3 -c 'print(__import__("6-sum_mixed_list.py").__doc__)'
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.
    """
    # python3 -c 'print(__import__("6-sum_mixed_list.py").my_function.__doc__)'
    return sum(mxd_lst)
