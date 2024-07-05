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
