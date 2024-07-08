"""
hassattr() 
try/except
"""
##example of missing attribute
import timeit 
s = """
try: 
    str.__bool__
except AttributeError:
    pass 
"""
t=timeit.timeit(stmt=s, number=100000)
print(t)

s = "if hasattr(str, '__bool__'): pass"   ##if it is string, pass?
res=timeit.timeit(stmt=s, number= 100000)
print(res)


##example of hasattr() 
import timeit 
s = """
try: 
    str.__bool__
except AttributeError:
    pass 
"""
t=timeit.timeit(stmt=s, number=100000)
print(t)
s = "if hasattr(int, '__bool__'):pass"
res=timeit.timeit(stmt=s, number=100000)
print(res)