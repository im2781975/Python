import threading def foo(): 
    print "Hello threading!"
my_thread = threading.Thread(target=foo)

import requests 
from threading import Thread
from queue import Queue
q = Queue(maxsize=20)
def put_page_to_q(page_num):   
    q.put(requests.get('http://some-website.com/page_%s.html' % page_num)
def compile(q):    
    if not q.full():       
        raise ValueError   
    else:       
        print("Done compiling!")
threads = [] 
for page_num in range(20):   
    t = Thread(target=requests.get, args=(page_num,))     
    t.start()     
    threads.append(t)
for t in threads:    
    t.join()
compile(q)

from threading import Thread 
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

import threading 
import os 
def process():  
    print("Pid is %s, thread id is %s" % (os.getpid(), threading.current_thread().name))
threads = [threading.Thread(target=process) for _ in range(4)] 
for t in threads:  
    t.start()
for t in threads:   
    t.join()

import multiprocessing
import os
def process():    
    print("Pid is %s" % (os.getpid(),))
processes = [multiprocessing.Process(target=process) for _ in range(4)]
for p in processes:   
    p.start() 
for p in processes:   
    p.join()

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

import multiprocessing 
plain_num = 0 
shared_num = multiprocessing.Value('d', 0) 
lock = multiprocessing.Lock()
def increment(): 
    global plain_num 
    with lock:   
        plain_num += 1  
        shared_num.value += 1
ps = [multiprocessing.Process(target=increment) for n in range(4)] 
for p in ps:    
    p.start() 
for p in ps:   
    p.join() 
print("plain_num is %d, shared_num is %d" % (plain_num, shared_num.value))

class Stack:   
    def __init__(self):       
        self.items = []
    def isEmpty(self): 
        return self.items == []
    def push(self, item):        
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self): 
        return self.items[-1]
    def size(self): 
        return len(self.items)
    def fullStack(self):
        return self.items
stack = Stack() 
print('Current stack:', stack.fullStack()). 
print('Stack empty?:', stack.isEmpty()) 
print('Pushing integer 1') stack.push(1) 
print('Pushing string "Told you, I am generic stack!"') 
stack.push('Told you, I am generic stack!') 
print('Pushing integer 3')
stack.push(3)
print('Current stack:', stack.fullStack()) 
print('Popped item:', stack.pop()) 
print('Current stack:', stack.fullStack()) 
print('Stack empty?:', stack.isEmpty())

def checkParenth(str):    
    stack = Stack()    
    pushChars, popChars = "<({[", ">)}]"   
    for c in str:        
        if c in pushChars:           
            stack.push(c)        
        elif c in popChars:           
            if stack.isEmpty():                
                return False         
            else:                
                stackTop = stack.pop()                # Checks to see whether the opening bracket matches the closing one               
                balancingBracket = pushChars[popChars.index(c)]               
                if stackTop != balancingBracket:                    
                    return False        
                    
        else:            
            return False    
    return not stack.isEmpty()
    
from threading import Thread 
import time 
def countdown(n):    
    while n > 0:      
        n -= 1 
COUNT = 10000000
t1 = Thread(target=countdown,args=(COUNT/2,))
t2 = Thread(target=countdown,args=(COUNT/2,)) 
start = time.time()
t1.start();t2.start() 
t1.join();t2.join() 
end = time.time() 
print end- start

import multiprocessing
import time 
def countdown(n):    
    while n > 0:       
        n -= 1
COUNT = 10000000
start = time.time() with multiprocessing.Pool as pool:    
    pool.map(countdown, [COUNT/2, COUNT/2])   
    pool.close()   
    pool.join()
    end = time.time() 
print(end-start)

from threading import Thread import time def countdown(n):    while n > 0:        n -= 1 COUNT = 10000000 t1 = Thread(target=countdown,args=(COUNT/2,)) t2 = Thread(target=countdown,args=(COUNT/2,)) start = time.time() t1.start();t2.start() t1.join();t2.join() end = time.time() print end-start

from threading import Thread import time def countdown(n):    while n > 0:        n -= 1 COUNT = 10000000 with nogil:    t1 = Thread(target=countdown,args=(COUNT/2,))    t2 = Thread(target=countdown,args=(COUNT/2,))    start = time.time()    t1.start();t2.start()    t1.join();t2.join()   end = time.time() print end-start

