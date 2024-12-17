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
