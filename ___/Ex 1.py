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
"""				"""
import random
from string import punctuation, ascii_letters, digits
symbols = punctuation + ascii_letters + digits
secure = random.SystemRandom()
password = "".join(secure.choice(symbols)for i in range(10))
print(password)
"""				"""
import string
from random import SystemRandom
secure = SystemRandom()
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secure.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and sum(c.isdigit() for c in password) >= 3):
        break
print("Generated secure password:", password)
print("List of 10 random digits:", [secure.randrange(10) for i in range(10)])
print("Random integer between 0 and 20:", secure.randint(0, 20))
#height check
height = int(input("Enter height: "))
if height > 3:
    print("Enter ride")
    age = int(input("Enter age: "))
    if age < 12:
        print("Have to pay 150")
    elif age < 18:
        print("Have to pay 250")
    else:
        print("Have to pay 500")
else:
    print("Can't ride")
#number check
num = int(input("Enter Integer: "))
if (num % 2 == 0):
    print("Even")
    if num > 30:
        print("Greater than 30")
    else:
        print("Less than 30")
else:
    print("Odd");
#calculate bmi
weight = input("Entet weight: ")
height = input("Enter height: ")
bmi = int(weight)/float(height)**2
print(round(bmi, 2))
#left age
age = int(input("Enter age: "))
year_left = 90 - age
days_left = year_left*365
month_left = year_left*12
weeks_left = year_left * 52
print(f"you have left {days_left} days, {month_left} months, {weeks_left} weeks")
#count BMI
hight = float(input("Enter height: "))
weight = float(input("Enter weight: "))
bmi = weight/hight**2
if bmi < 18.5:
    print(f"your bmi is {bmi} & you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} & you are normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} & you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi} & you are obese")
else:
    print(f"your bmi is {bmi} & you are clinically unfit")
    
#leap year
num = int(input("Enter Year: "))
if (num % 4 == 0 and num % 100 !=0) or (num % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#rolear coaster billing
height = int(input("Enter height: "))
bill = 0
if height > 3:
    print("Enter ride")
    age = int(input("Enter age: "))
    if age < 12:
        bill = 150
        print("Ticket price is 150")
    elif age <= 18:
        bill = 250
        print("Ticket price is 250")
    else:
        bill = 500
        print("Ticket price is 500")
    want_photo = input("Do you want to take a photo(y/n): ")
    if(want_photo == 'y' and want_photo != 'n'):
        bill += 50
    print(f"Total bill is {bill}")
else:
    print("Can't ride")
    """				pizza billing		"""
size = input("which type of pizza you want(S/M/L/XL): ")
bill = 0
if size == 's' or size == 'S':
    bill += 150
    print(f"Small pizza price is {bill}")
elif size == 'm' or size == 'M':
    bill += 200
    print(f"Medium pizza price is {bill}")
elif size == 'l' or size == 'L':
    bill += 250
    print(f"Large pizza price is {bill}")
else:
    bill += 300
    print(f"Extra Large pizza price is {bill}")
add_peperoni = input("Do you want peperoni: ")
if add_peperoni == 'Y' or add_peperoni == 'y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50
add_cheese = input("Do you want cheese: ")
if add_cheese == 'Y' or add_cheese == 'y':
    if size == 's' or size == 'S':
        bill += 20
    else:
        bill += 50
print(f"Final bill is {bill}")
#count Occurance
name1 = input("Enter string: ")
name2 = input("Enter string2: ")
combine = name1 + name2
convert_lower = combine.lower()
t = convert_lower.count('t')
r = convert_lower.count('r')
u = convert_lower.count('u')
e = convert_lower.count('e')
true = t + r + u + e
l = convert_lower.count('l')
o = convert_lower.count('o')
v = convert_lower.count('v')
e = convert_lower.count('e')
love = l + o + v + e
score = int(str(true) + str(love))
if(score < 10 or score > 90):
    print(f"Score is: {score} which between 10 & 90")
elif(score <= 40 or score >= 60):
    print(f"Score is: {score} which between 40 & 60")
else:
    print(f"Score is {score}")
    
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
"""            """
from functools import reduce
def factorial(n):
    return reduce(lambda a, b: (a * b), range(1, n + 1)
