def info(name, surname):
    formattedName = name.title()
    formattedSurname = surname.title()
    print(f"{formattedName} {formattedSurname} ")
    print(f"{name} {surname} ")
info("Molla", "ibrahim")
"""                 """
def greet(name):
    print("Hello {0}!".format(name))
    print("Whats your name")
    name = input()
greet('molla')

from statistics import *
def meanMedianMode(lst):
    #return mean(lst), median(lst), mode(lst)
    return [mean(lst), median(lst), mode(lst)]
print(meanMedianMode([2, 4, 1, 7, 5, 9]))
a, b, c = meanMedianMode([2, 4, 1, 7, 5, 9])
print(f"mean: {a}\nMedian: {b}\nMode: {c} ")
"""             """
def add(a, b):
    return a + b
def func2(x):
    return x + 1
x = add(9, 11)
print(func2(x))
"""                """
def double_it(num):
    num *= 2;
    return num
print(double_it(78))
#lambda func
double = lambda x : x * 2
square = lambda x : x * x
add = lambda x, y: x + y
sub = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y
divInt = lambda x, y: x // y
mod = lambda x, y: x % y
print(f'double is: {double(78)}\nSquare is: {square(89)}\naddition is: {add(34, 78)}\n')
print(f'deduction is :{sub(34, 78)}\nMult is: {mult(34, 78)}\nDivision is: {div(78, 34)}\nDivInt is: {divInt(78, 34)}\nRemainder is: {mod(78, 34)}\n')

def sum(a, b, c = 0):
    res = a + b + c
    return res
print(f'Sum is: {sum(78, 97)}')
print(f'Sum is: {sum(78, 23, 97)}')
print(f"Double of sum is: {sum(78, 97)}\n")

def sum(*num):
    total = 0
    for n in num:
        total += n
        print(total)
    return num
print(sum(23, 45, 89))

def sum(x, y, *args):
    print(args)
    total = 0
    for num in args:
        print(num)
        total += num
    return total
print(sum(2, 3, 6, 8))

def operation(a, b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b
    divInt = a // b
    return [add, sub, mult, div, divInt]
    #return add, sub, mult, div, divInt
print(operation(7, 9))

#from build-in import *(all)
#from [file name] import [function] as [our choice name]
from func import double_it as dt
print(dt(5))
highest = max([1, 2, 3, 4, 5])
lowest = min(1, 2, 3, 4, 5, 6)
count = len([1, 5])
final = sum([1, 2, 3, 4, 5])
print(highest, lowest, count, final)

#list is changeable but tuple no
def Muteable(lst):
    lst.append(3)
x = [2, 5]
Muteable(x), print(x)

def Immuteable(lst):
    lst.append(3)
x = (2, 5)
Immuteable(x), print(x)

def address(first, last):
    name = f"name is: {first} {last}"
    return name
#name = address('Molla', 'ibrahim')
name = address(first = 'Molla', last = 'ibrahim')
print(name)
"""                         """
def printKwargs(**kwargs):
    print(kwargs)
def printKwargs(**kwargs):
    for key in kwargs:
        print("key = {0}, value = {1}".format(key, kwargs[key]))
printKwargs(a = "two", b = 1)
"""                """
def kwargs(x, **key):
    print(key)
kwargs(2, b = 3, c = 4)
"""                """
def arges(x, *args):
    print("Formal arg: %s" %x)
    for arg in args:
        print("Another positional arg is: %s" %arg)
arges(1, "two", 3)
"""                """
def fooBar(foo = None, Bar = None):
    return "{}{}".format(foo, Bar)
values = {"foo" : "foo", "Bar" : "barista"}
print(fooBar(**values))
"""                """
def printArgs(arg, *args, key, keyword):
    print("First positional arg is: {}".format(arg))
    for i in args:
        print("Another position args is: {}".format(i))
    print("key value: {}".format(key))
    print("keyword value: {}".format(keyword))
printArgs(2, 8, 9, 1, key = 8, keyword = 9)
"""                """
def func(arg1, arg2, arg3):
    print("arg1: %s" %arg1)
    print("arg2: %s" %arg2)
    print("arg3: %s" %arg3)
kwargs = {"arg3" : 3, "arg2" : "two"}
func(1, **kwargs)
"""                """
def func(**kwargs):
    print(kwargs.get('value', 0))
func()
func(value = 1)
"""                """
def printArg(arg1, arg2):
    print(str(arg1) + str(arg2))
a = (1, 2)
b = tuple([3, 4])
printArg(a[0], b[1])
printArg(a, b)
"""                """
a , b = [1, 3, 5, 7],[2, 4, 6, 8]
zipped = zip(a, b)
print(zipped)
"""							"""
def intro(*title, first, last):
    name = f"name is: {title} {first} {last} "
    return name
name = intro(first = 'ibrahim', last = 'molla')
#name = intro('Dj',first = 'ibrahim', last = 'molla',)
print(name)
"""                         """
def intro(first, last, **add):
    name = f"{first} {last} {add}"
    #print(add)
    #print(add['title'])
    return name
name = intro(first = "hasan" ,  last = "mahmud", title = "Dj", add = "artist")
print(name)
"""                     """
def greet(name, age):
    print(f"name: {name}, age: {age} ")
#keyword arg should be after positional arg
greet("molla", 29)
greet(name = "Hasan", age = 34)
"""             """
def defaultArg(first, last, dpt = "CS"):
    print(f"name: {first} {last}\ndept: {dpt}")
#default arg should be provided after non def arg
defaultArg("Molla", "vai", "ME")
defaultArg("Hasan", "vai")
"""               """
def arbitryArg(*num):
    sum = 0
    for i in num:
        print(f"Elements are: {i}")
        sum += i
    print(f"sum is: {sum} ")
arbitryArg(4, 6, 8)
"""         """
def arbitryArg(*num, name):
    sum = 0
    print(name)
    for i in num:
        print(f"Elements are: {i}")
        sum += i
    print(f"sum is: {sum} ")
arbitryArg(4, 6, 8, name = "mollavai")
def arbitry_Arg(name, *num):
    sum = 0
    print(name)
    for i in num:
        print(f"Elements are: {i}")
        sum += i
    print(f"sum is: {sum} ")
arbitry_Arg(4, 6, 8)
"""                 """
def posArgs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
posArgs(name = "Ab", dept = "Cs", age = "25")

"""                     """
#keyword arg should be after positional arg
def mixArgs(*args, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(args)
#mixArgs(a = 2, b = 4, c = 8,name = "hasan", dept = "mahmud", age = "24")
mixArgs(2, 4, 6, name = "hasan", dept = "mahmud", age = "24")
def func(arg1, arg2, arg3):
    print(arg1, arg2, arg3)
args = ("Here", "I", "am")
func(*args)
kwargs = {"arg1" : "Here", "arg2" : "I", "arg3" : "am"}
func(**kwargs)
"""                    """
def func(*args):
    for arg in args:
        print(arg, end = " ")
func('Here', 'i', 'am')
"""                    """
def func(tmp, *args):
    print("\nFirst element is: ", tmp)
    for arg in args:
        print(arg, end = " ")
func('Here', 'i', 'am')
"""                    """
print()
def func(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" %(key, value))
func(first = 'Geeks', mid = 'for', last = 'Geeks')
"""                   """
def func(args, **kwargs):
    for key, value in kwargs.items():
        print("%s = %s"%(key, value))
func("Hi", first = 'Geeks', mid = 'for', last = 'Geeks')
def func(*arg, **kwarg):
    print(arg, kwarg)
args = {"Here i am"}
kwargs = {"first" : "where", "mid" : "are", "last" : "You"}
func(args, kwargs)
"""                """
def func(*arg, **kwarg):
    print(arg)
    print(kwarg)
args = {1, 2, 3}
kwargs = {"name" : "hasan", "mid" : "Alom", "last" : "mahmud"}
func(args, kwargs)
"""                """
def example(*args):
    total = sum(args)
    print(total)
example(2, 6, 9)

#scope
def counter():
    num = 0
    def incr():
        nonlocal num
        num += 1
        return num
    return incr
x = counter()
for i in range(1, 12):
    print(x(), end = " ")
print()
def read():
    if True:
        x = "Hi"
    print(x)
read()
"""            """
x = 'Hello'
def changeLocal():
    #global x
    x = 'Bye'
    print(x)
changeLocal()
print(x)
del(x)
"""            """
dic, lst = {'a' : 1, 'b' : 2}, [1, 2, 3, 4, 5]
del dic['a']
del lst[1 : 3]
print(dic, lst)
"""            """
foo = 1 
def func():
    foo = 7  
    print(foo)  
    print(globals()['foo']) 
func()
"""            """
foo = 1
def func():    
    global foo   
    foo = 2  
func()
print(foo)
"""            """
foo = 1
def fun():
    bar = 2
    foo = 2
    print(foo, globals().keys())
    print(bar, locals().keys())
    print(globals()['foo'])
    print(locals()['foo'])
fun()
"""            """
foo = 1
def f1():    
    bar = 1    
    def f2():        
        baz = 2     
        print(locals().keys())
        print('bar' in locals())
        print('bar' in globals()) 
    def f3():        
        baz = 3        
        print(bar)     
        print(locals().keys())      
        print('bar' in locals()) 
        print('bar' in globals()) 
    def f4():        
        bar = 4   
        baz = 4        
        print(bar)       
        print(locals().keys())      
        print('bar' in locals()) 
        print('bar' in globals())
    return f2, f3, f4
f2, f3, f4 = f1()
f2()
"""            """
foo = 0
def f1():    
    foo = 1
    def f2():       
        foo = 2       
        def f3():          
            foo = 3
            print(foo)          
            foo = 30          
        def f4():           
            global foo      
            print(foo) 
            foo = 100
"""            """
def f1():       
    def f2():        
        foo = 2 
        def f3():            
            nonlocal foo
            print(foo)  
            foo = 20 
"""				"""
a = 15
def display():
    a = 10
    def show():
        print(a)
    show()
display()
print(a)
"""             """
a, b = 6, 9
def disp():
    if a < b:
        c = a + b
    print(c)
disp()
"""             """
a = 52
def disp():
    #without global keyword we can access the variable not modify
    global a
    a += 1
    print(a)
disp()
"""             """
def disp():
    a = 20
    def show():
        nonlocal a
        a += 5
        print(a)
    print(a)
    show()
disp()
print(a) #access global variable
"""                """
a, b = 15, 10
def add():
    c = a + b
    print(c)
add()
def func():
    var = 10
    def unc():
        nonlocal var
        var += 10
        print(var)
    unc()
func()
#yield
def fun():
    total = 0
    for i in range(10):
        total += i
        yield total
for i in fun():
    print(i, end = " ")

def cube(x):
    r = x ** 3
    return r
def add(a, b):
    return a + b
def IsTrue(a):
    return bool(a)
print("Addition is: {}".format(add(8, 3)))
print("Boolean is: {}".format(IsTrue(2 < 8)))
"""            """
def func():
    ing = "Here i am"
    x = 10
    return ing, x
print(func())
def func():
    ing = "where are you"
    x = 22
    return [ing, x]
print(func())
def func():
    dic = dict()
    dic['str'] = "mollavai"
    dic['x'] = 20
    return dic
print(func())
"""                """
def adder(x):
    def add(y):
        return x + y
    return adder
print(adder(23))
"""                """
def outer(x):
    return x * 10
def func():
    return outer
res = func()
print(res(5))

def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False
"""                """
a = order
b = order
c = order
if a(-1) or b(5) or c(10):
    print("Atleast one of the number is positive")
def addition(x):
    return x + x
num = (1, 2, 3, 4)
res = map(addition, num)
res = map(lambda x : x + x, num)
square = list(map(lambda x : x ** 2, num))
print(list(res))
"""                    """
num, ber = [1, 2, 3], [4, 5, 6]
res = map(lambda x, y : x + y, num, ber)
print(list(res))
 
lst = ['sat', 'sun', 'mon', 'fri']
print(list(map(list, lst)))

def even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
def double(num):
    return 2 * num
num = [1, 2, 3, 4, 5]
print(list(map(even, num)))
print(list(map(double, num)))
"""					"""
def gen():    
    yield 1 
iterable = gen() 
for a in iterable:   
    print (a)
"""				"""
def yoda(prolouge, sentence):
    sentence.reverse()
    prolouge += "".join(sentence)
    return prolouge
focused = ["You must", "stay focused"] 
saying = "Yoda said: " 
print(yoda(saying, focused))
"""            """
def lstcheck(check, lst):
    for item in lst:
        if check == item:
            return True
    return False
"""            """
processFailed = False
output = 42
def Intensive(val):
    if processFailed:
        return None
    return outout
x = 5
if Intensive(x) is not None: 
    print(Intensive(x) / 2)
else: 
    print(x, "could not be processed")
print(x)
"""            """
def get_very_long_dictionary():
    return {"african swallow": 11.0, "european swallow": 10.0}  
bird_speeds = get_very_long_dictionary() 
if "european swallow" in bird_speeds:    
    speed = bird_speeds["european swallow"]
else:    
    speed = input("What is the air-speed velocity of an unladen swallow?") 
print(speed)
"""				"""
def foo(name) :    
    print(str(name).lower())
def bar(listing) :    
    lst = list(listing)   
    lst.extend((1, 2, 3))    
    return ", ".join(l)
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
def fact(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product
"""            """
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
def fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib(n - 1)
        return (a + b, a)
"""            """
n = 0
for i in range(1, n + 1):
    n += i
    
def recur():
    if n == 1:
        return n + recur(n - 1)
"""            """
def cursing(depth): 
    try:    
        cursing(depth + 1) # actually, re-cursing  
    except RuntimeError as RE:   
        print('I recursed {} times!'.format(depth)) 
cursing(0)
def countDown(n):
    if n == 0:
        print("BlastOff")
    else:
        print(n, end = " ")
        countDown(n - 1)
def findMax(seq, maxi):
    if not seq:
        return maxi
    if maxi < seq[0]:
        return findMax(seq[1:], seq[0])
    else:
        return findMax(seq[1:], maxi)
"""            """
def tail_call_optimized(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@tail_call_optimized
def factorial(n, acc = 1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)
print(factorial(10))  
@tail_call_optimized
def fib(i, current = 0, next = 1):  
    if i == 0:    
        return current 
    else:    
        return fib(i - 1, next, current + next)
print(fib(10))  
"""				"""
def input_num(msg, errormsg=None):
    while True:        
        try:            
            return float(input(msg))       
        except ValueError:      
            if errormsg is not None: 
                print(errormsg)
            else:
                print("Invalid Input")
#num = input_num("Enter: "); print(num)
try:   
    x = 1.0 / 0.0    
    print(x) 
except ZeroDivisionError:   
    print("Division by zero")
print("Hello ", end = "<br>")
print("Hello", end = "Break")
def twoSum(a, b):
    return a + b
def twoSum(a : int, b : int) ->int:
    return a + b
def twoSum(a : str, b : str):
    return a + b
print(twoSum("a", "b"))
def func1(arg1, arg2, arg3):
    return (arg1, arg2, arg3)
print(func1(1, 2, 3), func1(*[6, 7], 9))
dic = {'arg1': 1, 'arg2': 2,'arg3': 3 }
print(func1(**dic))
def func2(arg1 = 'a', arg2 = 'b', arg3 = 'c'):
    return (arg1, arg2, arg3)
print(func2(1), func2(2, 3), func2(arg2 = 2, arg3 = 3))
dic = {'arg1': 1, 'arg2': 2, 'arg3': 3 } 
print(func2(**dic), func2(**{'arg2': 2}))
def func3(arg1, arg2='b', arg3='c'):
    return (arg1, arg2, arg3)
print(func3(*[1]))  
print(func3(*[1, 2, 3]))  
print(func3(**{'arg1' : 1}))  
print(func3(**{'arg1' : 1, 'arg2' : 2, 'arg3' : 3}))  
print(func3(*[1, 2], **{'arg3' : 3}))  
def func(*args, **kwargs):    
    print(args, kwargs)
print(func(1, 2, 3), func(a = 1, b = 2, c = 3), func(1, 2, 3), func('x', 'y', 'z', a = 1, b = 2, c = 3))


#Find Divisors
div = int(input("Enter integers: "))
for x in range(1, div + 1):
    if div / x == div // x:  
        print(x, end = " ")
print()
for i in range(4):   
    d = i * 2
    print(f"d at iteration {i}: {d}")
print("Final value of d:", d) 
"""            """
def switch(value):   
    if value == 1:
        return "one"   
    if value == 2:       
        return "two"    
    if value == 42:       
        return "Error"    
    raise Exception("No case found!")
switch(1)
switch = {1: lambda: 'one', 2: lambda: 'two', 42: lambda: 'Error',}
def default_case():    
    raise Exception('No case found!')
switch.get(1, default_case)()

def run_switch(value):    
    return switch.get(value, default_case)()
run_switch(1)
def greet_two(greeting):
    print(greeting)
greet_two("Howdy")
def greet_two(greeting = "Howdy"):    
    print(greeting)
greet_two()
def many_types(x):    
    if x < 0:        
        return "Hello!"    
    else:        
        return 0 
print(many_types(1)) 
print(many_types(-1))
def func(*args):
    for i in args:        
        print(i) 
func(1, 2, 3)
func(*[1, 2, 3])
def func(**kwargs):   
    for name, value in kwargs.items():  
        print(name, value)
func(x = 1, y = 2, z = 3)
dic = {'foo': 1, 'bar': 2}
func(**dic)       
def fn(**kwargs):   
    print(kwargs)   
    f1(**kwargs)
def f1(**kwargs):   
    print(len(kwargs))
fn(a = 1, b = 2)

def greeting():    
    return "Hello"
print(greeting())
greet_me = lambda: "Hello"
print(greet_me())
strip_and_upper_case = lambda s: s.strip().upper()
print(strip_and_upper_case(" Hello "))
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world = 'world')
def foo(msg):    
    print(msg) 
greet = lambda x = "hello world": foo(x) 
greet()
def make(action = 'nothing'):
    return action
print(make("fun"))
print(make(action = "sleep"))
print(make())

def give_me_five():   
    return 5
print(give_me_five()) 
print(give_me_five() + 10)
def give_me_another_five():    
    return 5    
    print('This statement will not be printed. Ever.')
print(give_me_another_five())
def give_me_two_fives():   
    return 5, 5  
first, second = give_me_two_fives()
print(first, second) 
def makeInc(x):  
    def inc(y):
        return y + x  
    return inc
incOne = makeInc(1)
incFive = makeInc(5)
print(incOne(5))
print(incFive(5))
def makeInc(x):  
    def inc(y): 
        nonlocal x
        x += y  
        return x 
    return inc
incOne = makeInc(1) 
print(incOne(5))
def makeInc(x): 
    def inc(y):     
        nonlocal x   
        x += y       
        return x  
    return inc 
incOne = makeInc(1) 
print(incOne(5))
def fibonacci(n):    
    def step(a,b):        
        return b, a+b    
    a, b = 0, 1    
    for i in range(n):       
        a, b = step(a, b) 
    return a
def make_adder(n):    
    def adder(x):        
        return n + x   
    return adder
add5 = make_adder(5)
add6 = make_adder(6) 
print(add5(10), add6(10))
def repeatedly_apply(func, n, x):    
    for i in range(n):      
        x = func(x)   
    return x 
repeatedly_apply(add5, 5, 1)
def cursing(depth): 
    try:   
        cursing(depth + 1) 
    except RuntimeError as RE:    
        print('I recursed {} times!'.format(depth))
        
cursing(0)
lambda_factorial = lambda i : 1 if i==0 else i* lambda_factorial(i - 1) 
print(lambda_factorial(4))
def factorial(n):    
    if n == 0:       
        return 1    
    else:       
        return n * factorial(n - 1)
print(factorial(3))
factorial = lambda n : 1 if n == 0 else n * factorial(n - 1)

def divide(dividend, divisor):
    print(dividend / divisor)
print(divide(10, 2))
print(divide(divisor = 2, dividend = 10))

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
