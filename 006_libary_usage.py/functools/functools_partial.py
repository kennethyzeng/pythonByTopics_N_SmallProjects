#! usr/bin/local/python3

from functools import partial 

def multiply(x, y): 
    return x*y 

double =partial(multiply, 3)  #double is address 
print(double(4))