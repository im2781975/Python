def double_it(num):
    num = num*2
    print(num)
double_it(8)
double_it(9)
double = lambda x : x*2
square = lambda x : x*x
add = lambda x, y : x+y
ded = lambda x, y : x - y
mult = lambda x, y : x*y
div = lambda x, y : x/y
div_int = lambda x, y: x//y
Rem = lambda x, y : x%y
print(f'double is :{double(78)}')
print(f'Square is :{square(89)}')
print(f'addition is :{add(34, 78)}')
print(f'deduction is :{ded(34, 78)}')
print(f'Multiplication is :{mult(34, 78)}')
print(f'Division is :{div(78, 34)}')
print(f'Div_int is: :{div_int(78, 34)}')
print(f'Remainder is: :{Rem(78, 34)}')
def s(a, b, c = 0):
    res = a + b + c
    return res
#def sum(a, b):
    #res = a + b
    #return res
total = s(23, 24)
print("Total value:",total)

final = double_it(total)
print("Final value is:",final)
#Without return it will show None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#E = map(square,numbers)
E = map(lambda x: x**2,numbers)
print(list(E))
#args
def all_(*nu):
    to = 0
    for num in nu:
        print(num)
        to += num
        print(to)
    return nu
xy = all_(23, 45, 89)
print(xy)

#minimum required two parametre
def all_sum(x, y, *args):
    print(args)
    s = 0
    for num in args:
        print(num)
        s+=num
    print(s)
        
t = all_sum(45, 56, 77, 89)
print(t)

def full_name(first, last):
    name = f'Name is {first} {last}'
    return name
#name = full_name('Molla', 'ibrahim')
name = full_name(first = 'Molla', last = 'ibrahim')
print(name)

actress = [
    {'name' : 'A', 'age' :12 },
    {'name' : 'B', 'age' :17 },
    {'name' : 'C', 'age' :25 },
    {'name' : 'D', 'age' :35 },
    ]
juniors = filter(lambda x : x['age'] < 25,actress)
Fiver = filter(lambda x : x['age'] % 5 == 0, actress)
print(list(Fiver))
print(list(juniors))
#kargs
def famous_name(first, last,**addition):
    name = f'Info is {last} {first}'
    #print(addition)
    #print(addition['title'])
    for key,value in addition.items():
        print(key, value)
    return name
xy = famous_name(first = 'Molla', last = 'ibrahim', title = "Worker", addition = "Student")
print(xy)

def full(*title, first, last):
    name = f'{title} {first} {last}'
    return name
    
#name = full('ibrahim', 'molla')
#name = full(last = 'molla', first = 'ibrahim')
#name = full(title = 'DJ', last = 'molla', first = 'ibrahim')
print(name)

def a_lot(a, b):
    add = a+b
    mult = a*b
    remain = a-b
    return [add, mult, remain]
    #return add, mult, remain
res = a_lot(5, 9)
print(res)

balance = 3000
def buy(item, price):
    #for used global balance
    global balance
   # balance = 2200
    print(f'previous balance:',balance)
    balance-=price
    print(f'After buying {item} balance:',balance)
buy('glass', 1000)
print(f'global accessed balance is:',balance)

#from build-in import build as b
#from build-in import *(all)
#from [file name] import [function] as [our choice name]
from func import double_it as dt
result = dt(5)
print(result)
highest = max([1, 2, 3, 4, 5])
print("Highest value is:",highest)
smallest = min(1, 2, 3, 4, 5)
print("Lowest value is:",smallest)
count = len([1, 5])
s = sum([1, 2, 3, 4, 5])
print(highest,smallest,count,s)
