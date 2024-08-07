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
