
#password generator
import random, string
icons = list(string.ascii_lowercase + string.ascii_uppercase)
icons = list(string.ascii_letters)
space = list(string.whitespace)
able = list(string.printable)
dig = list(string.digits)
punc = list(string.punctuation)
l = int(input("Enter require letters: "))
d = int(input("Enter require digits: "))
p = int(input("Enter require punctuation: "))
sign = []
for i in range(1, l + 1):    sign += random.choice(icons)
for i in range(1, d + 1):    sign += random.choice(dig)
for i in range(1, p + 1):    sign += random.choice(punc)
random.shuffle(sign); ing = ""
for i in sign:    ing += i
print(ing)
#password
symbol = string.punctuation + string.ascii_letters + string.digits
secure = random.SystemRandom()
print("".join(secure.choice(symbol) for i in range(10)))
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
# Who Has More Followers?
icon = (string.ascii_lowercase).lower()
data = [{"name" : icon[i], "roll" : i + 1}for i in range(26)]
def disp(account):    return account["name"]
def check(guess, cnt1, cnt2):
    return (guess == 1 and cnt1 > cnt2) or (guess == 2 and cnt1 < cnt2)
score = 0
b = random.choice(data)
while True:
    a = b
    b = random.choice(data)
    while a == b:    b = random.choice(data)
    print(f"1: {disp(a)}\n2: {disp(b)}")
    guess = int(input("who has more follower(1 or 2): "))
    cnt1, cnt2 = a["roll"], b["roll"]
    if(check(guess, cnt1, cnt2)):
        score += 1; print(score)
    else:    print(f"Final score: {score}"); break
#sum of even
res = 0
#for i in range(0, 101, 2):    res += i
for i in range(0, 101):
    if i % 2 == 0:    res += i
print(res) 
#print fizz, buzz, fizzbuzz based divisibil by 3, 5, 3 and 5
for i in range(0, 101):
    if i % 3 == 0 and i % 5 != 0:    print("Fizz", end = " ")
    elif i % 5 == 0 and i % 3 != 0:    print("Buzz", end = " ")
    elif i % 5 == 0 and i % 3 == 0:    print("FizzBuzz", end = " ")
    else:    print(i, end = " ")
else:    print()
#count color cane(a cane maximum paint 7sq)
import math
def countcane(height, width, cover):
    area = height * width
    print(math.ceil(area / cover), round(area / cover))
h = int(input("Enter height: "))
w = int(input("Enter weidth: "))
cv = 7; countcane(height = h, width = w, cover = cv)
#prime check
def prime(num):
    Isprime = True
    if num == 1:    Isprime = False
    for i in range(2, math.ceil(num / 2) + 1):
        if num % i == 0:    Isprime = False
    if Isprime:    print("prime")
    else:    print("composite")
prime(int(input("Enter number: ")))
# marks to grade
marks = {"A" : 23, "B" : 35, "C" : 78}
grade = {}
for i in marks:
    tag = marks[i]
    if tag >= 80:    grade[i] = "A+"
    elif tag >= 70:    grade[i] = "A"
    elif tag >= 60:    grade[i] = "A-"
    elif tag >= 50:    grade[i] = "B"
    elif tag >= 40:    grade[i] = "C"
    elif tag >= 33:    grade[i] = "D"
    else:    grade[i] = "F"
print(grade)
# split a balanced string which consists ['R', 'L'] into maximum number of substrings such that will be balanced.
def split(ing):
    cnt = L = R = 0
    lst = []
    for ch in ing:
        if ch == 'L':    L += 1
        elif    ch == 'R':    R += 1
        if X == Y:
            lst.append(ing[:L + R]); cnt += 1
            ing = ing[L + R:]; L = R = 0
    return cnt, lst
ing = input().strip()
cnt, balanced = split(ing); print(cnt)
for i in balanced:    print(i, end = " ")
# Count how many elements need to be removed so that each number x appears exactly x times.
from collections import defaultdict
n = int(input("Enter required: "))
ar = list(map(n, input().split()))
mp = defaultdict(int)
for num in ar:    mp[num] += 1
for num, cnt in mp.items():
    if cnt < num:    res += cnt
    else:    res += cnt - num
print(res)
#finds how many times all numbers in a list can be divided by 2
def maxi(lst):
    cnt = 0
    while all(n % 2 == 0 for n in lst):
        lst = [n // 2 for n in lst]; cnt += 1
    return cnt
n = int(input("Enter required: "))
lst = list(map(int, input().split()))
print(maxi(lst))    
#counts how many times each number from 1 to m appears in the input list of numbers,
n, m = map(int, input().split())
num = list(map(int, input().split()))
freq = [0] * (m + 1)
for i in num:    freq[i] += 1
for val in freq[1:]:    print(val, end = " ")
else:    print()
import string
icon = list(string.ascii_lowercase)
def encrypt(text, shift):
    ing = ""
    for i in text.lower():
        if i in icon:    ing += icon[(icon.index(i) + shift) % 26]
        else:    ing += i
    print(ing)
def decrypt(text, shift):
    ing = ""
    for i in text.lower():
        if i in icon:    ing += icon[(icon.index(i) - shift) % 26]
        else:    ing += i
    print(ing)
while True:
    choice = input("Enter 'encrypt' or 'decrypt': ").lower()
    msg = input("Enter message: ")
    shift = int(input("Enter shift key: "))
    if choice == 'encrypt':    encrypt(msg, shift)
    elif choice == 'decrypt':    decrypt(msg, shift)
    else:    print('Invalid')
    again = input("want to continue? (yes/no): ").lower()
    if again == "no":    break
#coffe machine
menu = {
    "latte" : {"ingredients" : {"water" : 200, "milk" : 150, "coffe" : 24}, "cost" : 150},
    "espresso" : {"ingredients" : {"water" : 50, "coffe" : 18}, "cost" : 100},
    "cappuccino" : {"ingredients" : {"water" : 250, "milk" : 100, "coffe" : 24}, "cost" : 200},
    "macciato" : {"ingredients" : {"water" : 150, "milk" : 100, "coffe" : 18}, "cost" : 150}
}
aid = {"water" : 900, "milk" : 700, "coffe" : 500}
profit = 0
def aidcheck(ingredients):
    for item, amount in ingredients.items():
        if amount > aid.get(item, 0):
            print(f"Not Enough {item}"); return False
    return True
def taskcoin():
    cnt5 = int(input("Enter 5units: ")) * 5
    cnt10 = int(input("Enter 10units: ")) * 10
    cnt20 = int(input("Enter 20units: ")) * 20
    return cnt5 + cnt10 + cnt20
def pagamento(payment, cost):
    global profit
    if payment >= cost:
        profit += cost; change = payment - cost
        print(change)
    else:    print(f"have to pay {cost - payment}")
def make(name, ingredients):
    for item, val in ingredients.items():
        aid[item] -= val
    print(f"Here is your: {name}")
def report():
    for item, val in aid.items():
        print(f"{item} : {val}")
def machine():
    choice = input("Enter choice: ")
    if choice == "off":
        print("shut down")
    elif choice == "report":    report()
    elif choice in menu:
        detect = menu[choice]
        if aidcheck(detect["ingredients"]):
            payment = taskcoin()
            if pagamento(payment, detect["cost"]):
                make(choice, detect["ingredients"])
    else:    print("Invalid choice")
    
machine()
#coin Toss
import random as rnd
side = rnd.randint(0, 1)
if side == 1:    print("Tail")
else:    print("Head")
#who pay the bill
data = ["Aa", "Bb", "Cc", "Dd"]; print(rnd.choice(data))
name = input("Enter names: ")
sp = name.split(" "); dist = len(sp)
x = rnd.randint(0, dist - 1); print(f"{sp[x]} will pay")
#Hide money
grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
pos = input("Enter pos: ")
r, c = int(pos[0]) - 1, int(pos[1]) - 1
grid[r][c] = "X"
for row in grid:    print(row)
#rock paper scisser
choices = ["rock", "paper", "scissors"]
user = int(input("Enter(0|1|2): "))
if user < 0 and user > 2:    print("Invalid")
else:
    print(f"You choice: {choices[user]}")
    comp = rnd.randint(0, 2)
    print(f"computer choice: {choices[comp]}")
    if user == comp:    print("Draw")
    elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):    print("win")
    else:    print("loss")
#calculate avg height & max height
height = input("Enter height: ")
lst = height.split(); cnt = 0
for i in lst:    cnt += 1
for i in range(0, cnt):    lst[i] = int(lst[i])
#for i in range(len(lst)):    lst[i] = int(lst[i])
res = avg = 0
for i in lst:    res += i
print(round(res / cnt))
maxi = lst[0]
for i in lst:
    if i > maxi:    maxi = i
print(maxi)
#add data
data = [
    {"name" : "Aa", "roll" : 10, "age" : 22, "course" : "python"},
    {"name" : "Bb", "roll" : 12, "age" : 23, "course" : "C++"},
    {"name" : "Cc", "roll" : 9, "age" : 21, "course" : "Java"}
    ]
def add(name, roll, age, course):
    data.append({"name" : name, "roll" : roll, "age" : age, "course" : course})
add("Dd", 15, 23, "Ruby")
for student in data:    print(student)
#Bidding Auction
def findwinner(bidders):
    winner = max(bidders, key = bidders.get)
    print(bidders)
    print(f"{winner} with highest bid {bidders[winner]}")
def findwinner(bidders):
    highest = 0, winner = ""
    for i in bidders:
        price = bidders[i]
        if price > highest:
            highest = price; winner = i
    print(bidders)
    print(f"{winner} with highest bid {bidders[winner]}")
bidders = {}
while True:
    name = input("Enter name: ")
    price = int(input("Enter price: "))
    bidders[name] = price
    more = input("Need more(Yes|No): ").lower()
    if more == "no":   
        print(bidders); findwinner(bidders)
        break
#leap days
def leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
def totalday(year, month):
    DaysList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap(year) and month == 2: return 29
    else:    return DaysList[month - 1]
year = int(input("Enter year: "))
month = int(input("Enter Month: "))
print(totalday(year, month)) 
#calculator
def add(a, b):    return a + b
def sub(a, b):    return a - b
def mult(a, b):    return a * b
def div(a, b):    return a / b
operations = {
    "+" : add, "-" : sub, "*" : mult, "/" : div
}
def calculator():
    x = float(input("Enter first: "))
    while True:
        #x = float(input("Enter first: "))
        for sym in operations:    print(sym, end = " ")
        print(); op = input("pick operation: ")
        y = float(input("Enter second: "))
        if op not in operations:
            print("Invalid"); continue
        res = operations[op](x, y)
        print(f"{x} {op} {y} = {res}")
        more = input("'y' = continue, 'n' = new calc,'x' = exit: ").lower()
        if more == 'y':    x = res
        elif more == 'n':    
            calculator()
        else:
            print("Bye")
            break
def calculator():
    x = float(input("Enter first: "))
    for sym in operations:    print(sym, end = " ")
    flag = True
    while flag:
        op = input("pick operation: ")
        y = float(input("Enter second: "))
        func = operations[op]
        res = func(x, y)
        print(f"{x} {op} {y} = {res}")
        more = input("'y' = continue, 'n' = new calc,'x' = exit: ").lower()
        if more == 'y':    x = res
        elif more == 'n':    
            flag = False; calculator()
        else:
            flag = False; print("Bye")
calculator()
#Guess the number
import random as rnd
EASY, HARD = 10, 5
def setdifficulty(lev):
    return EASY if lev == "easy" else HARD
def check(guess, res, attempts):
    if guess < res:
        print("low"); return attempts - 1
    elif guess > res:
        print("High"); return attempts - 1
    else:
        print(f"correct"); return 0;
def game():
    lev = input("choose difficulty(easy|hard): ").lower()
    print("assume between 1 to 50: ")
    res = rnd.randint(1, 50)
    if lev not in ["easy", "hard"]:
        print("Invalid"); return
    attempts = setdifficulty(lev)
    while attempts > 0:
        print(f"remaining: {attempts}")
        guess = int(input("Make a guess: "))
        attempts = check(guess, res, attempts)
        if attempts == 0 and guess != res:
            print(f"Lose. res is {res}")
        elif guess == res:    break
        else:    print("Guess Again")
game()
def game():
    lev = input("choose difficuly(easy|hard): ").lower()
    print("assume between 1 to 50: ")
    res = rnd.randint(1, 51)
    if lev not in ["easy", "hard"]:
        print("Invalid"); return
    if attempts != EASY and attempts != HARD:
        print("Wrong Entered")
    guess = 0
    while guess != res:
        print(f"{attempts} left")
        guess = int(input("Enter guess: "))
        attempts = check(guess, res, attempts)
        if attempts == 0:
            print("You lose"); break
        else:    print("Guess again")
import random as rnd
lst = ["apple", "beautiful", "potato"]
chosen, attempt, disp = rnd.choice(lst), 6, []
#disp = ["_"] * len(chosen)
#print(" ".join(disp))
for i in range(len(chosen)):    disp += '_'
print(disp)
over = False
while not over:
    guess = input("assume a letter: ").lower()
    for i in range(len(chosen)):
        word = chosen[i]
        if word == guess:    disp[i] = guess
    print(disp)
    if guess not in chosen:
        attempt -= 1
        if attempt == 0:
            over = True; print("lose")
            break
    if '_' not in disp:
        over = True; print("Win")
        break
"""
while True:
    guess = input("assume a letter: ").lower())
    if guess in chosen:
        for i, word in enumerate(chosen):
            if word == guess:    disp[i] = guess
            else:    attempt -= 1
    print(" ".join(disp))
    if "_" not in disp:
        print("win"); break
    if attempt == 0: 
        print(f"Lose.res is {chosen}")
        break
""'
#MULTIPLE CHOICE QUESTION
QueBank = [
    {"Quiz" : "1 + 1: ", "res " : "A"},
    {"Quiz" : "2 * 3: ", "res " : "D"},
    {"Quiz" : "6 / 3: ", "res " : "B"},
    {"Quiz" : "15 - 6: ", "res " : "C"},
    {"Quiz" : "2 ** 3: ", "res " : "C"},
    {"Quiz" : "15 % 2: ", "res " : "A"}
    ]
scelt = [ 
    ["A. 2", "B. 4", "C. 6", "D. 8"],
    ["A. 2", "B. 4", "C. 8", "D. 6"],
    ["A. 9", "B. 2", "C. 6", "D. 8"],
    ["A. 2", "B. 4", "C. 9", "D. 8"],
    ["A. 2", "B. 4", "C. 8", "D. 10"],
    ["A. 1", "B. 4", "C. 6", "D. 8"]]
score = 0
"""
for i, q in enumerate(QueBank):
    print(f"\nQ{i + 1 }. {q['Quiz']}")
    for opt in scelt[i]:
        print(opt)
    guess = input("assume res: ")
    if guess == q["res "]:
        score += 1; print("correct")
    else:    print(f"wrong.correct is {q["res "]} ")
print(f"Your total score: {score}/{len(QueBank)}")
print(f"Percentage: {score / len(QueBank) * 100:.1f}%")
"""
def check(guess, correct):
    if guess == correct:    return True
    else:    return False
for num in range(len(QueBank)):
    print(QueBank[num]["Quiz"])
    for i in scelt[num]:    print(i)
    guess = input("assume answer: ").upper()
    isright = check(guess, QueBank[num]["res "])
    if isright:    score += 1; print("correct")
    else:    print(f"incorrect.correct is {QueBank[num][" res"] }")
#dice game
dice = ["one", "Two", "three", "four", "five", "six"]
num = rnd.randint(0, 5); print(dice[num])
#Miliniel Year
year = int(input("Enter Year: "))
if year > 1980 and year <= 1996:    print("Millinel")
else:    print("GENZ")
#buy item
balance = 3000
def buy(item, price):
    global balance
    #balance = 3200
    print(f"previous balance: {balance} ")
    balance -= price
    print(f"After Buy balance: {balance} ")
buy('glass', 2200)
print('Global balance is: ', balance)
#coorinates
coordi = (3, 5)
x, y = coordi[0], coordi[1]
print(x, y)
#overlap
def overlap(lst, lis):
    for item in lst:
        if item in lis: return True
    return False
lst, lis = [1, 2, 3, 4, 5], [6, 2, 8, 9]
if overlap(lst, lis): print("Overlap")
else: print("Not Overlap")

def func(ch):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if ch in vowel:    return True
    else:    return False
seq = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
lst = list(filter(func, seq))
if 's' in lst:    print("Yes")
else:    print("No")
#count student
std = {}
def add(name = None):
    std['count'] = std.get('count', 0) + 1
    if name:    std.setdefault('names', []).append(name)
add("Alice"); add("Bob")
print(std)
#nth root
"""
def nth_root(x, n):
    high = 1
    while high ** n <= x: high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        mid_nth = mid ** n
        if low < mid and mid_nth < x:  low = mid        
        elif high > mid and mid_nth > x:   high = mid        
        else:   return mid    
    return mid + 1 
"""
def nth_root(x, n):
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        mid_pow = mid ** n
        if mid_pow == x:    return mid
        elif mid_pow < x:    low = mid + 1
        else:    high = mid - 1
    return high
x = 2 ** 100
cube = x ** 3
root = nth_root(cube, 3)
print(root == x)
#calculate BMI
weight = input("Entet weight: ")
height = input("Enter height: ")
bmi = int(weight) / float(height) ** 2
print(round(bmi, 2))
#count BMI
hight = float(input("Enter height: "))
weight = float(input("Enter weight: "))
bmi = weight / hight **2
if bmi < 18.5:    print(f"bmi {bmi} & underweight")
elif bmi < 25:    print(f"bmi {bmi} & normal weight")
elif bmi < 30:    print(f"bmi {bmi} & overweight")
elif bmi < 35:    print(f"bmi {bmi} & obese")
else:    print(f"bmi {bmi} & clinically unfit")
#rolear coaster billing
height = int(input("Enter height: "))
bill = 0
if height > 3:
    print("Enter ride")
    age = int(input("Enter age: "))
    if age < 12:
        bill = 150; print("Ticket price is 150")
    elif age <= 18:
        bill = 250; print("Ticket price is 250")
    else:
        bill = 500; print("Ticket price is 500")
    want_photo = input("Do you want to take a photo(y/n): ")
    if(want_photo == 'y' and want_photo != 'n'):
        bill += 50; print(f"Total bill is {bill}")
else:    print("Can't ride")
"""            PIZZA BILLING           """
size = input("which type of pizza you want(S/M/L/XL): ")
bill = 0
if size == 's' or size == 'S':
    bill += 150; print(f"Small pizza price is {bill}")
elif size == 'm' or size == 'M':
    bill += 200; print(f"Medium pizza price is {bill}")
elif size == 'l' or size == 'L':
    bill += 250; print(f"Large pizza price is {bill}")
else:
    bill += 300; print(f"Extra Large pizza price is {bill}")
add_peperoni = input("Do you want peperoni: ")
if add_peperoni == 'Y' or add_peperoni == 'y':
    if size == 's' or size == 'S':    bill += 30
    else:    bill += 50
add_cheese = input("Do you want cheese: ")
if add_cheese == 'Y' or add_cheese == 'y':
    if size == 's' or size == 'S':    bill += 20
    else:    bill += 50
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
    
