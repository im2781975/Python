import itertools
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2)) 
b = list(itertools.combinations(a, 3))
print(b)

def is_even(x): 
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44] 
result = list(itertools.dropwhile(is_even, lst))
print(result)

def dropwhile(predicate, iterable):    
    iterable = iter(iterable)    
    for x in iterable:        
        if not predicate(x):            
            yield x            
            break    
        for x in iterable:        
            yield x
result = list(itertools.takewhile(is_even, lst)) + list(itertools.dropwhile(is_even, lst))

from itertools import zip_longest 
a = [i for i in range(5)]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 
for i in zip_longest(a, b):  
    x, y = i 
    print(x, y)
for i in zip_longest(a, b,fillvalue='Hogwash!'):   
    x, y = i  
    print(x, y)

results = fetch_paged_results()
limit = 20 
for data in itertools.islice(results, limit):   
    print(data)
    
def gen():    
    n = 0    
    while n < 20:        
        n += 1        
        yield n
for part in itertools.islice(gen(), 3):    
    print(part)
#itertools.islice(iterable, 1, 30, 3)

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
def testGroupBy(lst):    
    groups = itertools.groupby(lst, key=lambda x: x[1])   
    for key, group in groups:        
        print(key, list(group))
testGroupBy(lst)
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)] 
testGroupBy(lst)

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)] 
groups = itertools.groupby(lst, key=lambda x: x[1])
for key, group in sorted(groups):
    print(key, list(group))
    
groups = itertools.groupby(lst, key=lambda x: x[1]) 
for key, group in sorted((key, list(group)) for key, group in groups):   
    print(key, list(group))
    
def is_even(x):    
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44] 
result = list(itertools.takewhile(is_even, lst))
print(result)

def takewhile(predicate, iterable):    
for x in iterable:        
    if predicate(x):            
        yield x        
    else:            
        break
result = list(itertools.takewhile(is_even, lst)) + list(itertools.dropwhile(is_even, lst))

a = [1,2,3]
list(itertools.permutations(a))
list(itertools.permutations(a, 2))
set(itertools.permutations(a))

import itertools 
for i in itertools.repeat('over-and-over', 3):
    print(i)
    
import itertools as it
import operator
list(it.accumulate([1,2,3,4,5]))
list(it.accumulate([1,2,3,4,5], func=operator.mul))

import itertools as it
it.cycle('ABCD')
cycle_iterator = it.cycle('abc123')
[next(cycle_iterator) for i in range(0, 10)]

for x, y in itertools.product(xrange(10), xrange(10)):   
    print x, y

for x in xrange(10):
    for y in xrange(10):        
        print x, y
        
its = [xrange(10)] * 2 
for x,y in itertools.product(*its):    
    print x, y
    
from itertools import product 
 a=[1,2,3,4] 
b=['a','b','c'] 
 product(a,b)
for i in product(a,b): 
    print i
    
for number in itertools.count():    
    if number > 20:       
        break    
    print(number)
    
for number in itertools.count(start=10, step=4):    
    print(number)   
    if number > 20:       
        break

from itertools import chain 
a = (x for x in ['1', '2', '3', '4']) 
b = (x for x in ['x', 'y', 'z']) ' '.join(chain(a, b))

from functools import partial
def f(a, b, c, x):     
    return 1000*a + 100*b + 10*c + x
g = partial(f, 1, 1, 1) 
print g(2)

import functools
import locale
sorted(["A", "S", "F", "D"], key=functools.cmp_to_key(locale.strcoll))

@lru_cache(maxsize=None) 
def fibonacci(n): 
    if n < 2:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)
    
from functools import reduce
def factorial(n):
    return reduce(lambda a, b: (a*b), range(1, n+1))

from Queue import Queue 
question_queue = Queue() 
for x in range(1,10):   
    temp_dict = ('key', x)    
    question_queue.put(temp_dict) 
while(not question_queue.empty()):    
    item = question_queue.get()    
    print(str(item))
    
