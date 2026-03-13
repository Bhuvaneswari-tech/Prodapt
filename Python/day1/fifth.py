# operators_example5.py
a = 5 # binary 0101
b = 3 # binary 0011
print("a & b =", a & b) # 0101 & 0011 = 0001 -> 1
print("a | b =", a | b) # 0101 | 0011 = 0111 -> 7
print("a ^ b =", a ^ b) # 0101 ^ 0011 = 0110 -> 6
print("~a =", ~a) # bitwise NOT of 5 (0101) is 1010 in two's complement, which is -6 in decimal
# 0111 -> 7
# 0110 -> 6
# bitwise NOT -> -6 (two's complement)
print("a << 1 =", a << 1) # 0101 << 1 = 1010 -> 10
print("a >> 1 =", a >> 1) # 0101 >> 1 = 0010 -> 2