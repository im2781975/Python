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

def greet(name):   
    print("Hello, {0}!".format(name))
    print("What's your name?")
    name = input() 
greet(name)

from itertools import chain 
class SolarSystem:   
    planets = [list (chain (planet, (index + 1,))) for index, planet in enumerate ((      
        ('Mercury', 'hot', 2240),        
        ('Venus', 'sulphurous', 6052),       
        ('Earth', 'fertile', 6378),        
        ('Mars', 'reddish', 3397),        
        ('Jupiter', 'stormy', 71492),        
        ('Saturn', 'ringed', 60268),        
        ('Uranus', 'cold', 25559),        
        ('Neptune', 'very cold', 24766)    ))]       
    lines = (        '{} is a {} planet',        'The radius of {} is {} km',        '{} is planet nr. {} counting from the sun'    )       
    def __init__ (self):        
        self.lineIndex = 0
    def greet (self):       
        self.planet = self.planets [int (Math.random () * len (self.planets))]       
        document.getElementById ('greet') .innerHTML = 'Hello {}'.format (self.planet [0])     
        self.explain()
    def explain (self):       
        document.getElementById ('explain').innerHTML = (            self.lines [self.lineIndex] .format (self.planet [0], self.planet [self.lineIndex + 1]) ) 
        self.lineIndex = (self.lineIndex + 1) % 3        
        solarSystem = SolarSystem ()

class A: 
    def __init__ (self, x):
        self.x = x 
    def show (self, label):
        print ('A.show', label, self.x)
class B: 
    def __init__ (self, y):        
        alert ('In B constructor') 
        self.y = y 
    def show (self, label): 
        print ('B.show', label, self.y) 
class C (A, B): 
    def __init__ (self, x, y):       
        alert ('In C constructor')      
        A.__init__ (self, x)       
        B.__init__ (self, y) 
        self.show ('constructor') 
    def show (self, label):        
        B.show (self, label) 
        print ('C.show', label, self.x, self.y)
a = A (1001) 
a.show ('america') 
b = B (2002) 
b.show ('russia') 
c = C (3003, 4004) 
c.show ('netherlands') 
show2 = c.show 
show2 ('copy')

 "£13.55".encode('ascii', errors='replace')
"£13.55".encode('ascii', errors='ignore')
"£13.55".encode('ascii', errors='namereplace')
"£13.55".encode('ascii', errors='xmlcharrefreplace')
"£13.55".encode('ascii', errors='backslashreplace')
b = "£13.55".encode('utf8')
b.decode('ascii', errors='replace')
b.decode('ascii', errors='ignore')
b.decode('ascii', errors='backslashreplace')
type("f") == type(u"f")
type(b"f")
"£13.55".encode('utf8')
"£13.55".encode('utf16')
print type(u"£13.55".encode('utf8'))
print u"£13.55".encode('utf8')
b'\xc2\xa313.55'.decode('utf8')

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
new_list

class Singleton(object):    
    def __new__(cls):          
        if not hasattr(cls, 'instance'):           
            cls.instance = super(Singleton, cls).__new__(cls) 
        return cls.instance
s = Singleton() 
print ("Object created", s) 
s1 = Singleton() 
print ("Object2 created", s1)

from abc import ABCMeta, abstractmethod 
class Music():    
    __metaclass__ = ABCMeta    
    @abstractmethod    
    def do_play(self):        
        pass 
class Mp3(Music):    
    def do_play(self):        
        print ("Playing .mp3 music!")   
class Ogg(Music):   
    def do_play(self):        
        print ("Playing .ogg music!")   
class MusicFactory(object):    
    def play_sound(self, object_type):        
        return eval(object_type)().do_play()  
if __name__ == "__main__":    
    mf = MusicFactory()    
    music = input("Which music you want to play Mp3 or Ogg")   
    mf.play_sound(music)
    
from types import MethodType
class Animal(object):      
    def __init__(self, *args, **kwargs):        
        self.name = kwargs.pop('name', None) or 'Animal'       
        if kwargs.get('walk', None):            
            self.walk = MethodType(kwargs.pop('walk'), self)   
    def walk(self):        
        """        Cause animal instance to walk               Walking functionality is a strategy, and is intended to        be implemented separately by different types of animals.        """        
        message = '{} should implement a walk method'.format(           self.__class__.__name__)        
        raise NotImplementedError(message)
    def snake_walk(self):    
        print('I am slithering side to side because I am a {}.'.format(self.name)) 
    def four_legged_animal_walk(self):    
        print('I am using all four of my legs to walk because I am a(n) {}.'.format(        self.name)) 
    def two_legged_animal_walk(self):    
        print('I am standing up on my two legs to walk because I am a {}.'.format(        self.name))
generic_animal = Animal() 
king_cobra = Animal(name='King Cobra', walk=snake_walk) 
elephant = Animal(name='Elephant', walk=four_legged_animal_walk)
kangaroo = Animal(name='Kangaroo', walk=two_legged_animal_walk)
kangaroo.walk() 
elephant.walk() 
king_cobra.walk()
generic_animal.walk()

from datetime import date 
from operator import attrgetter
class Proxy: 
    def __init__(self, current_user, reservation_service): 
        self.current_user = current_user 
        self.reservation_service = reservation_service
    def highest_total_price_reservations(self, date_from, date_to, reservations_count): 
        if self.current_user.can_see_reservations: 
            return self.reservation_service.highest_total_price_reservations(                date_from,                date_to,                reservations_count ) 
        else: 
            return []
            
class Reservation: 
    def __init__(self, date, total_price): 
        self.date = date 
        self.total_price = total_price
class ReservationService: 
    def highest_total_price_reservations(self, date_from, date_to, reservations_count): 
        reservations = [            Reservation(date(2014, 5, 15), 100),            Reservation(date(2017, 5, 15), 10),            Reservation(date(2017, 1, 15), 50) ]
        filtered_reservations = [r for r in reservations if (date_from <= r.date <= date_to)]        
        sorted_reservations = sorted(filtered_reservations, key=attrgetter('total_price'), reverse=True) 
        return sorted_reservations[0:reservations_count]
class User:
    def __init__(self, can_see_reservations, name): 
        self.can_see_reservations = can_see_reservations 
        self.name = name
class StatsService: 
    def __init__(self, reservation_service): 
        self.reservation_service = reservation_service 
    def year_top_100_reservations_average_total_price(self, year):        
        reservations = self.reservation_service.highest_total_price_reservations(            date(year, 1, 1),            date(year, 12, 31), 1 ) 
        if len(reservations) > 0:            
            total = sum(r.total_price for r in reservations) 
            return total / len(reservations)
            else: 
                return 0
def test(user, year):    
    reservations_service = Proxy(user, ReservationService())    
    stats_service = StatsService(reservations_service)    
    average_price = stats_service.year_top_100_reservations_average_total_price(year) 
    print("{0} will see: {1}".format(user.name, average_price))
    test(User(True, "John the Admin"), 2017) 
    test(User(False, "Guest"),         2017)

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

a = 1 
id(a)
a += 2

stack = "Overflow"
id(stack)
stack += " rocks!"
id(stack)
 
stack = "Stack" 
stackoverflow = stack + "Overflow" 
id(stack)
id(stackoverflow)

s = ""
for i in range(1, 1000):    
    s += str(i)    
    s += ","

b = bytearray(b'Stack')
id(b)
b += b'Overflow'
bytearray(b'StackOverflow') 
id(b)

c = b 
c += b' rocks!' 
bytearray(b'StackOverflow rocks!')
id(c) == id(b)

ll = [ [] ]*4
ll[0].append(23)

def list_add3(lin):    
    lin += [3]    
    return lin
a = [1, 2, 3]
b = list_add3(a)

def tuple_add3(tin):    
    tin += (3,)    
    return tin
a = (1, 2, 3) 
b = tuple_add3(a) 

def yoda(prologue, sentence):    
    sentence.reverse()    
    prologue += " ".join(sentence)    
    return prologue
focused = ["You must", "stay focused"] 
saying = "Yoda said: " 
yoda_sentence = yoda(saying, focused)

orders_df = pd.DataFrame() 
orders_df['customer_id'] = [1,1,1,1,1,2,2,3,3,3,3,3] 
orders_df['order_id'] = [1,1,1,2,2,3,3,4,5,6,6,6] 
orders_df['item'] = ['apples', 'chocolate', 'chocolate', 'coffee', 'coffee', 'apples', 'bananas', 'coffee', 'milkshake', 'chocolate', 'strawberry', 'strawberry']
print(orders_df)

count_number_of_orders = lambda x: len(x.unique())
orders_df['number_of_orders_per_cient'] = (orders_df .groupby(['customer_id'])['order_id']  .transform(count_number_of_orders))
print(orders_df)

def multiple_items_per_order(_items): 
    multiple_item_bool = _items.duplicated(keep=False) 
    return(multiple_item_bool)
    
orders_df['item_duplicated_per_order'] = (orders_df .groupby(['order_id'])['item'] .transform(multiple_items_per_order))
print(orders_df)

from ply import lex import ply.yacc as yacc
tokens = (    'PLUS',    'MINUS',    'TIMES',    'DIV',    'LPAREN',    'RPAREN',    'NUMBER', )

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

precedence = ( ( 'left', 'PLUS', 'MINUS' ), ( 'left', 'TIMES', 'DIV' ), ( 'nonassoc', 'UMINUS' ) )
def p_add( p ) : 
    'expr : expr PLUS expr'   
    p[0] = p[1] + p[3]
def p_sub( p ) :
    'expr : expr MINUS expr'   
    p[0] = p[1] - p[3]
def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'  
    p[0] = - p[2]
def p_mult_div( p ) : '''expr : expr TIMES expr            | expr DIV expr''' 
    if p[2] == '*' :        
        p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0") 
            raise ZeroDivisionError('integer division by 0')       
        p[0] = p[1] / p[3]
def p_expr2NUM( p ) : 
    'expr : NUMBER'   
    p[0] = p[1]
def p_parens( p ) : 
    'expr : LPAREN expr RPAREN' 
    p[0] = p[2]
def p_error( p ): 
    print("Syntax error in input!")
parser = yacc.yacc()
res = parser.parse("-4*-(3-5)")
print(res)

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
        
import unittest
class SomeTest(unittest.TestCase): 
    def setUp(self): 
        super(SomeTest, self).setUp() 
        self.mock_data = [1,2,3,4,5]
    def test(self): 
        self.assertEqual(len(self.mock_data), 5) 
    def tearDown(self):
        super(SomeTest, self).tearDown() 
        self.mock_data = [] 
if __name__ == '__main__': unittest.main()

import unittest import some_module
class SomeOtherTest(unittest.TestCase):
    def setUp(self): 
        super(SomeOtherTest, self).setUp()
        my_patch = mock.patch.object(some_module, 'method')        
        my_patch.start()
    self.addCleanup(my_patch.stop)
def division_function(dividend, divisor):   
    return dividend / divisor
class MyTestCase(unittest.TestCase):  
    def test_using_context_manager(self):        
        with self.assertRaises(ZeroDivisionError):            
            x = division_function(1, 0)
class MyTestCase(unittest.TestCase):    
    def test_using_context_manager(self):        
        with self.assertRaises(ZeroDivisionError) as ex:           
            x = division_function(1, 0)        
        self.assertEqual(ex.message, 'integer division or modulo by zero')
        
class WrongInputException(Exception):    
    pass
def convert2number(random_input):    
    try:       
        my_input = int(random_input)    
    except ValueError:        
        raise WrongInputException("Expected an integer!")   
    return my_input

import unittest
class ExceptionTestCase(unittest.TestCase):    
    def test_wrong_input_string(self):        
        self.assertRaises(WrongInputException, convert2number, "not a number")    
    def test_correct_input(self):        
        try:            
            result = convert2number("56")            
            self.assertIsInstance(result, int)        
        except WrongInputException:            
            self.fail()
            
import unittest 
class SimplisticTest(unittest.TestCase):    
    def test_basic(self):        
        self.assertTrue(1 + 1 == 2)
        self.assertTrue(1 + 1 == 3)
        
class Deque:
    def __init__(self): 
        self.items = []
    def isEmpty(self):
        return self.items == [] 
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item): 
        self.items.insert(0,item) 
    def removeFront(self): 
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0) 
    def size(self): 
        return len(self.items)
def list_check(to_check, the_list):
    for item in the_list: 
        if to_check == item: 
            return True 
    return False
    
def intensive_f(value):
    if process_has_failed: 
        return None
    return integer_output
x = 5
if intensive_f(x) is not None: 
    print(intensive_f(x) / 2) 
else: 
    print(x, "could not be processed")
print(x)

x = 5
result = intensive_f(x) 
if result is not None:   
    print(result / 2) 
else:    
    print(x, "could not be processed")
    
x = 5
try:    
    print(intensive_f(x) / 2)
except TypeError: 
    print(x, "could not be processed")
    
bird_speeds = get_very_long_dictionary() 
if "european swallow" in bird_speeds:    
    speed = bird_speeds["european swallow"] 
else:    
    speed = input("What is the air-speed velocity of an unladen swallow?") 
print(speed)

bird_speeds = get_very_long_dictionary() 
try:    
    speed = bird_speeds["european swallow"] 
except KeyError:   
    speed = input("What is the air-speed velocity of an unladen swallow?") 
print(speed)
