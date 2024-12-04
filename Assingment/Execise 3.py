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
