def unpacking(a, b, c = 45, d = 60, *args, **kwargs):
    print(a, b, c, d, args, kwargs)
unpacking(1, 2)
unpacking(1, 2, 3, 4)
unpacking(1, 2, c = 3, d = 4)
unpacking(1, 2, d = 4, c = 3)
pair = (3,)
unpacking(1, 2, *pair, d = 4)
unpacking(1, 2, d = 4, *pair)
args_list = [3]
unpacking(1, 2, *args_list, d = 4)
unpacking(1, 2, d = 4, *args_list)
pair = (3, 4)
unpacking(1, 2, *pair)
unpacking(1, 2, 3, 4, *pair)
args_list = [3, 4]
unpacking(1, 2, *args_list)
unpacking(1, 2, 3, 4, *args_list)
arg_dict = {'c' : 3, 'd' : 4}
unpacking(1, 2, **arg_dict)
arg_dict = {'d' : 4, 'c' : 3}
unpacking(1, 2, **arg_dict)
arg_dict = {'c' : 3, 'd' : 4, 'not_a_parameter' : 75}
unpacking(1, 2, **arg_dict)
def to_percent(num):   
    return num * 100
print(list(map(to_percent, [0.95, 0.75, 1.01, 0.1])))

from functools import partial 
from operator import mul
rate = 0.9
dollars = {'under_my_bed': 1000,           'jeans': 45, 'bank': 5000}
print(sum(map(partial(mul, rate), dollars.values())))
def average(*args):   
    return float(sum(args)) / len(args) 
measurement1 = [100, 111, 99, 97] 
measurement2 = [102, 117, 91, 102] 
measurement3 = [104, 102, 95, 101]
print(list(map(average, measurement1, measurement2, measurement3)))
def func(myList):   
    for item in myList:       
        print(item)
func([1, 2, 3, 5, 7])
lst = ['a', 'b', 'c', 'd'] 
func(lst)
def median_of_three(a, b, c):    
    return sorted((a, b, c))[1]
print(list(map(median_of_three, measurement1, measurement2, measurement3, measurement3)))
import operator 
measurement1 = [100, 111, 99, 97] 
measurement2 = [102, 117]
print(list(imap(operator.sub, measurement1, measurement2)))
print(list(imap(operator.sub, measurement2, measurement1)))
print(list(map(operator.sub, measurement1, measurement2)))
print(list(map(operator.sub, measurement2, measurement1)))

insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x : x + ' is an insect' print(list(map(f, insects)))
print(list(map(len, insects)))

carnivores = ['lion', 'tiger', 'leopard', 'arctic fox'] 
herbivores = ['african buffalo', 'moose', 'okapi', 'parakeet'] 
omnivores = ['chicken', 'dove', 'mouse', 'pig']
def animals(w, x, y, z):    
    return '{0}, {1}, {2}, and {3} ARE ALL ANIMALS'.format(w.title(), x, y, z)
import pprint pprint.pprint(list(map(animals, insects, carnivores, herbivores, omnivores)))
"""				"""
class NumberNotInRangeException(Exception):
    pass
def raise_power(x, y): 
    if y in (3, 4, 5): 
        return x ** y 
    raise NumberNotInRangeException("You should provide a valid exponent (3, 4, or 5)")
from functools import partial  
raise_to_three = partial(raise_power, y = 3)
raise_to_four = partial(raise_power, y = 4)
raise_to_five = partial(raise_power, y = 5)
print(raise_to_three(2))  
print(raise_to_four(2))   
print(raise_to_five(2))   

def func(params):    
    for value in params:  
        print('Got value {}'.format(value))   
        if value == 1:  
            print(">>>> Got 1")  
            return  
        print("Still looping")   
    return "Couldn't find 1"  
result = func([5, 3, 1, 2, 8, 9])
print(result)
def function():
    for x in range(10):
        yield x ** 2
print(sum(i for i in range(10) if i % 2 == 0))
foo = [1, 2, 3, 4]
print(any(x == 0 for x in foo))
print(type(a > b for a in foo if a % 2 == 1))
print(sum((i for i in range(10) if i % 2 == 0)))
print(any((x == 0 for x in foo)))
result_type_gen = type((a > b for a in foo if a % 2 == 1))
print("Type of generator expression (parens):", result_type_gen)
from functools import reduce
lem = lambda x : x * x
print(lem(2))
print(map(len, ["Mary", "Isla", "Sam"]))
print(reduce(lambda a, x: a + x, [0, 1, 2, 3, 4]))
arr = [1, 2, 3, 4, 5, 6]
print([i for i in filter(lambda x : x > 4,arr)])
import operator
print(reduce(operator.mul, [10, 5, -3]))
print(reduce(operator.and_, [False, True, True, True]))
print(reduce(operator.or_, [True, False, False, False]))
def raise_power(x, y): 
    if y in (3, 4, 5): 
        return x ** y 
    raise ValueError("You should provide a valid exponent (3, 4, or 5)")
from functools import partial  
raise_to_three = partial(raise_power, y=3)
raise_to_four = partial(raise_power, y=4)
raise_to_five = partial(raise_power, y=5)
print(raise_to_three(2))  
print(raise_to_four(2))   
print(raise_to_five(2))   
try:
    print(raise_power(2, 6))
except ValueError as e:
    print(f"Error: {e}")

def print_args(func):    
    def inner_func(*args, **kwargs):    
        print("Arguments:", args)  
        print("Keyword arguments:", kwargs)  
        return func(*args, **kwargs)
    return inner_func
@print_args
def multiply(num_a, num_b):    
    return num_a * num_b 
print("Result of multiplication:", multiply(3, 5))
def func(params):    
    for value in params:        
        print ('Got value {}'.format(value))        
        if value == 1:            
            print (">>>> Got 1")      
            return        
        print ("Still looping")   
    return "Couldn't find 1" 
print(func([5, 3, 1, 2, 8, 9]))
def function():
    for x in range(10):
        yield x ** 2
print(sum(i for i in range(10) if i % 2 == 0))
foo = [1, 2, 3, 4]
print(any(x == 0 for x in foo))
print(type(a > b for a in foo if a % 2 == 1))
print(sum((i for i in range(10) if i % 2 == 0)))
print(any((x == 0 for x in foo)))
print(type((a > b for a in foo if a % 2 == 1)))
print(sum(i ** 2 for i in range(4)))
import itertools
def starting_from(n):    
    while True:        
        yield n        
        n += 1
natural = starting_from(1)
natural = itertools.count(1)
multiples_of_two = (x * 2 for x in natural) 
multiples_of_three = (x for x in natural if x % 3 == 0)
list(multiples_of_two)
first_five_multiples_of_three = [next(multiples_of_three) for _ in range(5)]
from itertools import islice 
multiples_of_four = (x * 4 for x in starting_from(1)) 
first_five_multiples_of_four = list(islice(multiples_of_four, 5))
next(natural)    
next(multiples_of_two)   
next(multiples_of_four) 
for idx, number in enumerate(multiplies_of_two): 
    print(number)    
    if idx == 9:
        break

import itertools
def fibonacci():    
    a, b = 1, 1   
    while True:        
        yield a        
        a, b = b, a + b
first_ten_fibs = list(itertools.islice(fibonacci(), 10))
def nth_fib(n):    
    return next(itertools.islice(fibonacci(), n - 1, n))
ninety_nineth_fib = nth_fib(99)

def accumulator():    
    total = 0    
    value = None    
    while True:      
        value = yield total      
        if value is None: 
            break       
        total += value
generator = accumulator()
next(generator)    
generator.send(1)    
generator.send(10)   
generator.send(100) 
next(generator)

def foob(x):    
    yield from range(x * 2)    
    yield from range(2)
print(list(foob(5)))
def fibto(n):   
    a, b = 1, 1    
    while True:      
        if a >= n: break        
        yield a        
        a, b = b, a + b
def usefib():  
    yield from fibto(10)  
    yield from fibto(20)
print(list(usefib()))
def xrange(n):   
    i = 0   
    while i < n:       
        yield i       
        i += 1
for i in xrange(10):   
    print(i)
a, b, c = xrange(3)
print(list(xrange(10)))
def nums():    
    yield 1
    yield 2    
    yield 3 
generator = nums()
next(generator, None)  
next(generator, None)  
next(generator, None)  
next(generator, None)  
def coroutine(func):    
    def start(*args,**kwargs):        
        cr = func(*args,**kwargs)        
        next(cr)        
        return cr    
    return start
@coroutine
def adder(sum = 0):   
    while True:       
        x = yield sum   
        sum += x
s = adder() 
s.send(1) 
s.send(2) 
def create_gen():      
    yield value    
    return
print(list(create_gen()))
def preorder_traversal(node):    
    yield node.value    
    for child in node.children:        
        yield from preorder_traversal(child)
generator = (i * 2 for i in range(3))
next(generator)  
next(generator)  
next(generator)  
next(generator)  
def fib(a = 0, b = 1):   
    while True:      
        yield a        
        a, b = b, a + b 
f = fib() 
print(', '.join(str(next(f)) for _ in range(10)))

def find_and_transform(sequence, predicate, func):  
    for element in sequence:        
        if predicate(element):  
            return func(element)
    raise ValueError("No element satisfies the predicate")  
my_sequence = [1, 2, 3, 4, 5]
my_predicate = lambda x: x % 2 == 0
my_func = lambda x: x * x  
item = find_and_transform(my_sequence, my_predicate, my_func)
print("Transformed item:", item)
item = next(my_func(x) for x in my_sequence if my_predicate(x))
print("Transformed item using generator:", item)
def first(generator): 
    try: 
        return next(generator)  
    except StopIteration:
        raise ValueError("Generator is empty")  
gen = (x for x in my_sequence if x % 2 == 0)  
print("First even number:", first(gen))
a = [1, 2, 3]
b = ['a', 'b', 'c']
for x, y in zip(a, b): 
    print(x, y)  

from functools import reduce
import operator
def add(s1, s2):  
    return s1 + s2
asequence = [1, 2, 3, 4, 5]
sum_result = reduce(add, asequence)
print("Sum of elements:", sum_result)
sum_result = reduce(operator.add, asequence)
print("Sum using operator.add:", sum_result)
sum_result_with_initial = reduce(add, asequence, 10)  
print("Sum with initial value 10:", sum_result_with_initial)
def multiply(s1, s2):    
    print(f'{s1} * {s2} = {s1 * s2}')  
    return s1 * s2
asequence = [1, 2, 3]
cumprod_with_initial = reduce(multiply, asequence, 5)
print("Cumulative product with initial value 5:", cumprod_with_initial)
cumprod_without_initial = reduce(multiply, asequence)
print("Cumulative product without initial value:", cumprod_without_initial)

myvar = None  
if myvar is not None: print("Not None")
if myvar is None: print("None")
sentinel = object()
def myfunc(var = sentinel):
    if var is sentinel: print("Yes")  
    else: print("No") 
myfunc()        
myfunc(42)      
myfunc(None)    

def outerFunction(text):
    def innerFunction():
        print(text)
    innerFunction()
if __name__ == '__main__':
    outerFunction('Hey!')
    
def outerFunction(text): 
    def innerFunction(): 
        print(text) 
    return innerFunction  
if __name__ == '__main__': 
    myFunction = outerFunction('Hey!') 
    myFunction() 

import logging 
logging.basicConfig(filename='example.log',
                    level=logging.INFO) 
def logger(func): 
    def log_func(*args): 
        logging.info( 
            'Running "{}" with arguments {}'.format(func.__name__,
                                                    args)) 
        print(func(*args)) 
    return log_func             
 
def add(x, y): 
    return x+y 
def sub(x, y): 
    return x-y 
add_logger = logger(add) 
sub_logger = logger(sub) 
 
add_logger(3, 3) 
add_logger(4, 5) 
sub_logger(10, 5) 
sub_logger(20, 10) 

def add(x, y):
    return x + y
addition = add
print(add, "\n", addition)
print(addition(8, 9))
"""                                    """
def greet():
    print("Hi")
def disp(other):
    print("Displayed")
    other()
disp(greet)
def louder(name):
    print(f"Hi {name.upper()} ")
def softer(name):
    print(f"Hi {name.lower()} ")
def hello(other, name1):
    print("display func")
    other(name1)
hello(louder, "molla")
hello(softer, "MOLLA")
"""                                    """
def hello(name):
    print("Executed")
    def greet():
        print("Aa")
    def welcome():
        print("Bb")
    if name == "molla":
        return greet
    else:
        return welcome
#hello("molla")
x = hello("molla")
x()
"""							"""
def divide(x, y):
    try:
        print(x // y)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
divide(9, 7)
divide(9, 0)
def divide(x, y):
    try:
        print(x // y)
    except Exception as e:
        print("The error is: ", e)
divide(3, "GFG") 
divide(3, 0) 
def AdivB(a, b):
    try:
        c = (a + b) // (a - b)
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AdivB(2, 3)
AdivB(3.0, 3.0)

try: 
    k = 5 // 0
    print(k) 
except ZeroDivisionError:    
    print("Can't divide by zero")
finally:
    print('This is always executed')


a, b = 10, 20
print("Both are Equal" if a == b else "a is greater" if a > b else "b is greater")
print(("b is minimum", "a is minimum")[a < b])
print({True : "a is minimum", False: "b is minimum"}[a < b])
print((lambda: "b is minimum", lambda: "a is minimum")[a < b]())
print(a, "is minimum") if(a < b) else print(b, "is minimum")
maxi = a if a > b else b
Dict = {'max' : a if a > b else b}
res = "Positive" if a > 0 else "negetive"

#isinstance
i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1
print(i)
#control statement
cnt = 1
while cnt <= 10:
    print(cnt)
    cnt += 1
    if cnt == 7:
        #continue
        break
    print("inner loop")
print("outer loop")

cnt = 0
while cnt < 3:
    cnt += 1
    print("Hi")
    
#range
for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)

for i in range(5):
    print("a")
    print("b")
    if i == 2:
        print("Welcome")
        if True:
            print("Hello")
print("Bye")

def display():
    for i in range(1, 11):
        print(i)
display()

#in, not, not in, is, is not
#or, and
boss = True
if boss is True or boss is not False:
    print("True")
else:
    print("False")
coin = 'head'
if boss = False:
    print("False")
    if coin == 'tail':
        print("Batting")
    else:
        print("Bowling")
        
a = 23
if a > 5:
    if a % 2 == 0 and a > 7:
        print("Even")
    else:
        print("Odd")
else:
    print("less than 5")
    
num = 1
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
    if num == 8:
        break

i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end = " ")
    i += 1

#for i  in range(1, 11):
#range[start, end, step]
for i in range(1, 11, 2):
    print(i)

name, cog = ['Aa', 'Bb', 'Cc'], 'Molla'
for i in name:
    print(i)
    if i == 'Bb':  print("Hey")
for x in cog:
    print(x)
    
tes, lst = {2, 3, 5, -2, 10}, [2, 3, 5, -2, 10]
sq, sqr = set(), []
for i in tes:
    square = i ** 2
    sq.add(square)
    print(sq)
for i in lst:
    sq = i**2
    sqr.append(sq)
    print(sqr)
print(f"set: {sq}\nlist: {lst} ")

cnt = 1
while cnt <= 10: print(cnt); cnt += 1
cnt = 5
while cnt >= 5: print(cnt); cnt -= 1
lst = [2, 3, 4, 5]
while lst: print(lst, "Hi"); lst.pop()
"""             """
cnt = 1
#while cnt <= 5:
while True:
    print(cnt)
    cnt += 1
    if cnt == 2:
        break
else:
    print("Outer block")
print("End")
"""             """
cnt = 1
while cnt <= 5:
    print(cnt)
    cnt += 1
else:
    print("Outer block")
print("End")

#sentinal value
num = int(input("Enter val(-1 for exit): "))
while num != -1:
    print(num)
    num = int(input("Enter val(-1 for exit): "))
else:
    print("Outer Block")
print("End")
"""             """
total = 0
num = int(input("Enter val(-1 for exit): "))
while num != -1:
    total += num
    num = int(input("Enter val(-1 for exit): "))
print(total)
"""                """
rang = range(5)
print(f"rang: {rang}\nrang[1]: {rang[1]} ")
rang = range(2, 10, 2)#(start, end, stp)
for i in rang:
    print(i, rang)
for i in range(10, 0, -2):
    print(i, rang)
    
def table(n):
    for i in range(1, 11):
        print(i * n, end = " ")
table(5)
#sum of even
total = 0
#exclude 100 sum even
for i in range(0, 100, 2):
    total += i
print(total)

i = 25
if i == 10: print("i is 10")
elif i == 15: print("i is 15")
elif i == 20: print("i is 20")
else: 
    print("i isn't present")
"""                 """
i = 10
print(True) if i < 15 else print("False")
"""                 """
x = 0
res = { x > 0 : "positive", x < 0 : "negatives "}.get(True, "zero")
print(res)
x = 0
{x > 0 : print("positive"), x < 0 : print("negetive")}.get(True, print("Zero"))
"""                 """
letter = "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B, C")
"""             """
num = 10
if num > 5:
    print("greater than 5")
    if num <= 15:
        print("Between 5 & 15")
"""                 """
i = 0
if i != 0:
    if i > 0:
        print("positive")
    else:
        print("Negetive")
else:
    print("Zero")
"""                    """
def match():
    num = int(input("Enter choice: "))
    match num:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case _:
            print("Not Between 1 & 3")
def match():
    num = int(input("Enter choice: "))
    match num:
        case 1 | 2:
            print("One Or Two")
        case 3 | 4:
            print("Three Or Four")
        case 5 | 6:
            print("Five Or Six")
        case _:
            print("Not Between 1 & 6")
def match():
    num = int(input("Enter choice: "))
    match num:
        case num if num > 0:
            print("Positive")
        case num if num < 0:
            print("Negetive")
        case _:
            print("Zero")
def match():
    ing = "Hellow vai"
    match(ing[6]):
        case "w":
            print("case 1 match")
        case "W":
            print("case 2 match")
        case _:
            print("char not in the string")
def match(val):
    match val:
        case 1:
            return "val is 1"
        case 2:
            return "val is 2"
        case 3:
            return "val is 3"
        case _:
            return "else"
print(match(1))
print(match(2))
def match(ing):
    match ing:
        case ["a"] :
            print("a")
        case ["a", *b]:
            print(f"a and {b} ")
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e ")
        cese _:
            print("No data")
match([])
match(["a"])
match(["a", "b"])
match(["b", "c", "d", "e"])
"""             """
def runMatch(dictionary):
    match dictionary:
        case {"name": n, "age": a} if "salary" not in dictionary:
            print(f"Name: {n}, Age: {a}")
        case {"name": n, "salary": s} if "age" not in dictionary:
            print(f"Name: {n}, Salary: {s}")
        case {"name": n, "age": a, "salary": s}:
            print(f"Name: {n}, Age: {a}, Salary: {s}")
        case {"age": a} | {"salary": s}:
            print("Error: Name is missing in the data.")
        case _:
            print("Data does not match any known patterns.")
runMatch({"name": "Jay", "age": 24})            
runMatch({"name": "Ed", "salary": 25000})  
runMatch({"name": "Al", "age": 27, "salary": 30000})
runMatch({"age": 30})
runMatch({})            
"""             """
from dataclasses import dataclass
@dataclass
class person:
    name : str
    age : int
    salary: int
@dataclass
class programmer:
    name : str
    lang : str
    framework : str
def runMatch(instance):
    match instance:
        case Programmer("Om", language="Python", framework="Django"):
            print(f"Name: Om, Language:Python, Framework:Django")
        case Programmer("Rishabh", "C++"):
            print("Name:Rishabh, Language:C++")
        case Person("Vishal", age=5, salary=100):
            print("Name:Vishal")
        case Programmer(name, language, framework):
            print(f"Name:{name}, Language:{language}, Framework:{framework}")
        case Person():
            print("He is just a person !")
        case _:
            print("This person is nothiing!")
programmer1 = Programmer("Om", "Python", "Django")
programmer2 = Programmer("Rishabh", "C++", None)
programmer3 = Programmer("Sankalp", "Javascript", "React")
person1 = Person("Vishal", 5, 100)
runMatch(programmer1)
runMatch(programmer2)
runMatch(person1)
runMatch(programmer3)

"""            """
a, b, c = 0, 2, 4
if a > b or b < c:
    print("True")
else:
    print("False")
if a or b or c:
    print("\nAtleast one value has boolean true")
if a and b and c:
    print("\nAll number has boolean true")
else:
    print("\nAtleast one has boolean true")

"""                """
a = 0
if not a:
    print("\na is true")
#equivalent
b = 1
if(a == 0):
    print("a == 0: ", a == 0)
if(a == b):
    print("a == b", a == b)
if(a!= b):
    print("a != b", a != b)
"""            """
x, y = 10, 10
if(x is y):
    print("True")
else:
    print("False")
"""				"""
for i in range(5, 20, 2):
    print(i, end = " ")
print()
for i in range(25, 2, -2):
    print(i, end = " ")
print()
val = range(10)[0] #first
val = range(10)[-1] #last element
print(val)
from itertools import chain
res = chain(range(5), range(10, 20, 2))
print(res)
for i in res:
    print(i, end = " ")
print()
fruits = ["A", "B", "C", "D"]
for i in range(len(fruits)):
    print(fruits[i], i, end = " ")
"""					"""
ing = "mollavai"
for letter in ing:
    print(letter, end = ' ')
    if letter == 'a' or letter == 'i':
        break
print()
i = 0
while(True):
    print(ing[i], end = ' ')
    if ing[i] == 'a' or ing[i] == 'i':
        break
    i += 1
"""                """
print()
for i in range(1, 5):
    for j in range(2, 6):
        if j % i == 0:
            break
        print(i, ' ', j)
"""                 """
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end = ' ')
"""                   """
print()
for i in ing:
    if i == 'o':
        print("Executed")
        pass
    print(i, end = " ")
"""					"""
n = 5
print("Hello") if n > 10 else print("Bye") if n > 5 else print("GoodBye")
a = 1 
if a == 3 or 4 or 6:
    print('yes')
else:
    print('no')
if a in (3, 4, 6): 
    print('yes') 
else:
    print('no')
"""					"""
i = 0
while i < 7:
    print(i, end = " ")
    if i == 4:
        break
    i += 1
"""                """
print()
for i in (0, 1, 2, 3, 4, 5):
    print(i, end = " ")
    if i == 2:
        break
"""                 """
print()
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i, end = " ")
"""                 """
print()
def breakLoop():
    for i in range(1, 5):
        if i == 2:
            return i
        print(i)
    return (5)
"""                 """
print()
def breakAll():
    for j in range(1, 5):
        for i in range(1, 4):
            if i * j == 6:
                return (i)
            print(i * j)
"""                    """
print()
for i in [0, 1, 2, 3, 4]:
    print(i, end = ' ')
print()
for i in range(5):    
    print(i, end = ' ')
print()
for i in ['One', 'Two', 'Three', 'Four']:
    print(i, end = ' ')
print()
for i in range(1, 6):
    print(i, end = ' ')
print()
for index, item in enumerate(['one', 'two', 'three', 'four']):   
    print(index, '::', item, end = ' ')
print()
x = map(lambda e : e.upper(),['one', 'two', 'three', 'four']) 
print(x, end = ' ')
"""                    """
print()
for i in range(3):
    print(i,  end = " ")
else:
    print("done")
print()
i = 3
while i < 3:
    print(i, end = ' ')
    i += 1
else:
    print("done")
"""                    """
lst = [1, 2, 3, 4]
for i in lst:
    if type(i) is not int:
        print(i, end = ' ')
        break
    else:
        print("No exeception")
"""                """
print()
"""                """
a = 10
while True:
    a -= 1
    print(a, end = " ")
    if a < 7:
        break
print("Done")
"""						"""
ing = "Geeks"
for i in ing:
    print(i, end = " ")
l1 = ["eat", "sleep", "repeat"]
for count, ele in enumerate(l1):
    print (count, ele)
"""            """
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
lst = ["geeks", "for", "geeks"]
for i in lst:
    print(i, end = " ")
print([x for x in range(11)])

d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))
tup = ((1, 2), (3, 4), (5, 6))
for a, b in tup:
    print(a, b)

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)
for i in range(1, 4):
    print(i)
else:  
    print("No Break\n")
    
clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("socks")
print(f"Washing {paired_socks}")
for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
    
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
for char in 'Python':
    print(char)
for index, num in enumerate([10, 20, 30]):
    print(f'Index {index}: {num}')
    
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(f'{key}: {value}')

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f'Total sum: {total}')

count = 0
while (count < 3): 
    count = count + 1
    print("Hello Geek")
    
age = 28
while age > 19: 
    print('Infinite Loop')
    break

i = 0
a = 'geeksforgeeks'
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1

i = 0
a = 'geeksforgeeks'
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        break
    print('Current Letter :', a[i]) 
    i += 1

a = 'geeksforgeeks'
i = 0
while i < len(a): 
    i += 1
    pass
print('Value of i :', i) 

i = 0
while i < 4: 
    i += 1
    print(i) 
else:  
    print("No Break\n") 
  
i = 0
while i < 4: 
    i += 1
    print(i) 
    break
else: 
    print("No Break") 
    
a = int(input('Enter a number (-1 to quit): ')) 
while a != -1: 
    a = int(input('Enter a number (-1 to quit): '))
    
count = 0
while True: 
    count += 1
    print(f"Count is {count}") 
    if count == 10:
        break
a = [1, 2, 3, 4] 
while a: 
    print(a.pop())

count = 0
while (count < 5): 
    count += 1
    print("Hello Geek") 

initial_height = 10 
bounce_factor = 0.5 
height = initial_height 
while height > 0.1:   
    print("The ball is at a height of", height, "meters.") 
    height *= bounce_factor   
print("The ball has stopped bouncing.")

countdown = 10
while countdown > 0: 
    print(countdown) 
    countdown -= 1
print("Blast off!") 
