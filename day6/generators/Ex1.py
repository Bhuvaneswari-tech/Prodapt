def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

print(next(g))
print(next(g))
print(next(g))
