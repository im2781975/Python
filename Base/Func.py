def double_it(num):
    num = num*2
    print(num)
    return num
double_it(8)
double_it(9)

def sum(a, b, c = 0):
    res = a + b + c
    return res
#def sum(a, b):
    #res = a + b
    #return res
total = sum(23, 24)
print(total)

final = double_it(total)
print("Final value is:",final)

def all_sum(x, y, *args):
    print(args)
    s = 0
    for num in args:
        print(num)
        s+=num
    print(s)
        
t = all_sum(45, 56, 77, 89)
print(t)

#def full(title, first, last)
def full(*title, first, last):
    name = f'{title} {first} {last}'
    return name
def f(first, last, **add):
    name = f'{first} {last}'
    print(add['title'])
    for key,value in add.items():
        print(key, value)
#name = full('ibrahim', 'molla')
#name = full(last = 'molla', first = 'ibrahim')
#name = full(title = 'DJ', last = 'molla', first = 'ibrahim')
name = f(title = 'DJ', last = 'molla', first = 'ibrahim')
#print(name)

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
highest = max(1, 2, 3, 4, 5)
lowest = min(1, 2, 3, 4, 5)
count = len([1, 10])
s = sum([1, 2, 3, 4, 5])
print(highest, lowest, count, s)
