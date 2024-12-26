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

