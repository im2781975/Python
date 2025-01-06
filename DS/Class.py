class MultiIndexingList:    
    def __init__(self, value):        
        self.value = value           
    def __repr__(self):       
        return repr(self.value)       
    def __getitem__(self, item):        
        if isinstance(item, (int, slice)):            
            return self.__class__(self.value[item])        
        return [self.value[i] for i in item]      
    def __setitem__(self, item, value):      
        if isinstance(item, int):            
            self.value[item] = value    
        elif isinstance(item, slice):            
            raise ValueError('Cannot interpret slice with multiindexing')        
        else:           
            for i in item:                
                if isinstance(i, slice):                    
                    raise ValueError('Cannot interpret slice with multiindexing')                
                self.value[i] = value       
    def __delitem__(self, item):        
        if isinstance(item, int):            
            del self.value[item]        
        elif isinstance(item, slice):            
            del self.value[item]        
        else:           
            if any(isinstance(elem, slice) for elem in item):               
                raise ValueError('Cannot interpret slice with multiindexing')           
            item = sorted(item, reverse=True)            
            for elem in item:               
                del self.value[elem]
a = MultiIndexingList([1,2,3,4,5,6,7,8])
a[4, 1, 5:, 2, ::2]
a[4] = 1000
a[2,6,1] = 100
del a[5]
del a[4,2,5]

arr = ['a', 'b', 'c', 'd']
print(arr[0])
print(arr[1])
print(arr[-1])

class Integer(object):   
    def __init__(self, value):        
        self.value = int(value) # Cast to an integer           
    def __repr__(self):        
        return '{cls}({val})'.format(cls=self.__class__.__name__,   val=self.value)      
    def __pow__(self, other, modulo=None):        
        if modulo is None:           
            print('Using __pow__')            
            return self.__class__(self.value ** other)       
        else:            
            print('Using __pow__ with modulo')            
            return self.__class__(pow(self.value, other, modulo))      
    def __float__(self):        
        print('Using __float__')        
        return float(self.value)       
    def __complex__(self):        
        print('Using __complex__')       
        return complex(self.value, 0)
Integer(2) ** 2                 
Integer(2) ** 2.5               
pow(Integer(2), 0.5)            
operator.pow(Integer(2), 3)     
operator.__pow__(Integer(3), 3) 
pow(Integer(2), 3, 4)  
Integer(2).__pow__(3, 4)   

import math
math.pow(Integer(2), 0.5)
import cmath
cmath.exp(Integer(2)) 

z = y ** (1.0 / 3)

class sparselist(object):   
    def __init__(self, size):       
        self.size = size        
        self.data = {}      
    def __getitem__(self, index):        
        if index < 0:            
            index += self.size        
        if index >= self.size:           
            raise IndexError(index)
        try:            
            return self.data[index]        
        except KeyError:            
            return 0.0
    def __setitem__(self, index, value):       
        self.data[index] = value
    def __delitem__(self, index):        
        if index in self.data:            
            del self.data[index]
    def __contains__(self, value):        
        return value == 0.0 or value in self.data.values()
    def __len__(self):        
        return self.size
    def __iter__(self):        
        return (self[i] for i in range(self.size))
l = sparselist(10 ** 6) 
0 in l  
l[12345] = 10

class adder(object):  
    def __init__(self, first):        
        self.first = first  
    def __call__(self, second):       
        return self.first + second
add2 = adder(2) 
add2(1) 
add2(2)  

class MyIterable:    
    def __iter__(self):         return self    
    def __next__(self):
        pass
class MySequence:    
    def __getitem__(self, index):         
        if (condition):             raise IndexError        
        return (item)

ex1 = MyIterableClass() 
ex2 = MySequence() 
for (item) in (ex1): pass
for (item) in (ex2): pass

class AssignValue(object):    
    def __init__(self, value):        
        self.value = value 
my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value))
class Example(object):    
    def __init__(self,a,b,c):        
        self.a, self.b, self.c = a,b,c    
    def __format__(self, format_spec):       
    """ Implement special semantics for the 's' format specifier """        
        if format_spec[-1] != 's':            
            raise ValueError('{} format specifier not understood for this object', format_spec[:-1])
            raw = "(" + ",".join([str(self.a), str(self.b), str(self.c)]) + ")"
        return "{r:{f}}".format( r=raw, f=format_spec )
inst = Example(1,2,3)
print "{0:>20s}".format( inst )
class Person(object):  
    first = 'Zaphod'    
    last = 'Beeblebrox' 
'{p.first} {p.last}'.format(p=Person())

root
- A  
    - AA 
    - AB
- B 
    - BA
    - BB    
        - BBA
root = get_root(tree)
for node in get_children(root):    
    print(get_name(node))    
    for child in get_children(node):       
        print(get_name(child))        
        for grand_child in get_children(child):            
            print(get_name(grand_child))
def list_tree_names(node):    
    for child in get_children(node):       
        print(get_name(child))        
        list_tree_names(node=child) 
list_tree_names(node=get_root(tree))

def list_tree_names(node, lst=[]):    
    for child in get_children(node):        
        lst.append(get_name(child))        
        list_tree_names(node=child, lst=lst)    
    return lst
list_tree_names(node=get_root(tree))

class Cash(object):   
    def __init__(self, value):       
        self.value = value    
    @property    
    def formatted(self):        
        return '${:.2f}'.format(self.value)   
    @formatted.setter    
    def formatted(self, new):        
        self.value = float(new[1:])
wallet = Cash(2.50) 
print(wallet.formatted)
print(wallet.value)
wallet.formatted = '$123.45'
print(wallet.formatted)
print(wallet.value)

class Foo(object):    
    def __init__(self):        
        self.__bar = None    
    @property  
    def bar(self):        
        if self.__bar is None:           
            self.__bar = some_expensive_lookup_operation()        
        return self.__bar
from foobar import Foo
foo = Foo()
print(foo.bar) 
print(foo.bar) 

class BaseClass(object):
    @property 
    def foo(self): 
        return some_calculated_value() 
    @foo.setter 
    def foo(self, value):        
        do_something_with_value(value) 
class DerivedClass(BaseClass): 
    @BaseClass.foo.setter 
    def foo(self, value):        
        do_something_different_with_value(value)
        
class A:   
    p = 1234 
    def getX (self):
        return self._x
    def setX (self, value): 
        self._x = value 
    def getY (self): 
        return self._y 
    def setY (self, value): 
        self._y = 1000 + value    
    def getY2 (self): 
        return self._y 
    def setY2 (self, value): 
        self._y = value 
    def getT    (self): 
        return self._t
    def setT (self, value): 
        self._t = value 
    def getU (self): return self._u + 10000 
    def setU (self, value):
        self._u = value - 5000
x, y, y2 = property (getX, setX), property (getY, setY), property (getY2, setY2)   
t  = property (getT, setT)
u = property (getU, setU)
A.q = 5678

class B:
    def getZ (self):
        return self.z_ 
    def setZ (self, value):
        self.z_ = value  
    z = property (getZ, setZ)
class C: 
    def __init__ (self):
        self.offset = 1234 
    def getW (self): 
        return self.w_ + self.offset 
    def setW (self, value): 
        self.w_ = value - self.offset    
    w = property (getW, setW)
a1 = A () 
a2 = A () 
a1.y2 = 1000 
a2.y2 = 2000 
a1.x = 5 
a1.y = 6 
a2.x = 7 
a2.y = 8 
a1.t = 77
a1.u = 88
print (a1.x, a1.y, a1.y2)
print (a2.x, a2.y, a2.y2) 
print (a1.p, a2.p, a1.q, a2.q)
print (a1.t, a1.u)

b = B ()
c = C ()
b.z = 100100
c.z = 200200 
c.w = 300300
print (a1.x, b.z, c.z, c.w)
c.w = 400400 
c.z = 500500 
b.z = 600600
print (a1.x, b.z, c.z, c.w)

class Duck:   
    def quack(self):      
        print("Quaaaaaack!")   
    def feathers(self):      
        print("The duck has white and gray feathers.")
class Person:    
    def quack(self):       
        print("The person imitates a duck.")    
    def feathers(self):     
        print("The person takes a feather from the ground and shows it.")   
    def name(self):       
        print("John Smith")
def in_the_forest(obj):   
    obj.quack()  
    obj.feathers()
donald = Duck() 
john = Person() 
in_the_forest(donald) 
in_the_forest(john)

class Shape:
    def calculate_area(self):
        raise NotImplemented
class Square(Shape):
    side_length = 2
    def calculate_area(self):
        return self.side_length * 2
class Triangle(Shape):
    base_length = 4    
    height = 3
    def calculate_area(self):
        return 0.5 * self.base_length * self.height
    def get_area(input_obj):
        print(input_obj.calculate_area())
shape_obj = Shape() 
square_obj = Square()
triangle_obj = Triangle()
get_area(shape_obj) 
get_area(square_obj) 
get_area(triangle_obj)

class Square:    
    side_length = 2    
    def calculate_square_area(self):        
        return self.side_length ** 2
class Triangle:   
    base_length = 4   
    height = 3    
    def calculate_triangle_area(self):        
        return (0.5 * self.base_length) * self.height
    def get_area(input_obj):
        if type(input_obj).__name__ == "Square":        area = input_obj.calculate_square_area()    
        elif type(input_obj).__name__ == "Triangle":        
            area = input_obj.calculate_triangle_area()    print(area)
square_obj = Square()
triangle_obj = Triangle()
get_area(square_obj)
get_area(triangle_obj)

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
