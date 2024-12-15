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
