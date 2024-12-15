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
