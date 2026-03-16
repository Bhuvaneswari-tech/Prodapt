
import itertools

count = 0

for i in itertools.cycle(['A','B','C']):
    if count == 6:
        break
    print(i)
    count += 1