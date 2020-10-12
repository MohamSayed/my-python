# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:05:03 2020

@author: Naga
"""

import dpath.util

x = {
    "a": {
        "b": {
        "3": 2,
        "43": 30,
        "c": [],
        "d": ['red', 'buggy', 'bumpers'],
        }
    }
}
 
       
# search
print("\nSearch result:{}".format(dpath.util.search(x, "a/b/[cd3x]")))

print("\nget res: {}".format(dpath.util.get(x, "a/b/d")))

# Update
print("\nUpdate result code: {}".format(dpath.util.set(x, "a/b/c", "my value", )))
print(x)

print(dpath.util.get(x, 'a.b.43', separator='.'))
        