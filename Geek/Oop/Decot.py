# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello')) 
////
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

greet(shout) 
greet(whisper) 
////
# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

add_15 = create_adder(15) 

print(add_15(10)) 
////
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''
////
# defining a decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in 
    # which the argument is called
    
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")
        
    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()
///
# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)
////
def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
////
# code for testing decorator chaining 
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
  
print(num()) 
print(num2())
////
# Decorator example
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Annotation example
def greet(name: str) -> str:
    return f"Hello, {name}
////

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
