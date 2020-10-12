# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:36:26 2020

@author: Naga
"""

# Format map
my_dict = {"title": "Cairo", "address": {'apt': 19, 'floor': 1}}
formatted_string = "my title is {title} and my address is {address[apt]}".format_map(my_dict)
print(formatted_string)