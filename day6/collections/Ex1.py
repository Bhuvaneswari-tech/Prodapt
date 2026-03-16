from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

result = Counter(data)

print(result)
print(result['apple'])