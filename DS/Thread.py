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
