# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:10:22 2020

@author: Naga
"""

class FirstException(Exception):
    pass
        


try:
    raise FirstException
except FirstException as e:
    raise e
            
finally:
    pass
