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

#list is changeable but tuple no
def Muteable(lst):
    lst.append(3)
x = [2, 5]
Muteable(x), print(x)

def Immuteable(lst):
    lst.append(3)
x = (2, 5)
Immuteable(x), print(x)
