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

def fib(a=0, b=1):   
    """Generator that yields Fibonacci numbers. `a` and `b` are the seed values"""   
    while True:      
        yield a        
        a, b = b, a + b 
f = fib() 
print(', '.join(str(next(f)) for _ in range(10)))

def find_and_transform(sequence, predicate, func):  
    for element in sequence:        
        if predicate(element):            
            return func(element)    
    raise ValueError
item = find_and_transform(my_sequence, my_predicate, my_func)
item = next(my_func(x) for x in my_sequence if my_predicate(x))

def first(generator): 
    try: 
        return next(generator) 
    except StopIteration:
        raise ValueError
        
for x, y in zip(a,b): 
    print(x,y)
    
from functools import reduce
def add(s1, s2):  
    return s1 + s2
reduce(add, asequence)
import operator 
reduce(operator.add, asequence)
reduce(add, asequence, 10)

def multiply(s1, s2):    
    print('{arg1} * {arg2} = {res}'.format(arg1=s1, arg2=s2, res=s1*s2))    
    return s1 * s2
asequence = [1, 2, 3]
cumprod = reduce(multiply, asequence, 5)
print(cumprod)
cumprod = reduce(multiply, asequence)
print(cumprod)

import operator
reduce(operator.mul, [10, 5, -3])

import operator
reduce(operator.and_, [False, True, True, True])
reduce(operator.or_, [True, False, False, False])

names = ['Fred', 'Wilma', 'Barney']
map(len, names)

from itertools import imap
imap(len, names)
list(map(len, names))
[len(item) for item in names]
(len(item) for item in names) 

list(map(abs, (1, -1, 2, -2, 3, -3)))
map(lambda x:x*2, [1, 2, 3, 4, 5])

def to_percent(num):   
    return num * 100
list(map(to_percent, [0.95, 0.75, 1.01, 0.1]))

from functools import partial 
from operator import mul
rate = 0.9
dollars = {'under_my_bed': 1000,           'jeans': 45,           'bank': 5000}
sum(map(partial(mul, rate), dollars.values()))

def average(*args):   
    return float(sum(args)) / len(args) 
measurement1 = [100, 111, 99, 97] 
measurement2 = [102, 117, 91, 102] 
measurement3 = [104, 102, 95, 101]
list(map(average, measurement1, measurement2, measurement3))

def median_of_three(a, b, c):    return sorted((a, b, c))[1]
list(map(median_of_three, measurement1, measurement2, measurement3, measurement3))

import operator 
measurement1 = [100, 111, 99, 97] 
measurement2 = [102, 117]
list(imap(operator.sub, measurement1, measurement2))
list(imap(operator.sub, measurement2, measurement1)) 
list(map(operator.sub, measurement1, measurement2))
list(map(operator.sub, measurement2, measurement1))

insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x: x + ' is an insect' print(list(map(f, insects)))
print(list(map(len, insects)))

carnivores = ['lion', 'tiger', 'leopard', 'arctic fox'] 
herbivores = ['african buffalo', 'moose', 'okapi', 'parakeet'] 
omnivores = ['chicken', 'dove', 'mouse', 'pig']
def animals(w, x, y, z):    
    return '{0}, {1}, {2}, and {3} ARE ALL ANIMALS'.format(w.title(), x, y, z)
import pprint pprint.pprint(list(map(animals, insects, carnivores, herbivores, omnivores)))
