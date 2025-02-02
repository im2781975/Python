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
