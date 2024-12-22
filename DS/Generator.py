def function():
    for x in range(10):
        yield x**2
sum(i for i in range(10)if i % 2 == 0) 
any(x = 0 for x in foo)                   
type(a > b for a in foo if a % 2 == 1)
sum((i for i in range(10) if i % 2 == 0))
any((x = 0 for x in foo)) 
type((a > b for a in foo if a % 2 == 1))

def integers_starting_from(n):    
    while True:        
        yield n        
        n += 1
natural_numbers = integers_starting_from(1)
natural_numbers = itertools.count(1)
multiples_of_two = (x * 2 for x in natural_numbers) 
multiples_of_three = (x for x in natural_numbers if x % 3 == 0)
list(multiples_of_two)
first_five_multiples_of_three = [next(multiples_of_three) for _ in range(5)]

from itertools import islice 
multiples_of_four = (x * 4 for x in integers_starting_from(1)) 
first_five_multiples_of_four = list(islice(multiples_of_four, 5))
next(natural_numbers)    
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
    while True:        # receive sent value        
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
list(foob(5))

def fibto(n):   
    a, b = 1, 1    
    while True:      
        if a >= n: break        
        yield a        
        a, b = b, a + b
def usefib():  
    yield from fibto(10)  
    yield from fibto(20)
list(usefib()) 

def xrange(n):   
    i = 0   
    while i < n:       
        yield i       
        i += 1
for i in xrange(10):   
    print(i)
a, b, c = xrange(3)
l = list(xrange(10))

def nums():    
    yield 1
    yield 2    
    yield 3 
generator = nums()
next(generator, None)  # 1 
next(generator, None)  # 2
next(generator, None)  # 3
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
values = list(create_gen())

def preorder_traversal(node):    
    yield node.value    
    for child in node.children:        
        yield from preorder_traversal(child)
        
generator = (i * 2 for i in range(3))
next(generator)  
next(generator)  
next(generator)  
next(generator)  

sum(i ** 2 for i in range(4)) 
