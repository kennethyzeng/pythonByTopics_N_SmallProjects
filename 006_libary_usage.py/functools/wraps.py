"""
wrapper: wrapper() function
wrapped: func or orgianl function my_function()
decorator: my_decorator()

Below with wraps. It keep the attribute of oringal function.
also check without wraps
"""

from functools import wraps 

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        return (func(*args, **kwargs))
    return wrapper 

@my_decorator 
def my_function():
    """This is decorated function."""
    print("Function executed")

print(my_function.__name__)
print(my_function.__doc__)
print(my_function.__module__)

"""
my_function
This is decorated function.
__main__
"""