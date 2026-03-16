class Count:
    def __init__(self, max):
        self.max = max
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.max:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

c = Count(5)

for i in c:
    print(i)
    
l1 = []
for i in range(1,5+1):
    l1.append(i)
print(*l1)