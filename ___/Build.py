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
cnt = col.Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(cnt, cnt.keys(), cnt.values(), cnt.items(), cnt["a"])
dic = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
print(col.Counter(dic.values()).most_common())
print(col.Counter(dic.values()).most_common(2))
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
from operator import truediv, floordiv
test = [ (10, 8), (10, -8), (-10, 8), (-10, -8), 
    (7.5, 2.5), (9, 3), (0, 5), (5, 2)]
for a, b in test:
    print(f"truediv({a}, {b}) = {truediv(a, b)}")
    print(f"floordiv({a}, {b}) = {floordiv(a, b)}")
    assert truediv(a, b) == a / b 
    assert floordiv(a, b) == a // b
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
print(random.randint(0, 5))  
print(random.random())  
print(random.random() * 100)  
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

import ply.lex as lex
tokens = [ 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', ]
t_ignore = ' \t'; t_PLUS = r'\+'
t_MINUS = r'\-'; t_TIMES = r'\*'
t_DIV = r'/'; t_LPAREN = r'\('
t_RPAREN = r'\)'
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return None
def t_error(t):
    print("Invalid Token: ", t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
data = "3 + 4 * (5 - 2)"
lexer.input(data)
while True:        
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)
import ply.lex as lex  
class MyLexer(object):                    
    def build(self, **kwargs):           
        self.lexer = lex.lex(module = self, **kwargs)       
    def test(self, data):           
        self.lexer.input(data)          
        for token in iter(self.lexer.token, None):
            print(token)
m = MyLexer() 
m.build(); m.test("3 + 4 * 2")
import ply.yacc as yacc
from calclex import tokens
def p_binary_operators(p):
    if p[2] == '+':         
        p[0] = p[1] + p[3]      
    elif p[2] == '-':         
        p[0] = p[1] - p[3]      
    elif p[2] == '*':         
        p[0] = p[1] * p[3]     
    elif p[2] == '/':         
        p[0] = p[1] / p[3]
def p_expression_plus(p):
    p[0] = p[1] + p[3]
def p_expression_minus(p):
    p[0] = p[1] - p[3]
def p_expression_term(p):
    p[0] = p[1]
def p_term_times(p):
    p[0] = p[1] * p[3]
def p_term_div(p): 
    p[0] = p[1] / p[3]
def p_term_factor(p): 
    p[0] = p[1]
def p_factor_num(p): 
    p[0] = p[1]
def p_factor_expr(p): 
    p[0] = p[2]
def p_error(p):
    print("Syntax error in input!")
parser = yacc.yacc()
while True: 
    try:      
        s = input('calc > ') 
    except EOFError: 
        break
    if not s: continue   
    result = parser.parse(s)
    print(result)
import threading
def foo():
    print("Hello")
threading.Thread(target = foo)
t.start(); t.join()
import time
class sleepy(threading.Thread):
    def run(self):
        time.sleep(5)
        print("ciao")
if __name__ = "__main__":
    t = sleepy()
    t.start(); t.join()
import threading, time
def func(i):
    return i * i
def other(m, i):
    return m + i
def process():
    for j in range(100):
        result = 0
    for i in range(100000):            
        result = other(result, func(i))
"""def process():
    time.sleep(2) """
start = time.time()
process() 
print("One run took %.2fs" % (time.time() - start))
start = time.time()
threads = [threading.Thread(target = process) for _ in range(4)]
for t in threads:    
    t.start()
for t in threads:   
    t.join() 
print("Four runs took %.2fs" % (time.time() - start))
import multiprocessing, time
def func(i):
    return i * i
def other(m, i):
    return m + i
def process():
    for j in range(100):
        result = 0
    for i in range(100000):            
        result = other(result, func(i))
start = time.time()
process() 
print("One run took %.2fs" % (time.time() - start))
start = time.time()
processes = [multiprocessing.Process(target = process)for _ in range(4)] 
for p in processes:    
    p.start() 
for p in processes:    
    p.join()
print("Four runs took %.2fs" % (time.time() - start))
"""                """
import threading, os
def process():  
    print("Pid is %s, thread id is %s" % (os.getpid(), threading.current_thread().name))
threads = [threading.Thread(target = process) for _ in range(4)] 
for t in threads:  
    t.start()
for t in threads:   
    t.join()
import multiprocessing
import os
def process():    
    print("Pid is %s" % (os.getpid(),))
processes = [multiprocessing.Process(target = process) for _ in range(4)]
for p in processes:   
    p.start() 
for p in processes:   
    p.join()

import threading, pprint
obj = {}
obj_lock = threading.Lock()
def objify(key, val):
    print(f"[{threading.current_thread().name}] Obj has {len(obj)} values")
    with obj_lock:
        obj[key] = val
    print(f"[{threading.current_thread().name}] Obj now has {len(obj)} values")
ts = [threading.Thread(target = objify, args = (str(n), n)) for n in range(4)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print("Obj final result:")
pprint.pprint(obj)
"""                """
from threading import Thread
import time
def countdown(n):    
    while n > 0:       
        n -= 1
def run_threads():
    COUNT = 10000000 
    t1 = Thread(target = countdown, args = (COUNT//2,))
    t2 = Thread(target = countdown, args = (COUNT//2,))
    start = time.time()
    t1.start() ; t2.start()
    t1.join() ;t2.join()
    end = time.time()
    print(f"Time taken: {end - start} seconds")
run_threads()
import math
from multiprocessing import Process
def calc_fact(num):
    result = math.factorial(num)  
    print(f"Factorial of {num} is computed successfully.")
if __name__ == "__main__":
    num = 600000  
    print(f"About to calculate: {num}!")
    p = Process(target = calc_fact, args = (num,))  
    p.start()
    p.join()
    print("Factorial calculation completed.")
import bisect, timeit
def index_sorted(sorted_seq, value):   
    i = bisect.bisect_left(sorted_seq, value)    
    if i != len(sorted_seq) and sorted_seq[i] == value:        
        return i    
    raise ValueError(f"Value {value} not found in list")
lst = [i for i in range(1, 100000, 3)]
print(index_sorted(lst, 97285))  
try:
    print(index_sorted(lst, 4))  
except ValueError as e:
    print(e)
print("Timing with bisect.bisect_left:")
print(timeit.timeit(lambda: index_sorted(lst, 97285), number=10000))
print("Timing with list.index():")
print(timeit.timeit(lambda: lst.index(97285), number=10000))
print("Timing with bisect for missing value:")
print(timeit.timeit(lambda: index_sorted(lst, 4), number=10000))
print("Timing with list.index() for missing value:")
try:
    print(timeit.timeit(lambda: lst.index(4), number=10000))
except ValueError:
    print("ValueError occurred (as expected)")

import numpy as np
import calc  
import sys
print(sys.path)
a = np.array([0, 3, 4, 3, 5, 4, 7])
print("Occurrences of 3:", np.sum(a == 3)) 
print("10 + 2 =", calc.add(10, 2))
List = [1, 4, True, 800, "python", 27, "hello"]
print(random.choice(List)) 
import datetime
from datetime import date
import time
print(time.time())  
print(date.fromtimestamp(454554))

import typing as typ
point = typ.NamedTuple('point', [('x', int), ('y', int)])
p = point(3, 4); print(p.x, p.y)
x, y = p; print(x, y, p)
T = typ.TypeVar("T")
def getelement(elements: typ.Sequence[T], default: typ.Optional[T] = None) -> T:
    if elements:
        return elements[0]
    if default is not None:
        return default
    raise ValueError("Sequence is empty and no default value provided")
lst = [1, 2, 3]
strlst = ["apple", "banana", "cherry"]
empty_list = []
print(getelement(lst), getelement(strlst))  
print(getelement(empty_list, default = "No elements"))  
