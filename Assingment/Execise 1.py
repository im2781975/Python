#password Generator
import string, random
letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letters =list(string.ascii_letters)
spaces = list(string.whitespace)
printable =list(string.printable)
digit =list(string.digits)
punctuation = list(string.punctuation)
print("Password Generator: \n")
l = int(input("Enter Number of letter: "))
d = int(input("Enter Number of digits: "))
p = int(input("Enter Number of punctuation: "))
password = []
for i in range(1, l + 1):
    char = random.choice(letter)
    password += char
for i in range(1, d + 1):
    char = random.choice(digit)
    password += char
for i in range(1, p + 1):
    char = random.choice(punctuation)
    password += char
random.shuffle(password)
print(password)
Generated = ""
for i in password:
    Generated += i
print(Generated)

#sum of the even num from 0 to 100
total = 0
#for i in range(0, 101, 2):
    #total += i 
for i in range(0, 101):
    if i % 2 == 0:
        total += i
print(total) 
#print numbers range(0, 100) where divisible by 3, 5, 3 and 5. instead of i print frizz, buzz, frizzbuzz
for i in range(101):
    if i % 3 == 0 and i % 5!= 0:
        print(i, "Fizz")
    elif i % 5 == 0 and i % 3 !=0:
        print(i, "Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    else:
        print(i)

#How many canes Of color need to paint a wall.(a cane max paint 7sq area )
import math
def PaintCalculation(height, weidth, coverage):
    area = height * weidth
    #NoOfCanes = round(area / coverage)
    NoOfCanes = math.ceil(area / coverage)
    print(f"{NoOfCanes} Canes need ")
h = int(input("Enter height: "))
w = int(input("Enter Weidth: "))
cover = 7
PaintCalculation(height = h, weidth = w, coverage = cover)

#prime checker
import math
def PrimeChecker(num):
    IsPrime = True
    if num == 1:
        IsPrime = False
    for i in range(2, math.ceil(num/2) + 1):
        if num % i == 0:
            IsPrime = False
    if IsPrime == True:
        print("Prime Number")
    else:
        print("Its not a prime number")
num = int(input("Enter number: "))
PrimeChecker(num)

#marks to grade
studentMarks = { "A":23, "B": 35, "C":78}
grade = {}
for i in studentMarks:
    marks = studentMarks[i]
    if marks > 90:
        grade[i] = "A+"
    elif marks > 80:
        grade[i] = "A"
    elif marks > 70:
        grade[i] = "B+"
    elif marks > 60:
        grade[i] = "B"
    elif marks > 50:
        grade[i] = "C"
    elif marks > 40:
        grade[i] = "D"
    else:
        grade[i] = "F"
print(grade)
# split a balanced string which consists ['R', 'L'] into maximum number of 
# strings such that the new strings are also balanced.
def split(ing):
    cnt = cntX = cntY = 0
    balanced = []
    for ch in ing:
        if ch == 'L':
            cntX += 1
        elif ch == 'R':
            cntY += 1
        if cntX == cntY:
            balanced.append(ing[:cntX + cntY])
            cnt += 1
            ing = ing[cntX + cntY:]
            cntX = cntY = 0
    return cnt, balanced
ing = input().strip()
cnt, balanced = split(ing)
print(cnt)
for rin in balanced:
    print(rin, end = " ")
# from a sequence of positive integers have to remove some of the elements so that it will be a good sequence.
# sequence b is a good sequence when each element of x in b, occurs exactly x times in b.
# Find the minimum number of elements that needs to be removed so that it will be a good sequence.
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
mp = defaultdict(int)
for num in a:
    mp[num] += 1
ans = 0
for num, count in mp.items():
    if count < num:
        ans += count
    else:
        ans += count - num
print(ans)
#Minimize a number
def maxi(N, x):
    cnt = 0
    while all(num % 2 == 0 for num in x):
        x = [num // 2 for num in x]
        cnt += 1
    return cnt
num = int(input(""))
ing = input("")
lst = list(map(int, ing.split()))
print(maxi(num, lst))
#Freq array
n, m = map(int, input().split())
num = list(map(int, input().split()))
freq= [0] * (m + 1)

for i in num:
    freq[i] += 1
for val in freq[1:]:
    print(val)
#Cypher
import string
letter = list(string.ascii_lowercase)
def encryption(text, shiftKey):
    cypherText = ""
    for i in text:
        if i in letter:
            position = letter.index(i)
            NewPos = (position + shiftKey) % 26
            cypherText += letter[NewPos]
        else:
            cypherText += i
    print(f"After Encryption Text is: {cypherText} ")
def decryption(text, shiftKey):
    PlainText = ""
    for i in text:
        if i in letter:
            position = letter.index(i)
            NewPos = (position - shiftKey) % 26
            PlainText += letter[NewPos]
        else:
            PlainText += i
    print(f"After Decryption Text is: {PlainText} ")
Flag = False
while not Flag:
    ToDo = input("'Encrypt' for encryption, 'Decrypt' for decryption: ")
    text = input("Enter message: ").lower()
    shift = int(input("Type Shift Key: "))
    if ToDo == 'Encrypt':
        encryption(text, shift)
    elif ToDo == 'Decrypt':
        decryption(text, shift)
    Again = input("Enter 'Yes' for continue 'No' for exit")
    if Again == 'No':
        Flag = True
#Higher lower game
import string, random
letter = list(string.ascii_lowercase)
StudentData = [{"Name ": "a", "roll ": 1},]
def add_data(name, roll):
    newDict = {}
    newDict["Name"] = name
    newDict["roll"] = roll
    StudentData.append(newDict)
for i in range(1, 26):
    add_data(letter[i], i + 1)
def DisplayAccount(account):
    name= account["Name"]
    return f"{name}"
def CheckAnswer(guess, cnt1, cnt2):
    if cnt1 < cnt2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
score = 0
b = random.choice(StudentData)
Flag = True
while Flag:
    a = b
    b = random.choice(StudentData)
    while a == b:
        b = random.choice(StudentData)
    print(f"Compare 1: {DisplayAccount(a)} ")
    print(f"Compare 2: {DisplayAccount(b)} ")
    guess = int(input("who has more follower(Type 1 or 2): "))
    cnt1 = a["roll"]
    cnt2 = b["roll"]
    CheckAnswer(guess, cnt1, cnt2)
    IsCorrect = CheckAnswer(guess, cnt1, cnt2)
    if IsCorrect == True:
        score += 1
        print(f"Score is: {score} ")
    else:
        print(f"Score is: {score} ")
        Flag = False

#coffe machine
Menu = {
    "latte" :{
        "ingredients": {
            "water": 200,
            "milk" : 150,
            "coffe" : 24,
        },
        "cost": 150,
    },
    "espresso" :{
        "ingredients": {
            "water": 50,
            "coffe" : 18,
        },
        "cost": 100,
    },
    "cappuccino" :{
        "ingredients": {
            "water": 250,
            "milk" : 100,
            "coffe" : 24,
        },
        "cost": 200
    }
}
resources = {
    "water": 500,
    "milk" : 200,
    "coffe" : 100,
}
def CheckResources(Ingredients):
    for item in Ingredients:
        if Ingredients[item] > resources[item]:
            print(f"Not Enough {item}")
            return False
    return True
def ProcessCoin():
    print("please Insert coin: ")
    total = 0
    coinFive = int(input("No of CoinFive: "))
    coinTen = int(input("No of CoinTen: "))
    coinTwenty = int(input("No of CoinTwenty: "))
    total = coinFive * 5 + coinTen * 10 + coinTwenty * 20
    return total
def IsPaymentSuccess(money, cost):
    if money >= cost:
        global profit
        profit += cost
        change = money - cost
        print(f"Here is your change: {change} ")
        return True
    else:
        print(f"please provide more {cost - money}")
        return False
def MakeCoffe(name, Ingredients):
    for item in Ingredients:
        resources[item] -= Ingredients[item]
    print(f"Here is your {name}. Enjoy!!\n")
profit = 0
IsOn = True
while IsOn:
    choice = input("what you like to have(latte/ espresso/ cappuccino): ")
    if choice == 'off':
        IsOn = False
    if choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"milk: {resources['milk']}ml")
        print(f" coffe: {resources['coffe']} ml")
        print(f"Money: {profit} ")
    else:
        Type = Menu[choice]
        print(Type)
        if(CheckResources(Type['ingredients'])):
            payment = ProcessCoin()
            if IsPaymentSuccess(payment, Type['cost']):
                MakeCoffe(choice, Type['ingredients'])
