class Dog:
    x = "molla"; y = "vai"
    def func(self):
        print("i am ", self.x)
        print("i am ", self.y)
    
dog = Dog()
print(dog.x, dog.y); dog.func()
"""                    """
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"MyError has occurred with value: {repr(self.value)}"
try:
    raise MyError(3 * 2)
except MyError as error:
    print('A New Exception occurred:', error.value)
    print('Error details:', str(error))
finally:
    print('Exception handling completed.')
"""                    """
class Error(Exception):
    pass
class zerodivision(Error):
    pass
while True:
    try:
        num = int(input("Enter a number (or type 'exit' to quit): "))
        if num == 0:
            raise zerodivision
        print(f"You entered: {num}")
        break 
    except zerodivision:
        print("Input value is zero, try again!\n")
    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        break
"""                    """
class Error(Exception):
    """Base class for other exceptions."""
    pass
class TransitionError(Error):
    """Raised when an operation is not allowed due to an invalid state transition."""
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.nex = nex
        self.msg = msg
    def __str__(self):
        return f"Transition from {self.prev} to {self.nex} is not allowed: {self.msg}"
try:
    raise TransitionError(2, 3 * 2, "Not Allowed")
except TransitionError as error:
    print('Exception occurred:', error.msg)
    print('Full Error Details:', error)
"""                        """
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise Networkerror("Error")
except Networkerror as e:
    print(e.args)
"""						"""
class student:
    depart = 'CSE'
    def __init__(self, roll):
        self.roll = roll
a = student(103)
b = student(104)
print(a.depart, b.depart, a.roll, b.roll, student.depart)
"""                    """
class operation:
    def __init__(self, value):
        self.value = value
    def __and__(self, other):
        print("And operator ")
        if isinstance(other, operation):
            return self.value & other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __or__(self, other):
        print("OR operator ")
        if isinstance(other, operation):
            return self.value | other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __xor__(self, other):
        print("XOR operator ")
        if isinstance(other, operation):
            return self.value ^ other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __lshift__(self, other):
        print("left shift operator ")
        if isinstance(other, operation):
            return self.value << other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __rshift__(self, other):
        print("right shift operator ")
        if isinstance(other, operation):
            return self.value >> other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value
if __name__ == "__main__":
    a, b = operation(10), operation(20)
    print(a & b, a | b, a ^ b, a << b, a >> b, ~a)
"""                    """
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [ 
    person('Alice', 25), person('Bob', 30), person('Charlie', 22) ]
filtered = list(filter(lambda person: person.age > 25, people))
for person in filtered:
    print(person.name, person.age)

"""            Abstract            """
from abc import ABC, abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
class triangle(polygon):
    def sides(self):
        print("3 sides")
class pentagon(polygon):
    def sides(self):
        print("5 sides")
class hexagon(polygon):
    def sides(self):
        print("6 sides")
class quadrilateral(polygon):
    def sides(self):
        print("4 sides")
t = triangle(); t.sides();
p = pentagon(); p.sides();
h = hexagon(); h.sides();
q = quadrilateral(); q.sides();
"""                        """
class animal(ABC):
    #@abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print("walk & run")
class snake(animal):
    def move(self):
        print("crawl")
class dog(animal):
    def move(self):
        print("bark")
class lion(animal):
    def move(self):
        print("roar")
h = human(); h.move();
s = snake(); s.move();
d = dog(); d.move();
l = lion(); l.move();
print(issubclass(lion, animal))
print(isinstance(lion(), animal))
"""                    """
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
"""					"""
from abc import ABC
class B(ABC):
    def D(self):
        print("Abstract Base Class")

class C(B):
    def D(self):
        super().D()
        print("subclass ")
r = C(); r.D()
"""                    """
import abc
from abc import ABC, abstractmethod
class parent(ABC):
    @abc.abstractproperty
    def func(self):
        return "parent class"
class child(parent):
    @property
    def func(self):
        return "child class"
try:
    r = parent()
    print(r.func)
except Exception as err:
    print(err)
r = child()
print(r.func)
"""						"""
class dog:
    animal = 'dog'
    def __init__(self, breed):
        self.breed = breed
    def setcolor(self, color):
        self.color = color
    def getcolor(self):
        return self.color
dg = dog("pug")
dg.setcolor("brown")
print(dg.getcolor())
"""            Decorator            """
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
@decorator
def hello_decorator():
    print("Gfg")
hello_decorator()
"""                    """
def hello_decorator(func):
    def inner():
        print("before function execution")
        func()
        print("after function execution")
    return inner
def used():
    print("inside the function !!")
used = hello_decorator(used)
used()
"""						"""
def singleton(func):
    instance = [None]    
    def wrapper(*args, **kwargs):        
        if instance[0] is None:            
            instance[0] = func(*args, **kwargs)        
        return instance[0]    
    return wrapper
@singleton 
class delta:   
    x = 2    
    def __init__(self):       
        print("Created!") 
obj = delta()
obj = delta() 
print(obj.x)                
obj.x = 3 
print(delta().x)
"""                    """
import time
import math
def calculateTime(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in :", func.__name__, end - begin)
    return inner
@calculateTime
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
factorial(10)
"""                    """
def decorator(func):
    def inner(*args, **kwargs):
        print("before Execution")
        val = func(*args, **kwargs)
        print("after Execution")
        return val
    return inner
@decorator
def sumof(a, b):
    print("Inside the function")
    return a + b
a, b = 1, 2
print("Sum =", sumof(a, b))
"""                    """
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 
def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
@decor1
@decor
def num(): 
    return 10
@decor
@decor1
def num2():
    return 10
print(num()); print(num2())
"""                    """
def decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper
@decorator
def greet():
    print("Hello!")
greet()
"""                    """
def prin(func):    
    def inner(*args, **kwargs):        
        print(args)      
        print(kwargs)
        return func(*args, **kwargs)   
    return inner
@prin
def multiply(a, b):   
    return a * b
print(multiply(3, 5))
"""                    """
class Decorator(object):    
    def __init__(self, func):        
        self.func = func    
    def __call__(self, *args, **kwargs):
        print('Before call')
        res = self.func(*args, **kwargs)
        print('After call.')       
        return res
@Decorator 
def test():    
    print('Inside the function.') 
test()
"""                    """
from types import MethodType 
class Decorator(object):  
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs): 
        print('Inside the decorator.')
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls): 
        return self if instance is None else MethodType(self, instance)
class Test(object): 
    @Decorator
    def __init__(self): 
        pass
a = Test()
"""                    """
from types import MethodType 
class CountCallsDecorator(object): 
    def __init__(self, func):
        self.func = func 
        self.ncalls = 0  
    def __call__(self, *args, **kwargs): 
        self.ncalls += 1  
        # Increment call count
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls): 
        return self if instance is None else MethodType(self, instance)
class Test(object):
    def __init__(self): 
        pass 
    @CountCallsDecorator
    def do_something(self): 
        return 'something was done' 
a = Test() 
print(a.do_something())  
print(f"Calls from 'a': {Test.do_something.ncalls}")  
a.do_something()
print(f"Calls from 'a' after second call: {Test.do_something.ncalls}")

b = Test() 
print(b.do_something())  
print(f"Total calls from 'a' and 'b': {Test.do_something.ncalls}")
"""                    """
def decoratorfactory(message):  
    def decorator(func):       
        def wrapped_func(*args, **kwargs):            
            print('The decorator wants to tell you: {}'.format(message))  
            return func(*args, **kwargs)
        return wrapped_func  
    return decorator
@decoratorfactory('Hello World') 
def test():   
    print("Inside the test function.")
test()
"""                    """
def decoratorfactory(*decorator_args, **decorator_kwargs):    
    class Decorator(object):        
        def __init__(self, func):           
            self.func = func        
        def __call__(self, *args, **kwargs):            
            print('Inside the decorator with arguments {}'.format(decorator_args))           
            return self.func(*args, **kwargs)           
    return Decorator
@decoratorfactory(10) 
def test():   
    pass 
test()
"""                    """
from functools import wraps
def decorator(func):    
    @wraps(func)  
    def wrapped_func(*args, **kwargs):        
        return func(*args, **kwargs)    
    return wrapped_func 
@decorator 
def test():   
    """This is the docstring of the test function."""
    pass 
print(test.__name__)  
print(test.__doc__)   
"""                    """
from functools import wraps
class Decorator(object):    
    def __init__(self, func):
        self.func = func
        wraps(func)(self)  
    def __call__(self, *args, **kwargs): 
        return self.func(*args, **kwargs)
@Decorator 
def test():   
    """Docstring of test."""
    print("Inside the test function.")
print(test.__doc__); print(test.__name__) ; test()
"""   Decorator     """
import time 
def timer(func):    
    def inner(*args, **kwargs):
        t1 = time.time()        
        f = func(*args, **kwargs) 
        t2 = time.time()       
        print('Runtime took {0} seconds'.format(t2 - t1))  
        return f    
    return inner
@timer 
def example_function():   
    time.sleep(1)  
example_function()
"""					"""
def shout(txt):
    return txt.upper()
print(shout("hello"))
func = shout
print(func("hello"))
"""                    """
def shout(text): 
    return text.upper() 
def whisper(text): 
    return text.lower() 
def greet(func): 
    greeting = func(" I was at some place other than my body ") 
    print (greeting) 
greet(shout); greet(whisper) 
"""                    """
def adder(x):
    def add(y):
        return x + y
    return add
tmp = adder(15)
print(tmp(10))
"""            Encapsulation            """
class base:
    def __init__(self):
        self._a = 2
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a)
        self._a = 3
        print(self._a)
x = base(); print(x._a)
y = derived(); print(y._a)
"""                    """
class Base: 
    def __init__(self): 
        self.a = "Here i am"
        self.__c = "where are you"
class Derived(Base): 
    def __init__(self):
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 
obj = Base() 
print(obj.a)
"""            Inheritance            """
class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def disp(self):
        print(self.name, self.id)
class emp(person):
    def printf(self):
        print("Employe class")
info = emp("Hasan", 108)
info.disp(); info.printf()
"""                    """
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("Molla")  
print(emp.getName(), emp.isEmployee())
emp = Employee("Vai")  
print(emp.getName(), emp.isEmployee())
"""                    """
class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)
class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, id)
a = Employee('Rahul', 886012, 200000, "Intern")
a.display()
"""                    """
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
class Student(Person):
    def __init__(self, name, age):
        super().__init__("Rahul", age)
        self.sName = name
        self.sAge = age
    def displayInfo(self):
        print(self.sName, self.sAge)
obj = Student("Mayank", 23)
obj.display(); obj.displayInfo()
"""                    """
class Base1(object):
    def __init__(self):
        self.x = "Molla"
        print("Base1")
class Base2(object):
    def __init__(self):
        self.y = "vai"
        print("Base2")
class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def disp(self):
        print(self.x, self.y)
ob = Derived()
ob.disp()
"""                    """
class Base(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    def getAge(self):
        return self.age
class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
    def getAddress(self):
        return self.address
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
"""            Inheritance            """
class C(object):
    def __init__(self):
        self.c = 21
        self.__d = 42
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
        #super().__init__()
obj = D(); print(obj.c, obj._C__d)
"""            Iterator            """
class Test:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.x = 10
        return self
    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1;
        return x
for i in Test(15):
    print(i, end = " ")
for i in Test(5):
    print(i, end = " ")
"""            Polymarphizm"""
class India():
    def capital(self):
        print("New Delhi.")
    def language(self):
        print("Hindi.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington, D.C.")
    def language(self):
        print("English.")
    def type(self):
        print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
obj_ind = India()
obj_usa = USA()
func(obj_ind)
func(obj_usa)
"""                    """
class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
bird = Bird()
spr = sparrow()
ost = ostrich()
bird.intro(); bird.flight()
spr.intro(); spr.flight()
ost.intro(); ost.flight()
"""                    """
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
"""                    """
class Animal:
    def sound(self):
        return "Some sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
dog = Dog()
print(dog.sound())
"""                    """
class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Circle(Shape):
    def draw(self):
        return "Drawing a circle"
class Square(Shape):
    def draw(self):
        return "Drawing a square"
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.draw())
"""                    """
def make_sound(animal):
    return animal.sound()
class Dog:
    def sound(self):
        return "Bark"
class Cat:
    def sound(self):
        return "Meow"
animals = [Dog(), Cat()]
for animal in animals:
    print(make_sound(animal))
"""                    """
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Car(Vehicle):
    def move(self):
        return "Car is moving"
class Bike(Vehicle):
    def move(self):
        return "Bike is moving"
vehicles = [Car(), Bike()]
for vehicle in vehicles:
    print(vehicle.move())
class person(object): 
    species = "Homo Sapiens"            
    def __init__(self, name):      
        self.name = name            
    def __str__(self):                 
        return self.name 
    def rename(self, renamed):
        self.name = renamed 
        print("Now my name is {}".format(self.name))
Aa = person("Aa")
Bb = person("Bb")
print(Aa.species, Bb.species)
print(Bb.__str__(), Bb)
Bb.rename("Cc");
"""                    """
import inspect
class A(object):    
    def func(self, x):      
        return 2 * x 
a = A()
print(inspect.isfunction(A.func))
print(inspect.ismethod(A.func))
print(A.func(a, 7))
print(a.func(20))
"""            """
class delta(object):    
    multiplier = 2    
    @classmethod    
    def func(cls, x):       
        return cls.multiplier * x  
    @staticmethod    
    def gun(name):       
        print("Hello, %s" % name)
print(delta.func, delta.func(12))
print(delta.gun, delta.gun("world"))
d = delta()
d.multiplier = 1337 
print(delta.multiplier, d.multiplier)
print(d.func, d.func(10))
"""                    """
class rectangle():    
    def __init__(self, weidth, hight): 
        self.weidth = weidth 
        self.hight = hight
    def area(self):       
        return self.weidth * self.hight  
    def perimeter(self):        
        return 2 * (self.weidth + self.hight)
class square(rectangle):   
    def __init__(self, side):  
        super(square, self).__init__(side, side)       
        self.side = side
r = rectangle(4, 9)
s = square(2)
print(r.area(), r.perimeter(), s.area(), s.perimeter())
print(issubclass(square, rectangle))
print(isinstance(r, rectangle), isinstance(r, square), isinstance(s, rectangle), isinstance(s, square))
"""					"""
class delta(object):   
    def __init__(self, num):        
        self.num = num   
    def __add__(self, other):        
        return delta(self.num + other.num)
def get(self):    
    return self.num
x = delta(56); delta.get = get
print(x.get, x.get())
"""                """
class person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
    def greet(self):
        print("Hello, my name is " + self.full_name + ".")
    def is_adult(self):
        return self.age >= 18
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.first_name}! You are now {self.age} years old.")
    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
        self.full_name = self.first_name + " " + self.last_name
        print(f"Your name has been updated to {self.full_name}.")
x = person("John", "Doe", 25)
y = person("Alice", "Smith", 16)
x.greet(); y.greet()  
print(f"Is {x.first_name} an adult? {x.is_adult()}")  
print(y.birthday())
x.update_last_name("Johnson"); x.greet()
"""                    """
class person(object):
    def __init__(self, fname, age, lname=None):
        if lname is None:
            parts = fname.split(" ", 1)
            if len(parts) == 2:
                self.first_name, self.last_name = parts
            else:
                self.first_name = parts[0]
                self.last_name = ' '
        else:
            self.first_name = fname
            self.last_name = lname
        self.full_name = self.first_name + " " + self.last_name if self.last_name else self.first_name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.full_name + ".")
x = person("John Doe", 25); x.greet()
"""            """
class person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError("Full name must include both first and last names.")
        first_name, last_name = name.split(" ", 1)  
        return cls(first_name, last_name, age)
    def greet(self):
        print("Hello, my name is " + self.full_name + ".")
bob = person("Bob", "Bobberson", 42)
alice = person.from_full_name("Alice Henderson", 31)
bob.greet(); alice.greet()  
"""						"""
class Foo(object):
    def foo_method(self):
        print("Foo Method")
class Bar(object):
    def bar_method(self):
        print("Bar Method")
class FooBar(Foo, Bar):
    def foo_method(self):
        super().foo_method()
        print("FooBar's Override of foo_method")
    def bar_method(self):
        super().bar_method()
        print("FooBar's Extension of bar_method")
foobar = FooBar()
foobar.foo_method(); foobar.bar_method()   
print(FooBar.__mro__)
"""                    """
class Foo(object):        
    def __init__(self):            
        print("foo init")    
class Bar(object):        
    def __init__(self):            
        print("bar init")    
class FooBar(Foo, Bar):        
    def __init__(self):            
        print("foobar init")          
        super(FooBar, self).__init__()
a = FooBar()
print(isinstance(a, FooBar), isinstance(a, Foo)
print(isinstance(a, Bar), FooBar.__mro__))
"""                    """
class MyClass(object):    
    def __init__(self):       
        self.ing = ""  
    @property    
    def string(self):        
        return self.ing
    @string.setter    
    def string(self, val):        
        assert isinstance(val, str), "Give me a string, not a %r!" % type(val)        
        self.ing = val 
    @string.deleter    
    def string(self):        
        self.ing = None
mc = MyClass() 
mc.string = "String!" 
print(mc.string); del mc.string
"""                    """
class Character(object):    
    def __init__(self, name, max_hp):
        self._name = name        
        self._hp = max_hp        
        self._max_hp = max_hp
    @property    
    def hp(self):        
        return self._hp
    @hp.setter
    def hp(self, value): 
        self._hp = value
    @property 
    def name(self):
        return self._name  
    def take_damage(self, damage): 
        self.hp -= damage  
        self.hp = 0 if self.hp < 0 else self.hp  
    @property 
    def is_alive(self): 
        return self.hp != 0  
    @property 
    def is_wounded(self): 
        return self.hp < self._max_hp if self.hp > 0 else False  
    @property 
    def is_dead(self): 
        return not self.is_alive  
bilbo = Character('Bilbo Baggins', 100) 
print(bilbo.hp)  
bilbo.hp = 200  
print(bilbo.hp, bilbo.is_alive, bilbo.is_wounded, bilbo.is_dead)  
bilbo.take_damage(50)  
print(bilbo.hp, bilbo.is_alive)  
print(bilbo.is_wounded, bilbo.is_dead)
