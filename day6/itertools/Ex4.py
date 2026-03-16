import itertools

data = [1,2,3]
#permutations - all possible arrangements of the data
result = itertools.permutations(data)

#combinations - Without changing the order of the data
result1 = itertools.combinations(data, 3)

print(list(result))
print(list(result1))

