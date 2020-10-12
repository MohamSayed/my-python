# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:21:43 2020

@author: Naga
"""

class Test():
    pass

test = Test()

print(hasattr(test, '__new__'))

my_str = "String"
print(hasattr(my_str, '__new__'))