# -*- coding: utf-8 -*-
"""Created on Thu Feb  6 21:09:29 2020.

@author: Naga
"""

import logging


# logging.basicConfig(level=logging.DEBUG, format="basic config => [%(asctime)s]:%(levelname)s:%(name)s:%(module)s:%(funcName)s: %(message)s")

def add_numbers(x, y):
    return x + y

add_numbers(1, 9)
# logging.debug("Adding numbers")


# Advanced logging: logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_handler = logging.FileHandler("test.log")
log_formatter = logging.Formatter("Advanced => [%(asctime)s]:%(levelname)s:%(name)s:%(module)s:%(funcName)s: %(message)s")
log_file_handler.setFormatter(log_formatter)
## Output to terminal
log_stream = logging.StreamHandler()
### You can alos specify different 
### formatter for different streams
log_stream.setFormatter(log_formatter)
logger.addHandler(log_file_handler)
logger.addHandler(log_stream)


add_numbers(1, 9)
logger.debug("adding numbers")
