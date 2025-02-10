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
def add(x, y):
    return (x+y)
def subtract(x, y):
    return (x-y)
import calc
print(calc.add(10, 2))
from math import *
print(sqrt(16))
print(factorial(6))
import sys
print(sys.path)
import math as mt
print(mt.sqrt(16))
print(mt.factorial(6))
import math
print(math.sqrt(25), math.pi, math.degrees(2), math.radians(60), math.sin(2), math.cos(0.5), math.tan(0.23), math.factorial(4))
import random
print(random.randint(0, 5))  
print(random.random())  
print(random.random() * 100)  
 
List = [1, 4, True, 800, "python", 27, "hello"]
print(random.choice(List)) 
import datetime
from datetime import date
import time
print(time.time())  
print(date.fromtimestamp(454554))
