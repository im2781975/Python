from operator import add 
add(1, 1)
from operator import mul 
mul('a', 10)
mul([3], 3)
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

#comparizon operator
if 1 > -1 < 2 > 0.5 < 100 != 24:
    print("Yes")
else:
    print("No")
    
a = b = 'Python is fun!'
print(a == b, a is b)
a = [1, 2, 3, 4, 5] 
b = a
print(a == b, a is b)
b = a[:]
print(a == b, a is b)

if myvar is not None:   
    print("Not none");
if myvar is None:    
    print("None")
    
sentinel = object() 
def myfunc(var = sentinel):
    if var is sentinel:     
        print("Yes")
    else:   
        print("No")
        
print("alpha" < "beta")
print('12' != '1')
print('12' == 12)

class Foo(object):    
    def __init__(self, item):        self.my_item = item
    def __eq__(self, other):        return self.my_item == other.my_item   
a = Foo(5)
b = Foo(5) 
a == b     
a != b     
a is b

class Bar(object):    
    def __init__(self, item):        self.other_item = item 
    def __eq__(self, other):        return self.other_item == other.other_item    
    def __ne__(self, other):        return self.other_item != other.other_item   
c = Bar(5) 
a == c    
