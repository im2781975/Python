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
