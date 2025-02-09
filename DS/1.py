class delta:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return delta(self.value + other.value)
    def __sub__(self, other):
        return delta(self.value - other.value)
    def __mul__(self, other):
        return delta(self.value * other.value)
    def __matmul__(self, other):
        return delta(self.value @ other.value)  
    def __truediv__(self, other):
        return delta(self.value / other.value)
    def __floordiv__(self, other):
        return delta(self.value // other.value)
    def __mod__(self, other):
        return delta(self.value % other.value)
    def __pow__(self, other, modulo = None):
        return delta(pow(self.value, other.value, modulo) if modulo else self.value ** other.value)
    def __lshift__(self, other):
        return delta(self.value << other.value)
    def __rshift__(self, other):
        return delta(self.value >> other.value)
    def __and__(self, other):
        return delta(self.value & other.value)
    def __xor__(self, other):
        return delta(self.value ^ other.value)
    def __or__(self, other):
        return delta(self.value | other.value)
    def __neg__(self):
        return delta(-self.value)
    def __pos__(self):
        return delta(+self.value)
    def __invert__(self):
        return delta(~self.value)
    def __lt__(self, other):
        return self.value < other.value
    def __le__(self, other):
        return self.value <= other.value
    def __eq__(self, other):
        return self.value == other.value
    def __ne__(self, other):
        return self.value != other.value
    def __gt__(self, other):
        return self.value > other.value
    def __ge__(self, other):
        return self.value >= other.value
    def __getitem__(self, index):
        return str(self.value)[index]  
        # Access digit of a number as a string
    def __contains__(self, other):
        return str(other) in str(self.value)
    def __call__(self, *args, **kwargs):
        return f"Called with {args}, {kwargs}"
    def __str__(self):
        return str(self.value)
x, y = delta(10), delta(3)
print(x + y, x - y, x * y, x / y, x // y, x % y)
print(x ** y, x << y, x >> y, x & y, x | y, x ^ y) 
print(-x, +x, ~x, x > y, x < y, x == y, x != y) 
a = delta(12345)
print(a[2], 2 in a)
print(x(5, key = "value"))
import math
class cast:
    def __init__(self, value):
        self.value = value
    def __int__(self):
        return int(self.value)
    def __abs__(self):
        return abs(self.value)
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"CustomNumber({self.value})"
    def __unicode__(self):
        return unicode(self.value)
    def __bool__(self):
        return self.value != 0
    def __format__(self, formatstr):
        return formatstr.format(self.value)
    def __hash__(self):
        return hash(self.value)
    def __len__(self):
        return len(str(abs(self.value)))
    def __reversed__(self):
        return reversed(str(abs(self.value)))  
    def __floor__(self):
        return math.floor(self.value)
    def __ceil__(self):
        return math.ceil(self.value)
num = cast(123.75)
num_neg = cast(-456.25)
print("Casting to int:", int(num))  
print("Absolute value:", abs(num_neg))  
print("Casting to str:", str(num))  
print("String representation:", repr(num))
print("Casting to bool:", bool(num))
print("Casting to bool (zero case):", bool(cast(0)))  
print("String formatting:", "{:.2f}".format(num))  
print("Hash value:", hash(num)) 
print("Length (digit count):", len(CustomNumber(98765)))  
print("Reversed digits:", ''.join(reversed(CustomNumber(54321))))  
print("Floor value:", math.floor(num)) 
print("Ceiling value:", math.ceil(num))
"""					"""
class A:    
    def __init__(self, a):        
        self.a = a    
    def __add__(self, other):        
        return self.a + other  
    def __radd__(self, other): 
        print("radd")
        return other + self.a
class B:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):        
        self.val += other        
        print("iadd")
        return self  
obj = A(10)
print(obj + 5, 5 + obj)
print(A(11) + 7, 7 + A(11))
b = B(88)
print(b.val)
b += 1; print(b.val)
"""				"""
import math
class Vector:    
    def __init__(self, x, y):
        self.x = x; self.y = y
    def __neg__(self):  
        return Vector(-self.x, -self.y)
    def __add__(self, other):        
        if not isinstance(other, Vector):
            raise TypeError("Can only add another Vector")
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):        
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract another Vector")
        return self + (-other)
    def __eq__(self, other):        
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
    def __abs__(self):        
        return math.hypot(self.x, self.y)
    def __mul__(self, scalar):  
        if not isinstance(scalar, (int, float)):
            raise TypeError("Multiplication requires a scalar (int or float)")
        return Vector(self.x * scalar, self.y * scalar)
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Division requires a scalar (int or float)")
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Vector(self.x / scalar, self.y / scalar)
    def __floordiv__(self, scalar): 
        return Vector(self.x // scalar, self.y // scalar)
    def __str__(self):    
        return f'<{self.x}, {self.y}>'
    def __repr__(self):        
        return f'Vector({self.x}, {self.y})'
v = Vector(3, 4); u = Vector(1, 2)
print(v + u, v - u, v == u, abs(v))  
print(v * 2, v / 2, v // 2, u + v == v + u)
"""						"""
class lst:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return repr(self.val)
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.val[item])        
        return [self.val[i] for i in item] 
    def __setitem__(self, item, value):  
        if isinstance(item, int):        
            self.val[item] = value
        elif isinstance(item, slice):    
            raise ValueError('Cannot interpret slice with multiindexing')        
        else:           
            for i in item:                
                if isinstance(i, slice):   
                    raise ValueError('Cannot interpret slice with multiindexing')
                self.val[i] = value   
    def __delitem__(self, item):        
        if isinstance(item, int):     
            del self.val[item]        
        elif isinstance(item, slice):     
            del self.val[item]        
        else:           
            if any(isinstance(elem, slice) for elem in item):        
                raise ValueError('Cannot interpret slice with multiindexing')       
            item = sorted(item, reverse = True)            
            for elem in item:           
                del self.val[elem]
l = lst([1, 2, 3, 4, 5, 6, 7, 8])
print(l[4], l[1], l[5:], l[::2])
l[4] = 1000; l[2, 6, 1] = 100
del(l[4, 2, 5])
print(l[::1])
"""				"""
import operator
class integral(object):   
    def __init__(self, val):        
        self.val = int(val)
    def __repr__(self):        
        return '{cls}( {val} )'.format(cls = self.__class__.__name__, val = self.val)
    def __pow__(self, other, module = None):        
        if module is None:           
            return self.__class__(self.val ** other)       
        else:  
            return self.__class__(pow(self.val, other, module)) 
    def __float__(self):      
        return float(self.val)       
    def __complex__(self):        
        return complex(self.val, 0)
x = integral(5)
print(x, x ** 5, x.__pow__(3, 7), float(x), complex(x))
print(integral(5) ** 8, pow(integral(2), 0.5))
print(operator.pow(integral(2), 3), operator.__pow__(integral(3), 3))
print(pow(integral(2), 3, 4), integral(2).__pow__(3, 4))
"""				"""
class sparselist(object):   
    def __init__(self, size):       
        self.size = size        
        self.data = {}      
    def __getitem__(self, index):    
        if isinstance(index, slice): 
            return [self[i] for i in range(*index.indices(self.size))]  
        if index < 0:            
            index += self.size        
        if index >= self.size:           
            raise IndexError(index)
        return self.data.get(index, 0.0)
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
sp= sparselist(10)
sp[2], sp[5] = 3.5, 7.2
print(sp[1::]); del sp[2]
print(sp[::1])
print(3.5 in sp, 7.2 in sp, 0.0 in sp) 
print(len(sp), list(sp))
l = sparselist(10 ** 6) 
print(sparselist(10 ** 6))
"""				"""
class Instructor:
    print("Empty class")
    def __init__(self):
        print("Constructor")
instruc = Instructor()
instruc.name = "Hasan"
print(type(instruc),"\n", instruc.name)
"""                    """
class teacher:
    follower = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.follower = 0
    def show(self, sub):
        print(f"name: {self.name}, teach: {sub}, follower: {self.follower}, lived in: {self.address}");
    def update(self, namefollower):
        self.follower += 1
        print(f"name: {namefollower}\nfollower: {self.follower} ")
tr = teacher("Ab", "124 via villa")
tr.show("chem")
for i in range(5):
    tr.update("Hasan")
print(tr.follower)
"""                    """
class circle:
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def __init__(self, radius = 6):
        self.radius = radius
        self.area = circle.pi * radius * radius
    def circum(self):
        return 2 * circle.pi * self.radius
cir = circle(5.42)
print(cir.area, cir.circum())
"""        Multiple Inheritance        """
class human:
    def __init__(self, heart):
        self.eyes = 1; self.noses = 1;
        self.heart = heart
    def eat(self):
        print("eat")
    def work(self):
        print("work")
class male(human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name
    def flirt(self):
        print("flirt")
    def work(self):
        super().work()
    def show(self):
        print(f"name: {self.name}, have {self.heart}, do{self.work()} ")
        self.work()
class female:
    def __init__(self, name):
        self.name = name
    def flirt(self):
        print("flirt")
    def work():
        print("can code")
class boy(male, female):
    def __init__(self, name, heart, lang):
        male.__init__(self, name, heart)
        female.__init__(self, name)
        self.lang = lang
    def sleep(self):
        print("sleep")
    def work(self):
        print("cab test")
ml = male("Ab", 1); ml.show()
print(ml.noses, ml.eyes)
by = boy("Hasan", 1, "python")
by.flirt(); by.work();
print(boy.mro())
print(by.noses, by.heart, by.lang)
"""         MultiLevelHeritance        """
class human(object):
    breath = True
    def __init__(self, heart):
        self.heart = heart
        self.eyes = 2
    def eat(self):
        print("eat")
    def work(self):
        print("work")
class male(human):
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print("sleep")
class boy(male):
    def __init__(self, name, heart, dance):
        male.__init__(self, name)
        human.__init__(self, heart)
        self.dance = dance
    def work(self):
        #human.work(self)
        super().work()
        print("Can Code")
class programmer(boy):
    def work(self):
        print("Coded")
by = boy("Roy", 1, True)
by.eat(); by.work()
print(by.name, "\n", boy.mro())
prg = programmer("Molla", 2, False)
prg.work() 
"""        Heirical Inheritance        """
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self):
        print(f"name: {self.name}, age: {self.age} ")
    def eat(self):
        print("Can eat")
class Male(Human):
    def __init__(self, name, age, location):
        Human.__init__(self, name, age)
        self.location = location
    def sleep(self):
        print("Can sleep")
    def disp(self):
        print(f"name: {self.name}, age: {self.age}, location: {self.location} ")
class Female(Human):
    def __init__(self, name, age, dance):
        super().__init__(name, age)
        self.dance = dance
    def display(self):
        Human.disp(self)
        print(f"Dance: {self.dance} ")
    def work(self):
        print("Can code")
female = Female("Aslam", 24, True)
female.display(); female.eat()
male = Male("Molla", 25, "DCA")
male.disp()
"""					"""
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area")
class Square(Shape):
    length = 2
    def calculate_area(self):
        return self.length ** 2 
class Triangle(Shape):
    length = 4; height = 3
    def calculate_area(self):
        return 0.5 * self.length * self.height
def get_area(obj):
    print(obj.calculate_area())
square_obj = Square()
triangle_obj = Triangle()
get_area(square_obj) 
get_area(triangle_obj)
"""					"""
class Square:    
    length = 2    
    def square_area(self): 
        return self.length ** 2
class Triangle:   
    length = 4   
    height = 3    
    def triangle_area(self):
        return 0.5 * self.length * self.height
def get_area(obj):
    if isinstance(obj, Square):  
        area = obj.square_area()    
    elif isinstance(obj, Triangle):
        area = obj.triangle_area()
    else:
        raise TypeError("Unsupported object type")
    print(area)
square_obj = Square()
triangle_obj = Triangle()
get_area(square_obj)
get_area(triangle_obj)
"""            HibridHeritance        """
class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C:
    def show(self):
        print("C")
class D(B, C):
    def show(self):
        print("D")
x = D(); x.show();print(D.mro())
"""            DiamondHeritance        """
class A:
    def disp(self):
        print("A")
class B:
    def disp(self):
        print("B")
class C(A):
    def show(self):
        print("Class C")
    def show(self):
        print("Disp C")
class D(B, C):
    pass
d = D(); d.disp(); d.show()
"""        ABSTRACTION            """
from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self, n):
        self.type = n
    @abstractmethod
    def start(self):
        pass
    def disp(self):
        print("calling from vehicle")
class bike(vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("Bike start")
    def disp(self):
        print("")
class scooty(vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("Scooty start")
class car(vehicle):
    def __init__(self, n, gear):
        super().__init__(n)
        self.gear = 6
    def start(self):
        print("Car start")
bk = bike(2, "black")
bk.start()
"""          Access Modifier          """
class student:
    def __init__(self, name, roll, age):
        self.name = name
        self._roll = roll
        self.__age = age
    def __display(self):
        print(f"{self.name}\n{self._roll}\n{self.__age}")
    def dispData(self):
        self.__display()
class branch(student):
    pass
def showData():
    std = branch("Hasan", 21, 22)
    print(std.name, std._roll)
showData()
std = student("Molla", 34, 23)
print(std.dispData())
std._student__display()
print(dir(std))
"""            ENCAPSULATION            """
class student:
    def __init__(self, name, roll, age):
        self.name = name
        self._roll = roll; self.__age = age
    def getage(self):
        return self._age
    def setage(self, age):
        if self.__age > 35:
            print("should be less than 35")
        else:
            self.__age = age
    def __disp(self):
        print(f"name: {self.name}, roll: {self._roll}, age: {self.__age} ")
    def show(self):
        self.__disp()
class branch(student):
    def showData(self):
        print(f"name: {self.name}, roll: {self._roll}, age: {self.__age} ")
std = student("Aa", 29, 35)
std.setage(49)
print(std.show()); std._student__disp()
print(dir(std))
"""            DUCK TYPING            """
class duck:
    def swim(self):
        print("duck swim")
    def speak(self):
        print("duck speak")
class dog:
    def swim(self):
        print("dog swim")
    def speak(self):
        print("dog speak")
def disp(obj):
    obj.swim(); obj.speak()
class demo:
    def disp(self, obj):
        obj.swim(); obj.speak()
d = duck(); disp(d)
dm = demo(); dm.disp(d)
"""            OVERRIDING            """
class complexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __add__(self, other):
        return f"{self.real + other.real} + {self.img + other.img}i" 
a, b = complexNum(1, 2), complexNum(4, 5)
print(a + b)
"""            """
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        self.age > other.age
x = person("Aa", 22)
y = person("Bb", 23)
if x > y:
    print(f"{x.name} pay the bill")
else:
    print(f"{y.name} pay the bill")
"""            """
class father:
    def sleep(self):
        print("sleep")
class son(father):
    def sleep(self):
        print("sleeping")
        super().sleep()
s = son(); s.sleep()
"""                """
class author:
    def __init__(self, name, bookname, pages):
        self.name = name
        self.bookname = bookname; self.pages = pages
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"{self.name} wrote {self.bookname} which has {self.pages}"
    def __call__(self, *args, **kwargs):
        print("Hi")
    def __del__(self):
        print("Has been deleted")
inf = author("Aa", "Bb", 124)
print(len(inf), str(inf), inf)
inf(7, 9); del inf
"""                """
class Bank:
    def __init__(self, name, balance = 9):
        self.holder = name
        self.balance = balance
    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited amount is {self.amount} ")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
    def __str__(self):
        return f"Holder name: {self.holder}\nBalanced: {self.balance}"
UCB = Bank("Aa", 9000)
print(UCB, str(UCB), Bank.mro())
"""					"""
class total(object):  
    def __init__(self, first):        
        self.first = first  
    def __call__(self, second):       
        return self.first + second
x = total(2)
print(x(1))
"""                """
class MyIterable:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit  
    def __iter__(self):
        return self  
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current - 1
it = MyIterable(5)
for i in it:
    print(i)
"""                """
class MySequence:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        if index < 0 or index >= len(self.data): 
            raise IndexError("Index out of range")
        return self.data[index] 
seq = MySequence([10, 20, 30, 40, 50])
print(seq[2], seq[4], list(seq))
"""            """
class AssignValue(object):    
    def __init__(self, value):        
        self.value = value 
x = AssignValue(6)
print('My value is: {0.value}'.format(x))
"""                """
class Example(object):    
    def __init__(self, a, b, c):        
        self.a = a; self.b = b
        self.c = c  
    def __format__(self, format_spec):
        raw = f"({self.a}, {self.b}, {self.c})"
        if format_spec and format_spec[-1] != 's':  
            raise ValueError(f"'{format_spec}' format specifier not understood for this object")
        return f"{raw:{format_spec}}"
ex = Example(1, 2, 3)
print(f"{ex:s}, {ex}", "{0:>20s}".format(ex))
"""                """
class Person(object):  
    first = 'Zaphod'    
    last = 'Beeblebrox' 
print('{p.first} {p.last}'.format(p = Person()))
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
print(wallet.formatted, wallet.value)
wallet.formatted = '$123.45'
print(wallet.formatted, wallet.value)
"""                """
class Foo(object):    
    def __init__(self):        
        self.__bar = None    
    @property  
    def bar(self):        
        if self.__bar is None:           
            self.__bar = self.some_expensive_lookup_operation()        
        return self.__bar
    def some_expensive_lookup_operation(self):
        print("Performing expensive lookup")
        return "Expensive Data"
foo = Foo()
print(foo.bar, foo.bar)
"""                """
class BaseClass(object):
    def __init__(self):
        self._foo = None 
    @property 
    def foo(self): 
        return self.calculated_value() 
    @foo.setter 
    def foo(self, value):        
        self.do_with_value(value)
    def calculated_value(self):
        return "BaseClass Value"
    def do_with_value(self, value):
        print(f"BaseClass processing: {value}")
        self._foo = value
class DerivedClass(BaseClass): 
    @property
    def foo(self): 
        return super().foo  
    @foo.setter 
    def foo(self, value):        
        self.do_different_with_value(value)
    def do_different_with_value(self, value):
        print(f"DerivedClass processing: {value}")
        self._foo = value 
obj = DerivedClass()
obj.foo = 42 ; print(obj.foo)
"""                """
class A:
    p = 1234  
    def __init__(self):
        self._x = None; self._y = None
        self._t = None; self._u = None
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = 1000 + value
    @property
    def y2(self):
        return self._y
    @y2.setter
    def y2(self, value):
        self._y = value
    @property
    def t(self):
        return self._t
    @t.setter
    def t(self, value):
        self._t = value
    @property
    def u(self):
        return self._u + 10000 if self._u is not None else None
    @u.setter
    def u(self, value):
        self._u = value - 5000
obj = A()
obj.x = 10; print(obj.x)
obj.y = 20; print(obj.y) 
obj.y2 = 500; print(obj.y2) 
obj.t = 30; print(obj.t)  
obj.u = 7000; print(obj.u) 
"""                    """
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
    def getU (self):
        return self._u + 10000 
    def setU (self, value):
        self._u = value - 5000 
    x = property(getX, setX)
    y = property(getY, setY)
    y2 = property(getY2, setY2)
    t = property(getT, setT)
    u = property(getU, setU)
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
a1, a2 = A () 
a1.y2, a2.y2 = 1000, 2000
a1.x = 5; a1.y = 6 
a2.x = 7; a2.y = 8 
a1.t = 77; a1.u = 88
print (a1.x, a1.y, a1.y2)
print (a2.x, a2.y, a2.y2) 
print (a1.t, a1.u)
b = B ()
c = C ()
b.z = 100100; c.z = 200200; c.w = 300300
print (a1.x, b.z, c.z, c.w)
c.w = 400400; c.z = 500500; b.z = 600600
print (a1.x, b.z, c.z, c.w)
A.q = 5678
obj = A()
obj.x = 10; print(obj.x) 
obj.y = 20; print(obj.y) 
obj.y2 = 500; print(obj.y2)  
obj.t = 30; print(obj.t)  
obj.u = 7000; print(obj.u) 
print(A.p, A.q)
"""					"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 
    def getData(self): 
        return self.data 
    def getNext(self): 
        return self.next 
    def setData(self, val):
        self.data = val 
    def setNext(self, val):
        self.next = val
class LinkedList: 
    def __init__(self):
        self.head = None 
    def isEmpty(self):
        return self.head is None 
    def add(self, item):
        new_node = Node(item)  
        new_node.setNext(self.head) 
        self.head = new_node 
    def size(self):
        count = 0       
        current = self.head
        while current is not None:
            count += 1            
            current = current.getNext()
        return count 
    def search(self, item): 
        current = self.head        
        while current is not None: 
            if current.getData() == item:                
                return True 
            current = current.getNext()
        return False
    def remove(self, item): 
        current = self.head        
        previous = None        
        found = False 
        while current is not None and not found:
            if current.getData() == item:                
                found = True
            else:               
                previous = current
                current = current.getNext()
        if found: 
            if previous is None: 
                self.head = current.getNext()
            else:                
                previous.setNext(current.getNext()) 
        else: 
            raise ValueError("Value not found.")

    def insert(self, position, item):
        if position > self.size(): 
            raise IndexError("Index out of bounds.")
        new_node = Node(item)
        if position == 0:
            new_node.setNext(self.head)
            self.head = new_node
        else:
            current = self.head        
            previous = None        
            pos = 0
            while pos < position:              
                previous = current
                current = current.getNext()
                pos += 1  
            previous.setNext(new_node)           
            new_node.setNext(current)
    def index(self, item):
        current = self.head        
        pos = 0       
        while current is not None:
            if current.getData() == item:                
                return pos
            current = current.getNext()
            pos += 1
        return None  
    def pop(self, position=None): 
        if self.head is None:
            raise IndexError("Cannot pop from empty list.")
        if position is None:
            position = self.size() - 1  
        if position >= self.size() or position < 0:
            raise IndexError("Index out of bounds.")
        current = self.head 
        previous = None 
        pos = 0 
        while pos < position:
            previous = current
            current = current.getNext()
            pos += 1  
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getData()
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(new_node)
    def printList(self):
        current = self.head 
        while current is not None: 
            print(current.getData(), end=" ")  
            current = current.getNext()
        print()
ll = LinkedList() 
ll.add('l') 
ll.add('H') 
ll.insert(1, 'e') 
ll.append('l')
ll.append('o')
ll.printList()  
"""					"""
class Node:
    def __init__(self, cargo=None, next=None): 
        self.car = cargo
        self.cdr = next    
    def __str__(self): 
        return str(self.car)
    @staticmethod
    def display(lst): 
        current = lst
        while current:
            print(current, end=" -> ")
            current = current.cdr
        print("nil") 
node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)
Node.display(node1) 
"""				"""
import datetime
from operator import attrgetter
class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height
    def __repr__(self):
        return self.name
persons = [
    Person("John Cena", datetime.date(1992, 9, 12), 175),
    Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
    Person("Jon Skeet", datetime.date(1991, 7, 6), 185)
]
persons.sort(key = lambda p: (p.name, p.birthday, p.height))
print(persons)
persons.sort(key = attrgetter('name'))     
persons.sort(key = attrgetter('birthday'))
persons.sort(key = attrgetter('height'))   
print(persons)
"""                """
class Rectangle(object):    
    def __init__(self, width, height, pos = None, color = 'blue'):
        if pos is None: 
            pos = [0, 0]
        self.width = width; self.height = height
        self.pos = pos; self.color = color
    def area(self):       
        return self.width  * self.height
r1 = Rectangle(5, 3)
r2 = Rectangle(7, 8, 'red')
r1.pos[0] = 4
print(r1.pos, r2.pos, r1.color, r2.color)
print(r1.area())
"""                """
class C:
    x = 2 
    def __init__(self, y):
        self.y = y  
print(C.x)  
c1, c2 = C(3), C(4)
print(c1.x, c1.y, c2.x, c2.y)  
print(c2.x, C.x)  
class D:
    def __init__(self, item):
        self.x = [] 
        self.x.append(item)
d1, d2 = D(1), D(2)
d2 = D(2)
print(d1.x, d2.x)
print(d2.x) 
try:
    print(D.x)
except AttributeError as e:
    print(e) 
"""					"""
class Country(object):
    def __init__(self):
        self.cities = [] 
    def addCity(self, city):
        self.cities.append(city)
class City(object):
    def __init__(self, numPeople):
        self.people = []  
        self.numPeople = numPeople
        self.country = None  
    def addPerson(self, person):
        self.people.append(person)  
    def join_country(self, country):
        self.country = country 
        country.addCity(self)  
        for i in range(self.numPeople):
            Person(i).join_city(self)
        return self  
class Person(object):
    def __init__(self, ID):
        self.ID = ID  
        self.city = None  
    def join_city(self, city):
        self.city = city  
        city.addPerson(self)  
    def people_in_my_country(self):
        if self.city and self.city.country:
            return sum(len(c.people) for c in self.city.country.cities)
        return 0  
US = Country()
NYC = City(10).join_country(US)  
SF = City(5).join_country(US) 
if US.cities and US.cities[0].people:
    print(US.cities[0].people[0].people_in_my_country())  
print(dir(list))
print([m for m in dir(list) if not m.startswith('__')])
