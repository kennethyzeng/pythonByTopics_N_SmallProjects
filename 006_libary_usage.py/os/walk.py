"""
Python method walk() generates the file names in a directory tree by walking the tree either top-down or bo

https://www.tutorialspoint.com/python/os_walk.htm
https://www.geeksforgeeks.org/os-walk-python/
"""
# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))


#####