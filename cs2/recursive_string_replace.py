# -*- coding: utf-8 -*-
'''Recursive find and replace of string variables


A recursive method that takes 1) a string to find, 2) a string to replace
the found string with, and 3) an initial string. Return the initial string with
all the found strings replaced with the replacement string. Without using loops
or the built-in string methods except comparison, length, and slicing.


Author: Larsen Close
Version: Completed through A level work
Outline and initial tests provided in class by Professor Dr. Beaty at MSU Denver


Todo:
    * Make runnable from file
    * Also also use ``sphinx.ext.todo`` extension
'''


def findandreplace(find, replace, string):
    '''
    Replace all instances of find with replace in string.

    Recursive approach:
    If the string starts with find
        return replace and call findandreplace with the rest of the string
    else
        return the first character of the string and call findandreplace
        with the rest of the string
    '''
    if find:
        a = len(find)
    if string == "":
        return ""
    if string is None:
        return None
    if string == find:
        return replace
    if replace is None:
        return string
    if find and string[:a] == find:
        return replace + findandreplace(find, replace, string[a:])
    else:
        return string[0] + findandreplace(find, replace, string[1:])
