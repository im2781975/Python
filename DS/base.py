begin, *tail = "Hello" print(begin)
print(tail)

person = ('John', 'Doe', (10, 16, 2016)) 
*_, (*_, year_of_birth) = person 
print(year_of_birth)

{*range(4), 4, *(5, 6, 7)}
iterable = [1, 2, 3, 4, 5]
print(iterable)
print(*iterable)

tail = {'y': 2, 'z': 3} 
{'x': 1, **tail}

dict1 = {'x': 1, 'y': 1}
dict2 = {'y': 2, 'z': 3} 
{**dict1, **dict2}

map(lambda (x, y): x + y, zip(range(5), range(5)))
map(lambda x: x[0] + x[1], zip(range(5), range(5)))

s = u'Café'
b = 'Lorem ipsum'
isinstance(s, basestring)

s = b'Cafe'          
s = 'Café'.encode()
isinstance(s, str)

from __future__ import unicode_literals 
print(repr("hi"))

b"abc"[0] == 97
b"abc"[0:1] == b"a"

print("Hi, my name is Łukasz Langa.") 
print(u"Hi, my name is Łukasz Langa."[::-1]) 
print("Hi, my name is Łukasz Langa."[::-1])

print "Hello World"
print "No newline"
print()    
print("Hello World")            
print("No newline", end="")      
print("Error", file=sys.stderr) 
print("Comma", "separated", "output", sep=",")  
print("A", "B", "C", sep="")    
print("Flush this", flush=True)   
print(1, 2, 3)                  
print((1, 2, 3))   

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print('foo', 'bar', sep='~') 
print('foo', 'bar', sep='.')
print('foo', 'bar', end='!')
print('foo', end='~') 
print('bar')

print(range(1, 10))
print(isinstance(range(1, 10), range))
print(range(1, 10)[3:7])
print(range(1, 10).count(5))
print(range(1, 10).index(7))
print(list(range(1, 10)))

from past.builtins import xrange 
for i in xrange(10**8):   
    pass

x = 'hello world!' vowels = [x for x in 'AEIOU']
print (vowels)
print(x)

x = 'hello world!' 
vowels = [] 
for x in 'AEIOU':    
    vowels.append(x)
print(x)

[1, 2] > 'foo'
(1, 2) > 'foo'
[1, 2] > (1, 2)
100 < [1, 'x'] < 'xyz' < (1, 'x')

l = [7, 'x', (1, 2), [5, 6], 5, 8.0, 'y', 1.2, [7, 8], 'z'] 
sorted(l)

list = [1, 'hello', [3, 4], {'python': 2}, 'stackoverflow', 8, {'python': 3}, [5, 6]] 
sorted(list, key=str)

g = (i for i in range(0, 3))
next(g)  
next(g)  
next(g) 

s = filter(lambda x: x.isalpha(), 'a1b2c3')
s = map(lambda x: x * x, [0, 1, 2])
s = zip([0, 1, 2], [3, 4, 5])

it = filter(lambda x: x.isalpha(), 'a1b2c3')
''.join(it)
it = filter(lambda x: x.isalpha(), 'a1b2c3')
 ''.join(it)
it = map(lambda x: x * x, [0, 1, 2])
list(it)
it = zip([0, 1, 2], [3, 4, 5])
list(it)

2**1024
print(-(2**1024))
type(2**1024)

my_list = [1, 2, 3, 4, 5] 
import operator, functools 
functools.reduce(operator.truediv, my_list)

map(str, [1, 2, 3, 4, 5])
type(_)
map(str, [1, 2, 3, 4, 5]) 
list(_)

list(map(lambda x, y, z: (x, y, z), [1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))
import itertools 
list(itertools.zip_longest([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))
 [str(i) for i in [1, 2, 3, 4, 5]]
 
round(1.5)  
round(0.5) 
round(-0.5)  
round(-1.5)  
round(4.8)

import sys
char_count = sys.stdout.write('hello world ?\\n')
byte_count = sys.stdout.buffer.write(b'hello world \\xf0\\x9f\\x90\\x8d\\n')

exec('code')
exec('code', global_vars) 
exec('code', global_vars, local_vars)

import codecs codecs.decode('1deadbeef4', 'hex')
codecs.encode(b'\x1d\xea\xdb\xee\xf4', 'hex')
codecs.encode(b'\x1d\xea\xdb\xee\xff', 'hex').decode('ascii')

d = {'a': 0, 'b': 1, 'c': 2, '!': 3} 
for key in d.keys():    
    if key.isalpha():       
        del d[key]
        
class MyClass:    
    def __bool__(self):        
        return False
my_instance = MyClass() 
print(bool(MyClass))      
print(bool(my_instance)) 

class A(object):    
    @property    
    def get(self):        
        raise IOError
    class B(object):   
    @property    
    def get(self):        
        return 'get in b' 
a = A() 
b = B()

print 'a hasattr get: ', hasattr(a, 'get')
print 'b hasattr get', hasattr(b, 'get')

try:   
    a.get 
except AttributeError:    
    print("no get property!")

p = getattr(a, "get", None) 
if p is not None:   
    print(p) 
else:    
    print("no get property!")

