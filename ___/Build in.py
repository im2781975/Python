import collections
counts = collections.Counter([1, 2, 3])
counts = collections.Counter('Happy Birthday')
counts = collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-Iam'.split())
counts = collections.Counter({'a': 4, 'b': 2, 'c': -2, 'd': 0})
counts['c'] = -3
counts.update({'a': 3, 'b' : 3})
counts.update({'a': 2, 'c' : 2})
counts.subtract({'a': 3, 'b': 3, 'c': 3})
print(sum(counts.values()))
print(counts.elements())
"""                    """
from collections import deque
deq = deque('ghi')
deq.append('j')
deq.appendleft('bc')
deq.pop()
deq.popleft()
deq.extend('jkl')
deq.extendleft('mnk')
print(deque.reverse(deq))
deq.rotate(1)
deq.rotate(-1)
print(list(deq))
print(list(reversed(deq)))
print('h' in deq)
for val in deq:
    print(val.upper(), end = "")
deq.clear()
deq = deque([1, 2, 3])
deq.popleft()
deq.appendleft(5)
dl = deque()
#dl = deque(maxlen = 100)
dl.append(2)
dl.extend([6, 7])
dl.extendleft([-2, -1])
dl.pop_left()
dl.remove(1)
dl.reverse()
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
    return distance
graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
result = bfs(graph, 1)
print(result)
"""					"""
import operator
print(operator.pow(4, 2), operator.__pow__(4, 3))
x, y = 2, 6
print(x.__pow__(y), y.__rpow__(x))
import math
print(math.pow(2, 2), math.pow(2, -2), math.pow(-2, 5), math.e ** 2, math.exp(2), math.exp(10), math.exp(10).real)
print(math.e ** 1e-3 - 1, math.exp(1e-3) - 1, math.expm1(1e-3), math.e ** 1e-15 - 1, math.exp(1e-15) - 1, math.expm1(1e-15))
"""                    """
import math
from decimal import Decimal
import cmath
print(math.sqrt(9), math.sqrt(11.11), Decimal('6.25').sqrt())
print(cmath.sqrt(4), cmath.sqrt(-4))
"""                    """
def modularInverse(x, p):
    return pow(x, p - 2, p)
print([modularInverse(x, 13) for x in range(1,13)])
"""                    """
import heapq
num = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, num))
print(heapq.nsmallest(4, num))
heapq.heapify(num)
heapq.heappop(num)
print(num)
"""				"""
people = [{'firstname': 'John', 'lastname': 'Doe', 'age': 30},    
        {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},    
        {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},  
        {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},    
        {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},    
        {'firstname': 'John', 'lastname': 'Roe', 'age': 45}]
oldest = heapq.nlargest(2, people, key = lambda s : s['age'])
youngest = heapq.nsmallest(2, people, key = lambda s : s['age'])
print(oldest, youngest)
"""				"""
from operator import *
print(add(a, b), sub(a, b), truediv(a, b), floordiv(a, b))
"""            """
import math
a, b = 1, 2
print(math.sinh(a), math.cosh(a), math.atan(math.pi), math.hypot(a, b), math.degree(a), math.radians(57.29577951308232))
"""            """
import cmath
complex_num = cmath.sqrt(-1) 
while complex_num: 
    print(complex_num)  
"""				"""
import random
num = random.randint(0, 12)
print(str(num))
"""				"""
import random
laugh = ["Aa", "Bb", " Cc"]
random.shuffle(laugh)
print(laugh, random.choice(laugh))
print(random.sample(laugh, 1), random.sample(laugh, 2), random.sample(laugh, 3))
print(random.randint(1, 100), random.randrange(100), random.randrange(20, 50), random.randrange(10, 20, 3), random.random(), random.uniform(1, 8))
random.seed(5)
print(random.randrange(0, 10), random.randrange(0, 10))
random.seed(5)
print(random.randrange(0, 10))
"""            """
state = random.getstate()
random.setstate(state)
print(state)
random.seed(None)
random.seed()
"""            """
probability = 0.3
if random.random() < probability:    
    print("Decision with probability 0.3") 
else:    
    print("Decision with probability 0.7")
    
from Queue import Queue 
question_queue = Queue() 
for x in range(1,10):   
    temp_dict = ('key', x)    
    question_queue.put(temp_dict) 
while(not question_queue.empty()):    
    item = question_queue.get()    
    print(str(item))
"""				"""
import itertools
lst = [1, 2, 3, 4, 5]
print(list(itertools.combinations(lst, 3)))
"""            """
def IsEven(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
print(list(itertools.dropwhile(IsEven, lst)))
print(list(itertools.takewhile(IsEven, lst)))
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
        for x in iterable:
            yield x
            
print(list(itertools.takewhile(IsEven, lst)) + list(itertools.dropwhile(IsEven, lst)))
"""            """
from itertools import zip_longest, islice
a = [i for i in range(5)]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in zip_longest(a, b):
    x, y = i
    print(x, y)
for i in zip_longest(a, b, fillvalue='Hogwash!'):
    x, y = i
    print(x, y)
def fetch_paged_results():
    for i in range(50):
        yield f"Result {i + 1}"
limit = 20
for data in islice(fetch_paged_results(), limit):
    print(data, end = " ")
"""            """
print()
def gen():
    n = 0
    while n < 20:
        n += 1
        yield n
for part in itertools.islice(gen(), 3):    
    print(part, end = " ")
"""            """
print()
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
def testGroupBy(lst):    
    groups = itertools.groupby(lst, key=lambda x: x[1])   
    for key, group in groups:        
        print(key, list(group))
testGroupBy(lst)
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)] 
testGroupBy(lst)
print()
"""            """
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)] 
groups = itertools.groupby(lst, key=lambda x: x[1])
for key, group in sorted(groups):
    print(key, list(group))
for key, group in sorted((key, list(group)) for key, group in groups):   
    print(key, list(group))
lst = [1, 2, 3]
print(itertools.permutations(a), itertools.permutations(a, 2))
for i in itertools.repeat('over-and-over', 3):
    print(i, end = " ")
print()
"""            """
import operator
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4, 5], func = operator.mul)))
print(itertools.cycle('ABCD'))
it = itertools.cycle('abc123')
print([next(it) for i in range(1, 10)])
"""            """
from itertools import product
for x, y in product(range(10), range(10)):
    print (x, y, end = " ")
print()
for x in range(10):
    for y in range(10):
        print (x, y, end = " ")
print()
its = [range(10)] * 2
for x, y in product(*its):
    print(x, y, end = " ")
print()
lst = [1, 2, 3, 4]
tis = ['a', 'b', 'c']
print(product(lst, tis))
for i in product(lst, tis):
    print(i, end = " ")
print()
for num in itertools.count():
    if num > 20:
        break
    print(num, end = " ")
print()
for num in itertools.count(start = 10, step = 4):
    print(num)
    if num > 20:
        break
print()
"""            """
from itertools import chain
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['a', 'b', 'c'])
print(' '.join(chain(a, b)))
from functools import partial
def func(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x
res = partial(func, 1, 1, 1)
print(res(2))
import functools
import locale
res = sorted(['A', 'S', 'F', 'D'],key = functools.cmp_to_key(locale.strcoll))
print(res)
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
"""            """
from functools import reduce
def factorial(n):
    return reduce(lambda a, b: (a * b), range(1, n + 1)
"""				"""
import dis
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)
print(dir(fib.__code__))
print(dis.dis(fib))
import random
import inspect
print(inspect.getsource(random.randrange))
print(inspect.getdoc(random.randint))
import sys
print("Error", file = sys.stderr) 
print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)
import sys
char_count = sys.stdout.write('hello world ?\\n')
byte_count = sys.stdout.buffer.write(b'hello world \\xf0\\x9f\\x90\\x8d\\n')
import codecs codecs.decode('1deadbeef4', 'hex')
codecs.encode(b'\x1d\xea\xdb\xee\xf4', 'hex')
codecs.encode(b'\x1d\xea\xdb\xee\xff', 'hex').decode('ascii')
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
data = ser.read()
data = ser.read(size=5)
data = ser.readline()
data = ser.read(ser.inWaiting())
ser.read(ser.inWaiting)

from serial.tools import list_ports
list_ports.comports() 
import turtle 
ninja = turtle.Turtle()
ninja.speed(10) 
for i in range(180):   
    ninja.forward(100)   
    ninja.right(30)    
    ninja.forward(20)   
    ninja.left(60)    
    ninja.forward(50)    
    ninja.right(30)    
    ninja.penup()    
    ninja.setposition(0, 0)   
    ninja.pendown()   
    ninja.right(2) 
turtle.done()
list_object=[1,1,2,3,5,8,'a','e','i','o','u'] 
save(list_file,list_object) 
new_list=load(list_file) 
print(new_list)
"""				"""
import hashlib 
m = hashlib.md5()
m.update("Nobody inspects") 
m.update(" the spammish repetition") 
m.digest()
m.hexdigest()
m.digest_size
m.block_size
hashlib.md5("Nobody inspects the spammish repetition").hexdigest() 'bb649c83dd1ea5c9d9dec9a18df0ffe9'
h = hashlib.new('ripemd160') 
h.update("Nobody inspects the spammish repetition") 
h.hexdigest()
