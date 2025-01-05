class AssignValue(object):    
    def __init__(self, value):        
        self.value = value 
my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value))

my_dict = {'key': 6, 'other_key': 7} 
print("My other key is: {0[other_key]}".format(my_dict)) 

my_list = ['zero', 'one', 'two'] 
print("2nd element is: {0[2]}".format(my_list))

t = (12, 45, 22222, 103, 6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t)   

number_list = [12,45,78]
print map('the number is {}'.format, number_list)

from datetime import datetime,timedelta   
once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0) 
delta = timedelta(days=13, hours=8,  minutes=20)   
gen = (once_upon_a_time + x * delta for x in xrange(5))  
print '\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))

def fn(l, incr): 
    result = l[0] 
    l[0] += incr 
    return result
lst = [0]
f'{fn(lst,2)} {fn(lst,3)}'
f'{fn(lst,2)} {fn(lst,3)}'
lst
 
from datetime import datetime 
'North America: {dt:%m/%d/%Y}.  ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()) '

data = ["a", "bbbbbbb", "ccc"] 
m = max(map(len, data)) 
for d in data:
    print('{:>{}}'.format(d, m))
    
person = {'first': 'Arthur', 'last': 'Dent'} 
'{p[first]} {p[last]}'.format(p=person)

class Person(object):  
    first = 'Zaphod'    
    last = 'Beeblebrox' 
'{p.first} {p.last}'.format(p=Person())

class Example(object):    
    def __init__(self,a,b,c):        
        self.a, self.b, self.c = a,b,c    
    def __format__(self, format_spec):       
    """ Implement special semantics for the 's' format specifier """        
        if format_spec[-1] != 's':            
            raise ValueError('{} format specifier not understood for this object', format_spec[:-1])
            raw = "(" + ",".join([str(self.a), str(self.b), str(self.c)]) + ")"
        return "{r:{f}}".format( r=raw, f=format_spec )
inst = Example(1,2,3)
print "{0:>20s}".format( inst )

import unicodedata
[unicodedata.name(char) for char in "ê"]
[unicodedata.name(char) for char in "e"]
unicodedata.normalize("NFKD", "ê") == unicodedata.normalize("NFKD", "e")

import unicodedata
def normalize_caseless(text):    return unicodedata.normalize("NFKD", text.casefold())
def caseless_equal(left, right):    return normalize_caseless(left) == normalize_caseless(right)

interstates_lengths = {    5: (1381, 2222),    19: (63, 102),    40: (2555, 4112),    93: (189,305), }
for road, length in interstates_lengths.items():    miles,kms = length
print('{} -> {} mi. ({} km.)'.format(str(road).rjust(4), str(miles).ljust(4), str(kms).ljust(4)))
