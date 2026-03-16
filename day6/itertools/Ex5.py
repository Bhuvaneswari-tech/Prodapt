import itertools

a = [1,2]
b = [3,4]

result = itertools.product(a,b)
print(list(result))

#Real time usage
l1=['Red', 'Green']
l2=['Small', 'Medium', 'Large']

result = list(itertools.product(l1, l2))

#print(list(result))
for i in result:
    print(i)
    
print(result)
    
# for x in l1:
#     for y in l2:
#         print(x,y)