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
        
        
