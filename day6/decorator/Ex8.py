#Caching Decorator
def cache(func):
    memory = {}

    def wrapper(n):
        if n in memory:
            return memory[n]

        result = func(n)
        memory[n] = result
        return result

    return wrapper

@cache
def square(n):
    print("Calculating...")
    return n * n

print(square(4))
print(square(4))