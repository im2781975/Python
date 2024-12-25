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

 "    a line with leading and trailing space     ".strip() 'a line with leading and trailing space'
 
">>> a Python prompt".strip('> ') 

"     spacious string      ".rstrip() '     spacious string'

"     spacious string      ".rstrip() 'spacious string      '

reversed('hello')
[char for char in reversed('hello')]
 
''.join(reversed('hello'))
def reversed_string(main_string):    
    return main_string[::-1]
reversed_string('hello')

"This is a sentence.".split()
" This is    a sentence.  ".split()
"            ".split()

"This is a sentence.".split(' ')
"Earth,Stars,Sun,Moon".split(',')
" This is    a sentence.  ".split(' ')
"This is a sentence.".split('e')
"This is a sentence.".split('en')
"This is a sentence.".split('e', maxsplit=0)
"This is a sentence.".split('e', maxsplit=1)
"This is a sentence.".split('e', maxsplit=2) 
 "This is a sentence.".split('e', maxsplit=-1)
"This is a sentence.".rsplit('e', maxsplit=1)
 "This is a sentence.".rsplit('e', maxsplit=2)
"Make sure to foo your sentence.".replace('foo', 'spam')
"It can foo multiple examples of foo if you want.".replace('foo', 'spam')
"""It can foo multiple examples of foo if you want, \ ... or you can limit the foo with the third argument.""".replace('foo', 'spam', 1)
"Hello World".isalpha()
"Hello2World".isalpha()
"HelloWorld!".isalpha()
"HelloWorld".isalpha()
"HeLLO WORLD".isupper()
"HELLO WORLD".isupper()
"".isupper()
"Hello world".islower()
"hello world".islower()
"".islower()
"hello world".istitle()
"Hello world".istitle()
"Hello World".istitle()
"".istitle()
"Hello2World".isalnum()
"HelloWorld".isalnum()
"2016".isalnum()
 "Hello World".isalnum()
 "\t\r\n".isspace()
" ".isspace()
"".isspace()

my_str = ''
my_str.isspace()
my_str.isspace() or not my_str
not my_str.strip()

"foo" in "foo.baz.bar"
 "" in "test"
 
" ".join(["once","upon","a","time"])
"---".join(["once", "upon", "a", "time"])

s = "She sells seashells by the seashore."
s.count("sh")
s.count("se")
s.count("sea")
s.count("seashells")
s.count("sea", start)

t = s[start:]
t.count("sea")

"ß".lower()
"ß".upper().lower()
"ß".upper().lower()

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


s = "This is a test string"
s.startswith("T")
s.startswith("Thi")
s.startswith("thi")  
s.startswith("is", 2)
s.startswith(('This', 'That'))
s.startswith(('ab', 'bc'))
s.endswith('.')
s.endswith('!')
s.endswith('stop.')
s.endswith('Stop.')
s.endswith(('.', 'something'))
s.endswith(('ab', 'bc'))
 
s = b'\xc2\xa9 abc'
s[0]  
type(s)    
u = s.decode('utf-8') 
u[0] 
type(u)
u.encode('utf-8') 

import re
pattern = r"123" string = "123zzb"
re.match(pattern, string)
match = re.match(pattern, string)
match.group()

string = "\\t123zzb"
pattern = "\\t123"
re.match(pattern, string).group() 
re.match(pattern, "\t123zzb").group()

pattern = r"\\t123" 
re.match(pattern, string).group()

match = re.match(r"(123)", "a123zzb")
match is None
match = re.search(r"(123)", "a123zzb")
match.group()

pattern = r"(your base)"
sentence = "All your base are belong to us."
match = re.search(pattern, sentence)
match.group(1)
match = re.search(r"(belong.*)", sentence)
match.group(1)

match = re.search(r"^123", "123zzb")
match.group(0)
match = re.search(r"^123", "a123zzb")
match is None
match = re.search(r"123$", "zzb123")
match.group(0)

m = re.search("b", "ABC") 
m is None
m = re.search("b", "ABC", flags=re.IGNORECASE)
m.group()
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE)
m is None
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
m.group()

re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44")
re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25")
re.sub(r"t([0-9])([0-9])", r"t\g<2>\g<1>", "t13 t19 t81 t25")

items = ["zero", "one", "two"]
re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1], something, a[2]")

re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899")
results = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")
print(results)
for result in results:     
    print(result.group(0))
    
import re 
def is_allowed(string):    
    characherRegex = re.compile(r'[^a-zA-Z0-9.]')    
    string = characherRegex.search(string)  
    return not bool(string)
print (is_allowed("abyzABYZ0099"))
print (is_allowed("#*@#$%^"))

import re 
data = re.split(r'\s+', 'James 94 Samantha 417 Scarlett 74') 
print( data )

sentence = "This is a phone number 672-123-456-9910" 
pattern = r".*(phone).*?([\d-]+)"
match = re.match(pattern, sentence)
match.groups() 
m.group() 
m.group(0)
m.group(1)
m.group(2)
m.group(1, 2) 

match = re.search(r'My name is (?P<name>[A-Za-z ]+)', 'My name is John Smith')
match.group('name')
match.group(1)

re.match(r'(\d+)(\+(\d+))?', '11+22').groups()
re.match(r'(\d+)(?:\+(\d+))?', '11+22').groups()
match = re.search(r'[b]', 'a[b]c') 
match.group()

match = re.search(r'\[b\]', 'a[b]c') 
match.group()

re.escape('a[b]c')
match = re.search(re.escape('a[b]c'), 'a[b]c') 
match.group()

username = 'A.C.'
re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!')
re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!')

import re
text = 'You can try to find an ant in this string' 
pattern = 'an?\w' 
for match in re.finditer(pattern, text):
    sStart = match.start()
    sEnd = match.end()
    sGroup = match.group()
    print('Match "{}" found at: [{},{}]'.format(sGroup, sStart,sEnd))
