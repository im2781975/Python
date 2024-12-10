def greet_two(greeting):
    print(greeting)
greet_two("Howdy")

def greet_two(greeting="Howdy"):    print(greeting)
greet_two()

def many_types(x):    
    if x < 0:        
        return "Hello!"    
    else:        
        return 0 
print(many_types(1)) 
print(many_types(-1))

def func(*args):
    for i in args:        
        print(i) 
func(1, 2, 3)  
list_of_arg_values = [1, 2, 3] 
func(*list_of_arg_values)

def func(**kwargs):   
    for name, value in kwargs.items():        
        print(name, value)
func(value1=1, value2=2, value3=3)

my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)       

def fn(**kwargs):   
    print(kwargs)   
    f1(**kwargs)
def f1(**kwargs):   
    print(len(kwargs))
fn(a=1, b=2)

def greeting():    
    return "Hello"
print(greeting())
greet_me = lambda: "Hello"
print(greet_me())

strip_and_upper_case = lambda s: s.strip().upper() 
strip_and_upper_case("  Hello   ")

greeting = lambda x, *args, **kwargs: 
    print(x, args, kwargs)
greeting('hello', 'world', world='world')

sorted( [" foo ", "    bAR", "BaZ    "], key=lambda s: s.strip().upper()) 
sorted( [" foo ", "    bAR", "BaZ    "], key=lambda s: s.strip())
sorted( map( lambda s: s.strip().upper(), [" foo ", "    bAR", "BaZ    "]))
sorted( map( lambda s: s.strip(), [" foo ", "    bAR", "BaZ    "]))

def foo(msg):    
    print(msg) 
greet = lambda x = "hello world": foo(x) 
greet()

def make(action='nothing'):
    return action
make("fun")
make(action="sleep")
make() 

def give_me_five():   
    return 5
print(give_me_five()) 
print(give_me_five() + 10)

def give_me_another_five():    
    return 5    
    print('This statement will not be printed. Ever.')
print(give_me_another_five())

def give_me_two_fives():   
    return 5, 5  
first, second = give_me_two_fives()
print(first) 
print(second)

def makeInc(x):  
    def inc(y):
        return y + x  
    return inc
incOne = makeInc(1)
incFive = makeInc(5)
incOne(5) 
incFive(5)

def makeInc(x):  
    def inc(y): 
        x += y  
        return x 
    return inc
incOne = makeInc(1) 
incOne(5)

def makeInc(x): 
    def inc(y):     
        nonlocal x   
        x += y       
        return x  
    return inc 
incOne = makeInc(1) 
incOne(5)

def fibonacci(n):    
    def step(a,b):        
        return b, a+b    
    a, b = 0, 1    
    for i in range(n):       
        a, b = step(a, b) 
    return a
    
def make_adder(n):    
    def adder(x):        
        return n + x   
    return adder
add5 = make_adder(5)
add6 = make_adder(6) 
add5(10) 
add6(10)

def repeatedly_apply(func, n, x):    
    for i in range(n):      
        x = func(x)   
    return x 
repeatedly_apply(add5, 5, 1)

def cursing(depth): 
    try:   
        cursing(depth + 1) 
    except RuntimeError as RE:    
        print('I recursed {} times!'.format(depth))
        
cursing(0)
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1) 
print(lambda_factorial(4))

def factorial(n):    
    if n == 0:       
        return 1    
    else:       
        return n*factorial(n-1)
factorial(0)
factorial(1) 
factorial(2) 
factorial(3)
factorial = lambda n: 1 if n == 0 else n*factorial(n-1)

def divide(dividend, divisor):
    print(dividend / divisor)
divide(10, 2)
divide(divisor=2, dividend=10)

def unpacking(a, b, c=45, d=60, *args, **kwargs):
    print(a, b, c, d, args, kwargs)
unpacking(1, 2)
unpacking(1, 2, 3, 4)
unpacking(1, 2, c=3, d=4)
unpacking(1, 2, d=4, c=3)
pair = (3,)
unpacking(1, 2, *pair, d=4)
unpacking(1, 2, d=4, *pair)
args_list = [3]
unpacking(1, 2, *args_list, d=4)
unpacking(1, 2, d=4, *args_list)
pair = (3, 4)
unpacking(1, 2, *pair)
unpacking(1, 2, 3, 4, *pair)
args_list = [3, 4]
unpacking(1, 2, *args_list)
unpacking(1, 2, 3, 4, *args_list)
arg_dict = {'c':3, 'd':4}
unpacking(1, 2, **arg_dict)
arg_dict = {'d':4, 'c':3}
unpacking(1, 2, **arg_dict)
arg_dict = {'c':3, 'd':4, 'not_a_parameter': 75}
unpacking(1, 2, **arg_dict)

def func(myList):   
    for item in myList:       
        print(item)
func([1,2,3,5,7])
aList = ['a','b','c','d'] 
func(aList)

s=lambda x:x*x s(2)  
name_lengths = map(len, ["Mary", "Isla", "Sam"]) 
print(name_lengths) 

total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)  

arr=[1,2,3,4,5,6]
[i for i in filter(lambda x:x>4,arr)]

def raise(x, y): 
    if y in (3,4,5): 
        return x**y 
    raise NumberNotInRangeException("You should provide a valid exponent")
from functors import partial 
raise_to_three = partial(raise, y=3) 
raise_to_four = partial(raise, y=4) 
raise_to_five = partial(raise, y=5)

def print_args(func):    
    def inner_func(*args, **kwargs):        
        print(args)      
        print(kwargs)
        return func(*args, **kwargs)   
    return inner_func
@print_args 
def multiply(num_a, num_b):    return num_a * num_b
print(multiply(3, 5))

class Decorator(object):    
    """Simple decorator class."""   
    def __init__(self, func):        self.func = func    
    def __call__(self, *args, **kwargs):        
        print('Before the function call.')        
        res = self.func(*args, **kwargs)        
        print('After the function call.')       
        return res
@Decorator 
def testfunc():    
    print('Inside the function.') 
testfunc()
    
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

from types import MethodType 
class CountCallsDecorator(object): 
    def __init__(self, func):
        self.func = func 
        self.ncalls = 0    # 
    def __call__(self, *args, **kwargs): 
        self.ncalls += 1 
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
a.do_something() 
a.do_something.ncalls  
b = Test() 
b.do_something()
b.do_something.ncalls 

def decoratorfactory(message):    def decorator(func):       
        def wrapped_func(*args, **kwargs):            
            print('The decorator wants to tell you: {}'.format(message))            
            return func(*args, **kwargs)        
        return wrapped_func  
    return decorator
@decoratorfactory('Hello World') 
def test():   
    pass 
test()

def decoratorfactory(*decorator_args, **decorator_kwargs):    
    class Decorator(object):        def __init__(self, func):           
            self.func = func        
        def __call__(self, *args, **kwargs):            
            print('Inside the decorator with arguments {}'.format(decorator_args))           
            return self.func(*args, **kwargs)           
    return Decorator
@decoratorfactory(10) 
def test():   
    pass 
test()

def decorator(func):    # Copies the docstring, name, annotations and module to the decorator    
    @wraps(func)    
    def wrapped_func(*args, **kwargs):        
        return func(*args, **kwargs)    
    return wrapped_func 
@decorator 
def test():   
    pass 
test.__name__

class Decorator(object):    
    def __init__(self, func):       
        self._wrapped = wraps(func)(self)          
    def __call__(self, *args, **kwargs):        
        return self._wrapped(*args, **kwargs)
@Decorator 
def test():   
    """Docstring of test."""
    pass 
test.__doc__

import time 
def timer(func):    
    def inner(*args, **kwargs):
        t1 = time.time()        
        f = func(*args, **kwargs)        
        t2 = time.time()        
        print 'Runtime took {0} seconds'.format(t2-t1)        
        return f    
    return inner
@timer 
def example_function():   
example_function()
