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
