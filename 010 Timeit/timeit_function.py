import timeit
def f(x):
    return x ** 2

def g(x):
    return x**4 

def h(x):
    return x**8

print(timeit.timeit("[func(42) for func in (f,g,h)]", globals=globals()))
