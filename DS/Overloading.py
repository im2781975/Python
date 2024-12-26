+ Addition __add__(self, other) a1 + a2
- Subtraction __sub__(self, other) a1 - a2 
* Multiplication __mul__(self, other) a1 * a2 
@ Matrix Multiplication __matmul__(self, other) a1 @ a2 
/ Division __div__(self, other) a1 / a2 
/ Division __truediv__(self, other) a1 / a2 
// Floor Division __floordiv__(self, other) a1 // a2 
% Modulo/Remainder __mod__(self, other) a1 % a2 
** Power __pow__(self, other[, modulo]) a1 ** a2
<< Bitwise Left Shift __lshift__(self, other) a1 << a2
>> Bitwise Right Shift __rshift__(self, other) a1 >> a2
& Bitwise AND __and__(self, other) a1 & a2 
^ Bitwise XOR __xor__(self, other) a1 ^ a2
| (Bitwise OR) __or__(self, other) a1 | a2
- Negation (Arithmetic) __neg__(self)-a1 
+ Positive __pos__(self) +a1
~ Bitwise NOT __invert__(self) ~a1 
< Less than __lt__(self, other) a1 < a2
<= Less than or Equal to __le__(self, other) a1 <= a2 
== Equal to __eq__(self, other) a1 == a2
!= Not Equal to __ne__(self, other) a1 != a2
> Greater than __gt__(self, other) a1 > a2
>= Greater than or Equal to__ge__(self, other) a1 >= a2 
[index] Index operator __getitem__(self, index) a1[index] 
in In operator __contains__(self, other) a2 in a1 
(*args, ...) Calling __call__(self, *args, **kwargs)a1(*args, **kwargs)

Casting to int __int__(self) int(a1)
Absolute function __abs__(self) abs(a1)
Casting to str __str__(self) str(a1)
Casting to unicode __unicode__(self) unicode(a1) 
String representation__repr__(self) repr(a1)
Casting to bool __nonzero__(self) bool(a1)
String formatting __format__(self, formatstr)"Hi {:abc}".format(a1)
Hashing __hash__(self) hash(a1) 
Length __len__(self) len(a1) 
Reversed __reversed__(self) reversed(a1)
Floor __floor__(self) math.floor(a1)
Ceiling __ceil__(self) math.ceil(a1)
class A:    
    def __init__(self, a):        
        self.a = a    
    def __add__(self, other):        
        return self.a + other    
    def __radd__(self, other):        print("radd")
return other + self.a
A(1) + 2  
2 + A(1)  

class B:   
    def __init__(self, b):        
        self.b = b    
    def __iadd__(self, other):        
        self.b += other        
        print("iadd")       
        return self
b = B(2) 
b.b        
b += 1   
b.b   

import math
class Vector(object):    
    def __init__(self, x, y):
        self.x = x        
        self.y = y
    def __neg__(self):  
        return Vector(-self.x, -self.y)
    def __add__(self, other):        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):        return self + (-other)
    def __eq__(self, other):        
        return self.x == other.x and self.y == other.y
    def __abs__(self):        
        return math.hypot(self.x, self.y)
    def __str__(self):    
        return '<{0.x}, {0.y}>'.format(self)
    def __repr__(self):        
        return 'Vector({0.x}, {0.y})'.format(self)
v = Vector(1, 4)
u = Vector(2, 0)
u + v
print(u + v) 
u - v           
u == v          
u + v == v + u  
abs(u + v)   
