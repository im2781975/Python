foo = 1 bar = 'bar' baz = 3.14
print('{}, {} and {}'.format(foo, bar, baz))
print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz))
print('{0}, {1}, {2}, and {3}'.format(foo, bar, baz))
print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))

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

'{:~<9s}, World'.format('Hello')
'{:~>9s}, World'.format('Hello')
'{:~^9s}'.format('Hello')
'{:0=6d}'.format(-123)

foo = 'bar'
f'Foo is {foo}'
f'{foo:^7s}'

price = 478.23 
f"{f'${price:0.2f}':*>20s}" '

def fn(l, incr): 
    result = l[0] 
    l[0] += incr 
    return result
lst = [0]
f'{fn(lst,2)} {fn(lst,3)}'
f'{fn(lst,2)} {fn(lst,3)}'
lst

'{0:.0f}'.format(42.12345)
'{0:.1f}'.format(42.12345)
'{0:.3f}'.format(42.12345)
'{0:.5f}'.format(42.12345)
'{0:.7f}'.format(42.12345)
'{:.3f}'.format(42.12345)
'{answer:.3f}'.format(answer=42.12345)
'{0:.3e}'.format(42.12345)
'{0:.0%}'.format(42.12345)

s = 'Hello'
a, b, c = 1.12345, 2.34567, 34.5678 
digits = 2
'{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(s, a, b, c, n=digits)

'{first} {last}'.format_map(data) 'Hodor Hodor!'
'{first} {last}'.format(first='Hodor', last='Hodor!')

from datetime import datetime 
'North America: {dt:%m/%d/%Y}.  ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()) '

'{:c}'.format(65)
'{:d}'.format(0x0a)
'{:n}'.format(0x0a)
'{0:x}'.format(10)
'{0:X}'.format(10)
'{:o}'.format(10)
'{:b}'.format(10)
'{0:#b}, {0:#o}, {0:#x}'.format(42)
'8 bit: {0:08b}; Three bytes: {0:06x}'.format(42)
r, g, b = (1.0, 0.4, 0.0) 
'#{:02X}{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)) 
 '{:.>10}'.format('foo')
'{:.>{}}'.format('foo', 10)
'{:{}{}{}}'.format('foo', '*', '^', 15)

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

print (s.format(a="1"*1, c="3"*3, e="5"*5))

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

str. casefold
str. upper 
str. lower 
str. capitalize
str. title
str. swapcase
"XßΣ".casefold()
"This is a 'string'.".upper()
"This IS a 'string'.".lower()
"this Is A 'String'.".capitalize()
"this Is a 'String'".title()
"this iS A STRiNG".swapcase()
str.upper("This is a 'string'")
map(str.upper,["These","are","some","'strings'"])

translation_table = str.maketrans("aeiou", "12345") 
my_string = "This is a string!" 
translated = my_string.translate(translation_table)

'this syntax is very useful'.translate(None, 'aeiou')

i = 10 f = 1.5 s = "foo" l = ['a', 1, 2] d = {'a': 1, 2: 'foo'}
"{} {} {} {} {}".format(i, f, s, l, d)
str.format("{} {} {} {} {}", i, f, s, l, d)
"{0} {1} {2} {3} {4}".format(i, f, s, l, d)
"{0:d} {1:0.1f} {2} {3!r} {4!r}".format(i, f, s, l, d)
"{i:d} {f:0.1f} {s} {l!r} {d!r}".format(i=i, f=f, s=s, l=l, d=d)
 f"{i} {f} {s} {l} {d}"
f"{i:d} {f:0.1f} {s} {l!r} {d!r}"
"%(i)d %(f)0.1f %(s)s %(l)r %(d)r" % dict(i=i, f=f, s=s, l=l, d=d)

"I am from {}. I love cupcakes from {}!".format("Australia", "Australia")
"I am from {0}. I love cupcakes from {0}!".format("Australia")

"{'a': 5, 'b': 6}"
"{{'{}': {}, '{}': {}}}".format("a", 5, "b", 6)
f"{{'{'a'}': {5}, '{'b'}': {6}}"

import string
string.ascii_letters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits '0123456789'
string.hexdigits '0123456789abcdefABCDEF'
string.octaldigits '01234567'
string.punctuation '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace ' \t\n\r\x0b\x0c'
string.printable '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

