# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:18:40 2020

@author: Naga
"""

from queue import Queue
import threading

from time import sleep


class CustomQueue(Queue):
    closed = False
    def __init__(self):
        Queue.__init__(self)
        
    def close(self):
        self.closed = True

cq = CustomQueue()

def add_to_queue(q):
    for i in range(5):
        q.put(i)
        sleep(1)


thread = threading.Thread(target=add_to_queue, args=(cq,), daemon=True)
thread.start()


for job in iter(cq.get, None): # Replace `None` as you need.
    print(job)
