import collections as col 
count = col.Counter([1, 5, 9, 20])
count = col.Counter(["Hi everyone", "where "])
count = col.Counter('Here - i - am!where are-u'.split())
count = col.Counter({'a' : 4, 'b' : 2, 'c' : -2, 'd' : 0})
count['c'] = -3
count.update({'a' : 3, 'b' : 3})
count.update({'a' : 2, 'c' : 2})
count.subtract({'a': 3, 'b': 3, 'c': 3})
print(sum(count.values()))
print(count.elements())
print(count.keys())
print(count.values())
print(count.items())
from collections import deque
deq = deque('ghi')
deq.append('a'); deq.pop()
deq.popleft(); deq.extend('jkl')
deq.extendleft('mnk'); deq.rotate(1)
deq.rotate(-1)
print(deque.reverse(deq), list(deq), list(reversed(deq)))
print('h' in deq)
print(deq)
for val in deq:
    print(val.upper(), end = " ")
deq.clear()
deq = deque([1, 2, 3])
deq.popleft(); deq.appendleft(5)
deq.clear()
deq = deque()
deq.append(2); deq.extend([6, 7])
deq.extendleft([-2, -1]); deq.popleft()
deq.remove(7); deq.reverse()
print(deq)
"""                """
def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                q.append(neighbor)
    return distances
graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
print(bfs(graph, 1))
import operator
print(operator.pow(4, 2), operator.__pow__(4, 3))
x, y = 2, 6; print(x.__pow__(y), y.__rpow__(x))
from operator import *
a, b = 30, 15
print(add(a, b), sub(a, b), truediv(a, b), floordiv(a, b))
import math
from decimal import Decimal
import cmath
print(math.pow(2, 2), math.pow(2, -2), math.pow(-2, 5), math.e ** 2, math.exp(2), math.exp(10), math.exp(10).real)
print(math.e ** 1e-3 - 1, math.exp(1e-3) - 1, math.expm1(1e-3), math.e ** 1e-15 - 1, math.exp(1e-15) - 1, math.expm1(1e-15))
print(Decimal('6.25').sqrt(), math.sqrt(9), math.sqrt(11.11))
print(cmath.sqrt(4), cmath.sqrt(-4))
a, b = 1, 2
print(math.sinh(a), math.cosh(a), math.atan(math.pi))
print(math.hypot(a, b), math.degrees(a), math.radians(57.29577951308232))
num = cmath.sqrt(-1)
while num:
    print(num)
    break
import heapq
num = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, num), heapq.nsmallest(4, num))
heapq.heapify(num); print(num)
heapq.heappop(num); print(num)
people = [{'firstname': 'John', 'lastname': 'Doe', 'age': 30},    
        {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},    
        {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},  
        {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},    
        {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},    
        {'firstname': 'John', 'lastname': 'Roe', 'age': 45}]
oldest = heapq.nlargest(2, people, key = lambda x : x['age'])
youngest = heapq.nsmallest(2, people, key = lambda x : x['age'])
print(oldest,"\n", youngest)

from queue import Queue
q = Queue()
for x in range(1, 10):
    dic = ('key', x)
    q.put(dic)
while(not q.empty()):
    print(str(q.get()))
import random
print(str(random.randint(0, 12)))
laugh = ["Aa", "Bb", " Cc"]; random.shuffle(laugh)
print(laugh, random.choice(laugh))
print(random.sample(laugh, 1), random.sample(laugh, 3))
print(random.randint(1, 100), random.randrange(100), random.randrange(20, 50))
print(random.randrange(10, 20, 3), random.random(), random.uniform(1, 8))
random.seed(5)
print(random.randrange(0, 10), random.randrange(0, 10))
random.seed(5); print(random.randrange(1, 10))
import random, inspect
print(inspect.getsource(random.randrange))
print(inspect.getdoc(random.randrange))

"""            """
state = random.getstate(); random.setstate(state)
print(state, end = " ")
random.seed(None); random.seed()
prob = 0.3
if random.random() < prob:
    print("Decision with probability 0.3")
else:    
    print("Decision with probability 0.7")
import functools, locale
print(sorted(['A', 'S', 'F', 'D'],key = functools.cmp_to_key(locale.strcoll)))
from functools import partial
def func(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x
res = partial(func, 1, 1, 1)
print(res(2))
import itertools
for num in itertools.count():
    if num > 20:
        break
    print(num, end = " ")
print()
for num in itertools.count(start = 10, step = 4):
    print(num, end = " ")
    if num > 20:
        break
print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))
def gen():
    n = 0
    while n < 20:
        n += 1; yield n
for part in itertools.islice(gen(), 3):   
    print(part, end = " ")
    
def testGroupBy(lst):    
    groups = itertools.groupby(lst, key = lambda x : x[1])   
    for key, group in groups:        
        print(key, list(group))
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)] 
testGroupBy(lst)
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]  
lst.sort(key = lambda x : x[1])  
groups = itertools.groupby(lst, key = lambda x : x[1])  
group_list = [(key, list(group)) for key, group in groups]
for key, group in group_list:
    print(key, group)
for key, group in sorted(group_list):   
    print(key, group)
lst = [1, 2, 3]
print(list(itertools.permutations(lst)))  
print(list(itertools.permutations(lst, 2)))   
for i in itertools.repeat('over-and-over', 3):
    print(i, end=" ")
from itertools import dropwhile, takewhile
def IsEven(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
print(list(dropwhile(IsEven, lst)))
print(list(takewhile(IsEven, lst))) 
def custom_dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x  
            break
    yield from iterable  
print(list(custom_dropwhile(IsEven, lst)))
print(list(takewhile(IsEven, lst)) + list(dropwhile(IsEven, lst)))
from itertools import zip_longest, islice
a = [i for i in range(5)]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in zip_longest(a, b):
    x, y = i; print(x, y)
for i in zip_longest(a, b, fillvalue='Hogwash!'):
    x, y = i; print(x, y)
def fetch():
    for i in range(50):
        yield f"Result {i + 1}"
limit = 20
for data in islice(fetch(), limit):
    print(data, end = " ") 
import operator
print(list(itertools.accumulate([1, 2, 3, 4])))
print(list(itertools.accumulate([1, 2, 3, 4], func = operator.mul)))
print(itertools.cycle('ABCDE'))
it = itertools.cycle('abc123')
print([next(it) for i in range(1, 10)])
from itertools import product
for x, y in product(range(10), range(10)):
    print(x, y, end = " ")
it = [range(10)] * 2
for x, y in product(*it):
    print(x, y, end = " ")
lst, tis = [1, 2, 3, 4], ['a', 'b', 'c']
print(product(lst, tis))
for i in product(lst, tis):
    print(i, end = " ")
from itertools import chain
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['a', 'b', 'c'])
print(' '.join(chain(a, b)))

import sys, codecs
print(sys.stdout.write('hello world ?\\n'))
print(sys.stdout.buffer.write(b'hello world \\xf0\\x9f\\x90\\x8d\\n'))
print(codecs.decode('1deadbeef4', 'hex'))
print(codecs.encode(b'\x1d\xea\xdb\xee\xf4', 'hex'))
print(codecs.encode(b'\x1d\xea\xdb\xee\xff', 'hex').decode('ascii'))
import hashlib 
m = hashlib.md5()
m.update("Nobody inspects".encode())  
m.update(" the spammish repetition".encode())  
print("MD5 Digest (Bytes):", m.digest()) 
print("MD5 Hex Digest:", m.hexdigest())   
print("Digest Size:", m.digest_size)     
print("Block Size:", m.block_size)        
md5_hash = hashlib.md5("Nobody inspects the spammish repetition".encode()).hexdigest()
print("MD5 Hash (Single Call):", md5_hash)
h = hashlib.new('ripemd160')  
h.update("Nobody inspects the spammish repetition".encode())  
print("RIPEMD-160 Hash:", h.hexdigest()) 
import pandas as pd
df = DataFrame()
df['customer_id'] = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
df['order_id'] = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6]
df['item'] = ['apples', 'chocolate', 'chocolate', 'coffee', 'coffee', 'apples', 'bananas', 'coffee', 'milkshake', 'chocolate', 'strawberry', 'strawberry']
print(df)
countOrders = lambda x : len(x.unique())
df['number_of_orders_per_cient'] = (df .groupby(['customer_id'])['order_id']  .transform(countOrders))
print(df)
def multipleOrder(_items): 
    multiple_item_bool = _items.duplicated(keep = False) 
    return(multiple_item_bool)
orders_df['item_duplicated_per_order'] = (orders_df .groupby(['order_id'])['item'] .transform(multipleOrder))
print(orders_df)

