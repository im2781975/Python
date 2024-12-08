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

#Boolean
def or_(a, b):    
    if a:        
        return a    
    else:        
        return b
def and_(a, b):    
    if not a:        
        return a    
    else:        
        return b
print(or_(10, 15))

def T():
    return True
def F():
    return False
print(T() and F())
print(T() or F())

#compare
x = 3.141
if 3.14 < x < 3.142:    
    print("x is near pi")
else:
    print("Outer")
