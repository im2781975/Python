#Bitwise operator
a, b = 10, -20
print(~a, ~b)
#~n -> -|n+1|
# ~-n -> |n-1|

c, d = 0, 1
print(c ^ d)
print(c & d)
print(bin(c | d))
print(d << 5)
print(bin(100 >> 2))

#inplace operation
a = 0b001
a &= 0b010
a |= 0b010
a <<= 2
a >>= 2
a ^= 0b011
print(a)
