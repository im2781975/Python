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
