

def unpacking(a, b, c = 45, d = 60, *args, **kwargs):
    print(a, b, c, d, args, kwargs)
unpacking(1, 2)
unpacking(1, 2, 3, 4)
unpacking(1, 2, c = 3, d = 4)
unpacking(1, 2, d = 4, c = 3)
pair = (3,)
unpacking(1, 2, *pair, d = 4)
unpacking(1, 2, d = 4, *pair)
args_list = [3]
unpacking(1, 2, *args_list, d = 4)
unpacking(1, 2, d = 4, *args_list)
pair = (3, 4)
unpacking(1, 2, *pair)
unpacking(1, 2, 3, 4, *pair)
args_list = [3, 4]
unpacking(1, 2, *args_list)
unpacking(1, 2, 3, 4, *args_list)
arg_dict = {'c' : 3, 'd' : 4}
unpacking(1, 2, **arg_dict)
arg_dict = {'d' : 4, 'c' : 3}
unpacking(1, 2, **arg_dict)
arg_dict = {'c' : 3, 'd' : 4, 'not_a_parameter' : 75}
unpacking(1, 2, **arg_dict)
def to_percent(num):   
    return num * 100
print(list(map(to_percent, [0.95, 0.75, 1.01, 0.1])))

from functools import partial 
from operator import mul
rate = 0.9
dollars = {'under_my_bed': 1000,           'jeans': 45, 'bank': 5000}
print(sum(map(partial(mul, rate), dollars.values())))
def average(*args):   
    return float(sum(args)) / len(args) 
measurement1 = [100, 111, 99, 97] 
measurement2 = [102, 117, 91, 102] 
measurement3 = [104, 102, 95, 101]
print(list(map(average, measurement1, measurement2, measurement3)))
def func(myList):   
    for item in myList:       
        print(item)
func([1, 2, 3, 5, 7])
lst = ['a', 'b', 'c', 'd'] 
func(lst)
def median_of_three(a, b, c):    
    return sorted((a, b, c))[1]
print(list(map(median_of_three, measurement1, measurement2, measurement3, measurement3)))
import operator 
measurement1 = [100, 111, 99, 97] 
measurement2 = [102, 117]
print(list(imap(operator.sub, measurement1, measurement2)))
print(list(imap(operator.sub, measurement2, measurement1)))
print(list(map(operator.sub, measurement1, measurement2)))
print(list(map(operator.sub, measurement2, measurement1)))

insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x : x + ' is an insect' print(list(map(f, insects)))
print(list(map(len, insects)))

carnivores = ['lion', 'tiger', 'leopard', 'arctic fox'] 
herbivores = ['african buffalo', 'moose', 'okapi', 'parakeet'] 
omnivores = ['chicken', 'dove', 'mouse', 'pig']
def animals(w, x, y, z):    
    return '{0}, {1}, {2}, and {3} ARE ALL ANIMALS'.format(w.title(), x, y, z)
import pprint pprint.pprint(list(map(animals, insects, carnivores, herbivores, omnivores)))
"""				"""
class NumberNotInRangeException(Exception):
    pass
def raise_power(x, y): 
    if y in (3, 4, 5): 
        return x ** y 
    raise NumberNotInRangeException("You should provide a valid exponent (3, 4, or 5)")
from functools import partial  
raise_to_three = partial(raise_power, y = 3)
raise_to_four = partial(raise_power, y = 4)
raise_to_five = partial(raise_power, y = 5)
print(raise_to_three(2))  
print(raise_to_four(2))   
print(raise_to_five(2))   

def func(params):    
    for value in params:  
        print('Got value {}'.format(value))   
        if value == 1:  
            print(">>>> Got 1")  
            return  
        print("Still looping")   
    return "Couldn't find 1"  
result = func([5, 3, 1, 2, 8, 9])
print(result)
def function():
    for x in range(10):
        yield x ** 2
print(sum(i for i in range(10) if i % 2 == 0))
foo = [1, 2, 3, 4]
print(any(x == 0 for x in foo))
print(type(a > b for a in foo if a % 2 == 1))
print(sum((i for i in range(10) if i % 2 == 0)))
print(any((x == 0 for x in foo)))
result_type_gen = type((a > b for a in foo if a % 2 == 1))
print("Type of generator expression (parens):", result_type_gen)
from functools import reduce
lem = lambda x : x * x
print(lem(2))
print(map(len, ["Mary", "Isla", "Sam"]))
print(reduce(lambda a, x: a + x, [0, 1, 2, 3, 4]))
arr = [1, 2, 3, 4, 5, 6]
print([i for i in filter(lambda x : x > 4,arr)])
import operator
print(reduce(operator.mul, [10, 5, -3]))
print(reduce(operator.and_, [False, True, True, True]))
print(reduce(operator.or_, [True, False, False, False]))
def raise_power(x, y): 
    if y in (3, 4, 5): 
        return x ** y 
    raise ValueError("You should provide a valid exponent (3, 4, or 5)")
from functools import partial  
raise_to_three = partial(raise_power, y=3)
raise_to_four = partial(raise_power, y=4)
raise_to_five = partial(raise_power, y=5)
print(raise_to_three(2))  
print(raise_to_four(2))   
print(raise_to_five(2))   
try:
    print(raise_power(2, 6))
except ValueError as e:
    print(f"Error: {e}")

def print_args(func):    
    def inner_func(*args, **kwargs):    
        print("Arguments:", args)  
        print("Keyword arguments:", kwargs)  
        return func(*args, **kwargs)
    return inner_func
@print_args
def multiply(num_a, num_b):    
    return num_a * num_b 
print("Result of multiplication:", multiply(3, 5))
def func(params):    
    for value in params:        
        print ('Got value {}'.format(value))        
        if value == 1:            
            print (">>>> Got 1")      
            return        
        print ("Still looping")   
    return "Couldn't find 1" 
print(func([5, 3, 1, 2, 8, 9]))
def function():
    for x in range(10):
        yield x ** 2
print(sum(i for i in range(10) if i % 2 == 0))
foo = [1, 2, 3, 4]
print(any(x == 0 for x in foo))
print(type(a > b for a in foo if a % 2 == 1))
print(sum((i for i in range(10) if i % 2 == 0)))
print(any((x == 0 for x in foo)))
print(type((a > b for a in foo if a % 2 == 1)))
print(sum(i ** 2 for i in range(4)))
import itertools
def starting_from(n):    
    while True:        
        yield n        
        n += 1
natural = starting_from(1)
natural = itertools.count(1)
multiples_of_two = (x * 2 for x in natural) 
multiples_of_three = (x for x in natural if x % 3 == 0)
list(multiples_of_two)
first_five_multiples_of_three = [next(multiples_of_three) for _ in range(5)]
from itertools import islice 
multiples_of_four = (x * 4 for x in starting_from(1)) 
first_five_multiples_of_four = list(islice(multiples_of_four, 5))
next(natural)    
next(multiples_of_two)   
next(multiples_of_four) 
for idx, number in enumerate(multiplies_of_two): 
    print(number)    
    if idx == 9:
        break

import itertools
def fibonacci():    
    a, b = 1, 1   
    while True:        
        yield a        
        a, b = b, a + b
first_ten_fibs = list(itertools.islice(fibonacci(), 10))
def nth_fib(n):    
    return next(itertools.islice(fibonacci(), n - 1, n))
ninety_nineth_fib = nth_fib(99)

def accumulator():    
    total = 0    
    value = None    
    while True:      
        value = yield total      
        if value is None: 
            break       
        total += value
generator = accumulator()
next(generator)    
generator.send(1)    
generator.send(10)   
generator.send(100) 
next(generator)

def foob(x):    
    yield from range(x * 2)    
    yield from range(2)
print(list(foob(5)))
def fibto(n):   
    a, b = 1, 1    
    while True:      
        if a >= n: break        
        yield a        
        a, b = b, a + b
def usefib():  
    yield from fibto(10)  
    yield from fibto(20)
print(list(usefib()))
def xrange(n):   
    i = 0   
    while i < n:       
        yield i       
        i += 1
for i in xrange(10):   
    print(i)
a, b, c = xrange(3)
print(list(xrange(10)))
def nums():    
    yield 1
    yield 2    
    yield 3 
generator = nums()
next(generator, None)  
next(generator, None)  
next(generator, None)  
next(generator, None)  
def coroutine(func):    
    def start(*args,**kwargs):        
        cr = func(*args,**kwargs)        
        next(cr)        
        return cr    
    return start
@coroutine
def adder(sum = 0):   
    while True:       
        x = yield sum   
        sum += x
s = adder() 
s.send(1) 
s.send(2) 
def create_gen():      
    yield value    
    return
print(list(create_gen()))
def preorder_traversal(node):    
    yield node.value    
    for child in node.children:        
        yield from preorder_traversal(child)
generator = (i * 2 for i in range(3))
next(generator)  
next(generator)  
next(generator)  
next(generator)  
def fib(a = 0, b = 1):   
    while True:      
        yield a        
        a, b = b, a + b 
f = fib() 
print(', '.join(str(next(f)) for _ in range(10)))

def find_and_transform(sequence, predicate, func):  
    for element in sequence:        
        if predicate(element):  
            return func(element)
    raise ValueError("No element satisfies the predicate")  
my_sequence = [1, 2, 3, 4, 5]
my_predicate = lambda x: x % 2 == 0
my_func = lambda x: x * x  
item = find_and_transform(my_sequence, my_predicate, my_func)
print("Transformed item:", item)
item = next(my_func(x) for x in my_sequence if my_predicate(x))
print("Transformed item using generator:", item)
def first(generator): 
    try: 
        return next(generator)  
    except StopIteration:
        raise ValueError("Generator is empty")  
gen = (x for x in my_sequence if x % 2 == 0)  
print("First even number:", first(gen))
a = [1, 2, 3]
b = ['a', 'b', 'c']
for x, y in zip(a, b): 
    print(x, y)  

from functools import reduce
import operator
def add(s1, s2):  
    return s1 + s2
asequence = [1, 2, 3, 4, 5]
sum_result = reduce(add, asequence)
print("Sum of elements:", sum_result)
sum_result = reduce(operator.add, asequence)
print("Sum using operator.add:", sum_result)
sum_result_with_initial = reduce(add, asequence, 10)  
print("Sum with initial value 10:", sum_result_with_initial)
def multiply(s1, s2):    
    print(f'{s1} * {s2} = {s1 * s2}')  
    return s1 * s2
asequence = [1, 2, 3]
cumprod_with_initial = reduce(multiply, asequence, 5)
print("Cumulative product with initial value 5:", cumprod_with_initial)
cumprod_without_initial = reduce(multiply, asequence)
print("Cumulative product without initial value:", cumprod_without_initial)

myvar = None  
if myvar is not None: print("Not None")
if myvar is None: print("None")
sentinel = object()
def myfunc(var = sentinel):
    if var is sentinel: print("Yes")  
    else: print("No") 
myfunc()        
myfunc(42)      
myfunc(None)    

def outerFunction(text):
    def innerFunction():
        print(text)
    innerFunction()
if __name__ == '__main__':
    outerFunction('Hey!')
    
def outerFunction(text): 
    def innerFunction(): 
        print(text) 
    return innerFunction  
if __name__ == '__main__': 
    myFunction = outerFunction('Hey!') 
    myFunction() 

import logging 
logging.basicConfig(filename='example.log',
                    level=logging.INFO) 
def logger(func): 
    def log_func(*args): 
        logging.info( 
            'Running "{}" with arguments {}'.format(func.__name__,
                                                    args)) 
        print(func(*args)) 
    return log_func             
 
def add(x, y): 
    return x+y 
def sub(x, y): 
    return x-y 
add_logger = logger(add) 
sub_logger = logger(sub) 
 
add_logger(3, 3) 
add_logger(4, 5) 
sub_logger(10, 5) 
sub_logger(20, 10) 

def add(x, y):
    return x + y
addition = add
print(add, "\n", addition)
print(addition(8, 9))
"""                                    """
def greet():
    print("Hi")
def disp(other):
    print("Displayed")
    other()
disp(greet)
def louder(name):
    print(f"Hi {name.upper()} ")
def softer(name):
    print(f"Hi {name.lower()} ")
def hello(other, name1):
    print("display func")
    other(name1)
hello(louder, "molla")
hello(softer, "MOLLA")
"""                                    """
def hello(name):
    print("Executed")
    def greet():
        print("Aa")
    def welcome():
        print("Bb")
    if name == "molla":
        return greet
    else:
        return welcome
#hello("molla")
x = hello("molla")
x()
"""							"""
def divide(x, y):
    try:
        print(x // y)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
divide(9, 7)
divide(9, 0)
def divide(x, y):
    try:
        print(x // y)
    except Exception as e:
        print("The error is: ", e)
divide(3, "GFG") 
divide(3, 0) 
def AdivB(a, b):
    try:
        c = (a + b) // (a - b)
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AdivB(2, 3)
AdivB(3.0, 3.0)

try: 
    k = 5 // 0
    print(k) 
except ZeroDivisionError:    
    print("Can't divide by zero")
finally:
    print('This is always executed')
