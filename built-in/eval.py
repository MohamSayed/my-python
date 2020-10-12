# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 01:52:54 2020

@author: Naga
"""

class Test():
    name = ''
    def __init__(self, name):
        self.name = name
        

obj = eval("Test('boo')")
print(obj.name)

no_obj = None

try:
    eval("Test2('foo')")
except Exception as e:
    print(e)
print("passed")