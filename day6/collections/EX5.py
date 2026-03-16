d1 = {}

d1['a'] = 0
d1['b'] = 10
d1['c'] = 0

print(d1)

from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 3

print(d)

d.move_to_end('a')

print(d)
