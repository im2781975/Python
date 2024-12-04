size = input("which type of pizza you want(S/M/L/XL): ")
bill = 0
if size == 's' or size == 'S':
    bill += 150
    print(f"Small pizza price is {bill}")
elif size == 'm' or size == 'M':
    bill += 200
    print(f"Medium pizza price is {bill}")
elif size == 'l' or size == 'L':
    bill += 250
    print(f"Large pizza price is {bill}")
else:
    bill += 300
    print(f"Extra Large pizza price is {bill}")
add_peperoni = input("Do you want peperoni: ")
if add_peperoni == 'Y' or add_peperoni == 'y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50
add_cheese = input("Do you want cheese: ")
if add_cheese == 'Y' or add_cheese == 'y':
    if size == 's' or size == 'S':
        bill += 20
    else:
        bill += 50
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
    
