def log(func):

    def wrapper(*args, **kwargs):
        print("Function is executing")
        func(*args, **kwargs)

    return wrapper

#**kwargs is used to pass keyword arguments to the function. 
# The **kwargs syntax collects all the keyword arguments into a 
# dictionary, which can be accessed within the function.

@log
def add(a, b):
    print(a + b)

add(a=5, b=3)