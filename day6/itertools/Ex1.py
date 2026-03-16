import itertools

for i in itertools.count(5):
    if i > 10:
        break
    print(i, end = ' ')
print()
