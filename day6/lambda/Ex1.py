from functools import reduce

data = [10,20,30,40]

# transform
data2 = list(map(lambda x: x*2, data))
print(data2)
# filter
data3 = list(filter(lambda x: x > 40, data2))
print(data3)
# aggregate
total = reduce(lambda a,b: a+b, data3)

print(total)
