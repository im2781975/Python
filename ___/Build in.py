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
"""				"""
import pandas as pd
df = DataFrame()
df['customer_id'] = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
df['order_id'] = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6]
df['item'] = ['apples', 'chocolate', 'chocolate', 'coffee', 'coffee', 'apples', 'bananas', 'coffee', 'milkshake', 'chocolate', 'strawberry', 'strawberry']
print(df)
countOrders = lambda x: len(x.unique())
df['number_of_orders_per_cient'] = (df .groupby(['customer_id'])['order_id']  .transform(countOrders))
print(df)

def multipleOrder(_items): 
    multiple_item_bool = _items.duplicated(keep=False) 
    return(multiple_item_bool)
orders_df['item_duplicated_per_order'] = (orders_df .groupby(['order_id'])['item'] .transform(multipleOrder))
print(orders_df)
"""				"""
import ply.lex as lex
tokens = [ 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', ]

t_ignore = ' \t'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*' 
t_DIV     = r'/' 
t_LPAREN  = r'\(' 
t_RPAREN  = r'\)'
def t_NUMBER( t ) :   
    r'[0-9]+'    
    t.value = int( t.value )    
    return t
def t_newline( t ):
    r'\n+'  
    t.lexer.lineno += len( t.value )
def t_error( t ):
    print("Invalid Token:",t.value[0]) 
    t.lexer.skip( 1 )
lexer = lex.lex()
lexer.input(data)
while True:        
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)
    
import ply.lex as lex  
class MyLexer(object):                    
    def build(self, **kwargs):           
        self.lexer = lex.lex(module=self, **kwargs)       
    def test(self, data):           
        self.lexer.input(data)          . 
        for token in self.lexer.token():              
            print(token)
m = MyLexer() 
m.build()          
m.test("3 + 4")

import ply.yacc as yacc
from calclex import tokens
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
        s = raw_input('calc > ') 
    except EOFError: 
        break
    if not s: continue   
    result = parser.parse(s)
    print(result)
    
def p_binary_operators(p):
    if p[2] == '+':         
        p[0] = p[1] + p[3]      
    elif p[2] == '-':         
        p[0] = p[1] - p[3]      
    elif p[2] == '*':         
        p[0] = p[1] * p[3]     
    elif p[2] == '/':         
        p[0] = p[1] / p[3]
def p_binary_operators(p):
    if p[2] == '+':          
        p[0] = p[1] + p[3]      
    elif p[2] == '-':          
        p[0] = p[1] - p[3]      
    elif p[2] == '*':         
        p[0] = p[1] * p[3]     
    elif p[2] == '/':          
        p[0] = p[1] / p[3]
"""				"""
import threading 
def foo(): 
    print ("Hello threading!")
threading.Thread(target = foo)
"""            """
import time
class Sleepy(Thread): 
    def run(self): 
        time.sleep(5) 
        print("Hello form Thread")
if __name__ == "__main__":   
    t = Sleepy()    
    t.start()   
    t.join()
    print("The main program continues to run in the foreground.")
"""            """
import requests
from threading import Thread
from queue import Queue
q = Queue(maxsize = 20)
def put_page_to_q(page_num):
    response = requests.get(f'http://some-website.com/page_{page_num}.html')
    q.put(response)
def compile(q):
    if not q.full():
        raise ValueError("Queue is not full")
    else:
        print("Done compiling!")
threads = []
for page_num in range(20):
    t = Thread(target=put_page_to_q, args=(page_num,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
compile(q)
"""            """
import threading 
import time
def process(): 
    time.sleep(2)
start = time.time() 
process() 
print("One run took %.2fs" % (time.time() - start))
start = time.time()
threads = [threading.Thread(target=process) for _ in range(4)]
for t in threads:    
    t.start()
for t in threads:   
    t.join() 
print("Four runs took %.2fs" % (time.time() - start))
"""            """
import threading 
import time
def somefunc(i): 
    return i * i 
def otherfunc(m, i):
    return m + i
def process():
    for j in range(100):
        result = 0
    for i in range(100000):            
        result = otherfunc(result, somefunc(i))
start = time.time() 
process() 
print("One run took %.2fs" % (time.time() - start))
start = time.time() 
threads = [threading.Thread(target=process) for _ in range(4)]
for t in threads:    
    t.start() 
for t in threads:   
    t.join() 
    print("Four runs took %.2fs" % (time.time() - start))
"""            """
import multiprocessing
import time 
def somefunc(i): 
    return i * i 
def otherfunc(m, i):
    return m + i
def process(): 
    for j in range(100):        
        result = 0 
        for i in range(100000):            
            result = otherfunc(result, somefunc(i))
start = time.time() 
process() 
print("One run took %.2fs" % (time.time() - start))
start = time.time()
processes = [multiprocessing.Process(target=process)for _ in range(4)] 
for p in processes:    
    p.start() 
for p in processes:    
    p.join()
print("Four runs took %.2fs" % (time.time() - start))
"""            """
import threading 
import os 
def process():  
    print("Pid is %s, thread id is %s" % (os.getpid(), threading.current_thread().name))
threads = [threading.Thread(target=process) for _ in range(4)] 
for t in threads:  
    t.start()
for t in threads:   
    t.join()
"""            """
import multiprocessing
import os
def process():    
    print("Pid is %s" % (os.getpid(),))
processes = [multiprocessing.Process(target=process) for _ in range(4)]
for p in processes:   
    p.start() 
for p in processes:   
    p.join()
"""            """
import threading
obj = {}
obj_lock = threading.Lock()
def objify(key, val):   
    print("Obj has %d values" % len(obj))    
    with obj_lock:        
        obj[key] = val    
    print("Obj now has %d values" % len(obj))
ts = [threading.Thread(target=objify, args=(str(n), n))] for n in range(4)] 
for t in ts:   
    t.start() 
for t in ts:
    t.join() 
    print("Obj final result:")
import pprint; pprint.pprint(obj)
"""            """
from threading import Thread
import time
def countdown(n):    
    while n > 0:       
        n -= 1
def run_threads():
    COUNT = 10000000 
    t1 = Thread(target=countdown, args=(COUNT//2,))
    t2 = Thread(target=countdown, args=(COUNT//2,))
    start = time.time()
    t1.start() ; t2.start()
    t1.join() ;t2.join()
    end = time.time()
    print(f"Time taken: {end - start} seconds")
run_threads()
"""            """
import math
from threading import Thread
def calc_fact(num):    
    result = math.factorial(num)  
    print(f"Factorial of {num} is: {result}")  
num = 600000
print("About to calculate: {}!".format(num))
t = Thread(target=calc_fact, args=[num]) 
t.start()  
t.join()  
"""				"""
import bisect
def index_sorted(sorted_seq, value):   
    i = bisect.bisect_left(sorted_seq, value)    
    if i != len(sorted_seq) and sorted_seq[i] == value:        
        return i    
    raise ValueError
lst = [i for i in range(1, 100000, 3)]
print(index_sorted(alist, 97285)) 
try:
    print(index_sorted(alist, 4))  
except ValueError as e:
    print(e)
%timeit index_sorted(alist, 97285)
%timeit alist.index(97285)
%timeit index_sorted(alist, 4)
%timeit alist.index(4)
"""				"""
import numpy as np
a = np.array([0, 3, 4, 3, 5, 4, 7])
print(np.sum(a == 3))
