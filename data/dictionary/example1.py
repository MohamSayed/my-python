# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:49:47 2020

@author: Naga
"""

from addict import Dict

class TaskDict(Dict):
    def __init__(self, *args, **kwargs):
        super(TaskDict, self).__init__(self, *args, **kwargs)
        # Avoid conflicts between dict key 'items' and dict method 'items'
        items = self.get('items', [])
        
    
task = TaskDict({"title": {'first name': 'John', 'last name': "X"}})
print("task", task)          
print("items", task.items())
print(task.get("title.'first name'"))




class SimpleClass(object):
    my_list = dict()
    name = ''
    obj = None
    def __init__(self, name, my_list, obj):
        self.name = name
        self.my_list = my_list
        self.obj = obj
        
    def funt(self):
        pass
        
simple_class = SimpleClass("John", {'a': 1, 'v': 2, 'c': 3}, task)


print(simple_class.__dict__)

# Remove
simple_dict = {"title": {'first name': 'John', 'last name': "X"}}
simple_dict.pop('title')
print(simple_dict)
print(len(simple_dict))

