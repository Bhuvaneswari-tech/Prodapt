from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined = ChainMap(dict1, dict2)

print(combined)
print(combined['a'])