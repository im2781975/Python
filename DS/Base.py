def input_number(msg, err_msg=None):    
while True:       
    try:
        return float(raw_input(msg))        
    except ValueError:            
        if err_msg is not None:                
            print(err_msg) 
def input_number(msg, err_msg=None):
    while True:        
        try:            
            return float(input(msg))       
        except ValueError:      
            if err_msg is not None:                
            print(err_msg)
print("Hello, ", end="\n") 
print("World!")
print("Hello, ", end="") 
print("World!")
print("Hello, ", end="<br>")
print("World!")
print("Hello, ", end="BREAK")
print("World!")

try:   
    x = 1.0 / 0.0    
    print(x) 
except ZeroDivisionError:   
    print("Division by zero")

from collections import Counter
c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
c["a"]
Counter({"e": "e"}) 

from collections import Counter
adict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
Counter(adict.values()).most_common()
Counter(adict.values()).most_common(1)
Counter(adict.values()).most_common(2)

alist = [1, 2, 3, 4, 1, 2, 1, 3, 4]
alist.count(1)
atuple = ('bear', 'weasel', 'bear', 'frog')
atuple.count('bear')
atuple.count('fox')

astring = 'thisisashorttext' 
astring.count('t')
astring.count('th')
astring.count('is')
astring.count('text')
from collections import Counter 
Counter(astring)

import numpy as np 
a=np.array([0,3,4,3,5,4,7]) >>> 
print np.sum(a==3)

d1 = {1:[]}
d2 = d1.copy()
d1 is d2
d1[1] is d2[1]

import copy 
c = [[1,2]]
d = copy.copy(c) 
c is d
c[0] is d[0]

import copy 
c = [[1,2]] 
d = copy.deepcopy(c) 
c is d
c[0] is d[0]

l1 = [1,2,3]
l2 = l1[:] 
l2
l1 is l2

s1 = {()} 
s2 = s1.copy() 
s1 is s2
s2.add(3)
