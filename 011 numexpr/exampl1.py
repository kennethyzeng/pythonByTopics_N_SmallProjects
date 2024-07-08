import numexpr as ne 
import numpy as np 
import timeit
loops = 2500000
a = np.arange(1, loops)
ne.set_num_threads(1)
f = '3*log(a) + cos(a) **2'
r =ne.evaluate(f)
print(r)

###faster when set the multiple thread 
ne.set_num_threads(4)  #set 4 thread 
r=ne.evaluate(f)
print(r)