#choose
import random 
diceNum = ["one", "Two", "three", "four", "five", "six"]
num = random.randint(0, 5)
print(diceNum[num])

#Miliniel or not
year = int(input("Enter Year:"))
if year > 1980 and year <= 1996:
    print("Millenial")
elif:
    print("Gen Z")

#can vote or not
age = int(input("Enter age:"))
if age >= 18:
    print("vote")
else:
    print("can't vote")

#sum digits of a integer
num = input("Enter integer:")
first = num[0]
sec = num[1]
print(int(first) + int(sec))

#sum & mult
first = input("Enter first: ")
sec = input("Enter second: ")
intFirst = int(first)
intSec = int(sec)
print(f"Sum is: {intFirst + intSec}\nSubtract is: {intFirst - intSec}\nMult is: {intFirst * intSec}\nDiv is: {intFirst / intSec}\nModulo is: {intFirst % intSec}")

#buy item
balance = 3000
def buy(item, price):
    #access global variable
    global balance
    #balance = 3200
    print(f"previous balance: {balance} ")
    balance -= price
    print(f"After Buy balance: {balance} ")
buy('glass', 2200)
print('Global balance is: ', balance)


#Board To metro
height = int(input("Enter height: "))
if height > 3:
    print("Token required")
    print("Board metro")
else:
    print("No Token Required")
#Even or odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#digit sum of odd numbers
def digsum(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total
lst = [367, 111, 562, 945, 6726, 873]
newlist = [digsum(i) for i in lst if i & 1]
print(newlist)

#check wheather a number even or odd
def evenOdd(x):
    print("Even" if x % 2 == 0 else "Odd")
evenOdd(22)

coordinates = (3, 5)
x = coordinates[0]
y = coordinates[1]
print(f"X axis: {x}\nY axis: {y} ")
#overlap
def overlap(lst, lis):
    for item in lst:
        if item in lis:
            return True
    return False
lst = [1, 2, 3, 4, 5]
lis = [6, 2, 8, 9]
if(overlap(lst, lis)):
    print("Overlap")
else:
    print("Not Overlap")
# Even or odd
seq = [0, 1, 1, 2, 3, 5, 8, 13]
res = filter(lambda x : x % 2 == 0, seq)
res = filter(lambda x : x % 2 != 0, seq)
print(list(res))
#IsMultiple
def Ismultiple(num):
    return num % 3 == 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = list(filter(lambda x : Ismultiple(x), num))
print(res)
Even = [i for i in num if i % 2 == 0]
print(Even)
#split str
text = "Python is awesome and versatile"
filt = [word for word in text.split() if 'o' in word]
print(filt) 

def func(val):
    letter = ['a', 'e', 'i', 'o', 'u']
    if val in letter:
        return True
    else:
        return False
seq = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filt = filter(func, seq)
lst = list(filt)
if 's' in filt:
    print("Yes")
else:
    print("No")

def cube(x):
    return x * x * x
lambcube = lambda x : x * x * x
print(cube(5), lambcube(5))
#MultList
multList = [lambda arg = x : arg * 10 for x in range(1, 10)]
for item in multList:
    print(item(), end = " ")
#MaxMin
maxi = lambda a, b : a if (a > b) else b
print(maxi(3, 8))
#secondLargest
lst = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sortList = lambda x : (sorted(i) for i in x)
secondLargest = lambda x, f : [y[ -2] for y in f(x)]
res = secondLargest(lst, sortList);
print(res)
#oddList, square, adult
lst = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
oddList = list(filter(lambda x : (x % 2 != 0), lst))
square = list(map(lambda x : x ** 2, lst))
adult = list(filter(lambda age : age > 18, lst))
print(oddList, square, adult)

#upper
animals = ['dog', 'cat', 'parrot', 'rabbit']
print(list(map(lambda animal : animal.upper(), animals)))
#count student 
students = {}
def add(name = None):
    students['count'] = students.get('count', 0) + 1
    if name:
        students.setdefault('names', []).append(name)
add("Alice")
add("Bob")
print(students)
"""						"""
def nth_root(x, n):    
    upper_bound = 1    
    while upper_bound ** n <= x:        
        upper_bound *= 2    
    lower_bound = upper_bound // 2    
    while lower_bound < upper_bound:      
        mid = (lower_bound + upper_bound) // 2        
        mid_nth = mid ** n        
        if lower_bound < mid and mid_nth < x:            
            lower_bound = mid        
        elif upper_bound > mid and mid_nth > x:          
            upper_bound = mid        
        else:             
            return mid    
    return mid + 1 
x = 2 ** 100 
cube = x ** 3 
root = nth_root(cube, 3)
x == root
"""                    """
import numpy as np
from scipy.constants import h, k, c
def planks_law_math(lambda_, T):
    return 2 * h * c ** 2 / (lambda_ ** 5 * math.expm1(h * c / (lambda_ * k * T)))
def planks_law_naive_math(lambda_, T):
    return 2 * h * c ** 2 / (lambda_ ** 5 * (math.e ** (h * c / (lambda_ * k * T)) - 1))
def planks_law_numpy(lambda_, T):
    lambda_ = np.array(lambda_, dtype=np.float64)  
    return 2 * h * c ** 2 / (lambda_ ** 5 * np.expm1(h * c / (lambda_ * k * T)))

lambda_values = [100, 100]
T = 5000  
results_math = [planks_law_math(l, T) for l in lambda_values]
results_naive_math = [planks_law_naive_math(l, T) for l in lambda_values]
results_numpy = planks_law_numpy(lambda_values, T)
print("Results using math library:")
print("planks_law_math:", results_math)
print("planks_law_naive_math:", results_naive_math)
print("\nResults using numpy:")
print("planks_law_numpy:", results_numpy)
