#!/usr/bin/env bash
"""a module 1-concat.py, with basic annotations for concatneations"""
# python3 -c 'print(__import__("1-cocncat.py").__doc__)'

def concat(str1: str, str2: str) -> str:
    """
    a type-annotated function concat that takes a string str1
    and a string str2 as arguments and returns a concatenated string
    """
    #python3 -c 'print(__import__("1-concat.py").my_function.__doc__)' and python3 -c
    return str1 + str2
