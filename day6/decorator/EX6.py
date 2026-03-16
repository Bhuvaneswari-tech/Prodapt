def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def add_exclamation(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@uppercase
@add_exclamation
def hello():
    return "hello world"

print(hello())
