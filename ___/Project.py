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
#coin Toss
import random
side = random.randint(0, 1)
print(side)
if side == 1:
    print("Tail")
else:
    print("Head")
#who pay bill
import random
l = ["Ab", "Bc", "Cd", "De"]
x = random.choice(l)

#splited txt
text = "Ab Bc Cd De"
splited_txt = text.split(" ")
print(splited_txt)

name = input("Enter name separated by space: ")
splited = name.split(" ")
length = len(splited)
x = random.randint(0, length -1)
print(f"{splited[x]} will pay the bill ")

#Hide money
row1 = [-1, -1, -1]
row2 = [-1, -1, -1]
row3 = [-1, -1, -1]
matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3} ")
position = input("Enter position: ");
row = int(position[0])
col = int(position[1])
row_select = matrix[row - 1];
row_select[col - 1] = 'x';
print(f"{row1}\n{row2}\n{row3} ")

#rock-paper-scissors
# 0 -> Rock, 1->paper, 2->scissors
from random import *
GameImages = ["rock", "paper", "scissors"]
user = int(input("Enter (0/1/2): "))
if user >= 3 and user < 0:
    print("Invalid Input")
else:
    print(f"You choose {user} which is: {GameImages[user]} ")
    computer = randint(0, 2)
    print(f"Computer choice: {computer} which is {GameImages[computer]}")
    if user == computer:
        print("draw")
    elif computer == 0 and user == 2:
        print("You lose")
    elif user == 0 and computer == 2:
        print("You win")
    elif user > computer:
        print("You win")
    elif user < computer:
        print("You lose")

#calculate avg height from a list of height
height = input("Enter height: ")
height_list = height.split()
cnt = 0
for height in height_list:
    cnt += 1
for i in range(0, cnt):
    height_list[i] = int(height_list[i])
total = 0
for val in height_list:
    total += val
avg = 0
avg = total/cnt
print(round(avg))

#calculate maximum number
num = input("Enter values: ")
val = num.split()
cnt = 0
for i in val:
    cnt += 1
for i in range(len(val)):
    val[i] = int(val[i])
maxi = val[0]
for i in val:
    if i > maxi:
        maxi = i
print(maxi)

#Add Data in Dict
studentData = [
    {"Name: ":"A", "roll": 10, "Age": 22, "course": "python",},
    {"Name: ": "B", "roll": 12, "Age": 24, "course": "java",}
]
def AddData(name, rollno, age, Course):
    newStudent = {}
    newStudent["Name"] = name
    newStudent["roll"] = rollno
    newStudent["Age"] = age
    newStudent["course"] = Course
    studentData.append(newStudent)
AddData("C", 15, 23, "C++")
print(studentData)
#Bidd Auction
def FindWinner(BidderData):
    highest = 0
    winner = ""
    for i in BidderData:
        BiddingPrice = BidderData[i]
        if BiddingPrice > highest:
            highest = BiddingPrice
            winner = i
    print(BidderData)
    print(f"{winner} with highest Bid {highest} ")
        
BidderData={}
EndOfBidding = False
while not EndOfBidding: 
    name = input("Enter Name: ")
    price = int(input("Enter Price: "))
    BidderData[name] = price
    MoreBidder = input("More Bidder?Type 'yes' or 'no': ").lower()
    if MoreBidder == 'no':
        EndOfBidding = True
        FindWinner(BidderData)
#Leap year Day count
def LeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def DaysInMonth(year, month):
    DaysList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if LeapYear(year) and month == 2:
        return 29
    else:
        return DaysList[month - 1]
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
print(DaysInMonth(year, month))

#Calculator
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def Div(a, b):
    return a/b
Operations = {
    "+" : add, "-" : sub, "*" : mult, "/" : Div,
}
def Calculator():
    num = int(input("Enter num: "))
    for i in Operations:
        print(i)
    flag = True
    while flag:
        symbol = input("Pick an Operation: ")
        num2 = int(input("Enter 2nd Number: "))
        CalculatorFunc = Operations[symbol]
        output = CalculatorFunc(num, num2)
        print(f"{num} {symbol} {num2} = {output} ")
        ShouldContinue = input(f"Enter 'y' to continue with {output} & 'n' for continue with new calculation else 'x' for exits ").lower()
        if ShouldContinue == 'y':
            num = output
        elif ShouldContinue == 'n':
            flag = False
            Calculator()
        elif ShouldContinue == 'x':
            flag = False
            print("Bye")
Calculator()
#Guess the number
import random
EasyLevel = 10
HardLevel = 5
def SetDifficulties(level):
    if level == 'easy':
        return EasyLevel
    if level == 'hard':
        return HardLevel
def CheckNumber(GuessNumber, ans, attempt):
    if GuessNumber < ans:
        print("Guess is too low")
        return attempt - 1
    elif GuessNumber > ans:
        print("Guess is too high")
        return attempt - 1
    else:
        print(f"Guess is right..ans is {answer} ")
print("Assume number from 1 to 50: ")
answer = random.randint(1, 51)
level = input("choose difficulty...'easy' or 'hard': ")
attempt = SetDifficulties(level)
if attempt != EasyLevel and attempt != HardLevel:
    print("Wrong Entered.play again")
    
GuessNumber = 0
while GuessNumber != answer:
    print(f"{attempt} left ")
    GuessNumber = int(input("Guess Number: "))
    attempt = CheckNumber(GuessNumber, answer, attempt)
    if attempt == 0:
        print("You loose")
        break
    elif GuessNumber != answer:
        print("Guess again")
#Hangman
import random
word_list = ["apple", "beautiful", "potato"]
live = 6
choosen_word = random.choice(word_list)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
Game_Over = False
while not Game_Over:
    guess_letter = input("Guess a letter: ").lower()
    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter == guess_letter:
            display[i] = guess_letter
    print(display)
    if guess_letter not in choosen_word:
        live -= 1
        if live == 0:
            Game_Over = True
            print("You Lose")
        if '_' not in display:
            Game_Over = True
            print("You win")
#Quiz Test   
QueBank = [
    {"text" : "1 + 1 = ", "answer" : "A"},
    {"text" : "2 * 3 = ", "answer" : "D"},
    {"text" : "6 / 3 = ", "answer" : "B"},
    {"text" : "15 - 6 = ", "answer" : "C"},
    {"text" : "2 ** 3 = ", "answer" : "C"},
    {"text" : "15 % 2 = ", "answer" : "A"}
    ]
Options = [ 
    ["A. 2", "B. 4", "C. 6", "D. 8"],
    ["A. 2", "B. 4", "C. 8", "D. 6"],
    ["A. 9", "B. 2", "C. 6", "D. 8"],
    ["A. 2", "B. 4", "C. 9", "D. 8"],
    ["A. 2", "B. 4", "C. 8", "D. 10"],
    ["A. 1", "B. 4", "C. 6", "D. 8"]]
score = 0
def checkAns(userGuess, correctAns):
    if userGuess == correctAns:
        return True
    else:
        return False
for QueNum in range(len(QueBank)):
    print(QueBank[QueNum]["text"])
    for i in Options[QueNum]:
        print(i)
    guess = input("Enter answer(A / B / C / D): ").upper()
    IsCorrect = checkAns(guess, QueBank[QueNum]["answer"])
    if IsCorrect:
        score += 1
        print("Correct Answer")
    else:
        print("Incorrect Answer")
        print(f"Correct answer is: {QueBank[QueNum]["answer"] }")
print(f"Total score is {score}")
print(f"Score is: {(score / len(QueBank))*100} %")
