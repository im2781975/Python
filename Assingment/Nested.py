#height check
height = int(input("Enter height: "))
if height > 3:
    print("Enter ride")
    age = int(input("Enter age: "))
    if age < 12:
        print("Have to pay 150")
    elif age < 18:
        print("Have to pay 250")
    else:
        print("Have to pay 500")
else:
    print("Can't ride")
#number check
num = int(input("Enter Integer: "))
if (num % 2 == 0):
    print("Even")
    if num > 30:
        print("Greater than 30")
    else:
        print("Less than 30")
else:
    print("Odd");
#calculate bmi
weight = input("Entet weight: ")
height = input("Enter height: ")
bmi = int(weight)/float(height)**2
print(round(bmi, 2))
#left age
age = int(input("Enter age: "))
year_left = 90 - age
days_left = year_left*365
month_left = year_left*12
weeks_left = year_left * 52
print(f"you have left {days_left} days, {month_left} months, {weeks_left} weeks")
#count BMI
hight = float(input("Enter height: "))
weight = float(input("Enter weight: "))
bmi = weight/hight**2
if bmi < 18.5:
    print(f"your bmi is {bmi} & you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} & you are normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} & you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi} & you are obese")
else:
    print(f"your bmi is {bmi} & you are clinically unfit")
    
#leap year
num = int(input("Enter Year: "))
if (num % 4 == 0 and num % 100 !=0) or (num % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#rolear coaster billing
height = int(input("Enter height: "))
bill = 0
if height > 3:
    print("Enter ride")
    age = int(input("Enter age: "))
    if age < 12:
        bill = 150
        print("Ticket price is 150")
    elif age <= 18:
        bill = 250
        print("Ticket price is 250")
    else:
        bill = 500
        print("Ticket price is 500")
    want_photo = input("Do you want to take a photo(y/n): ")
    if(want_photo == 'y' and want_photo != 'n'):
        bill += 50
    print(f"Total bill is {bill}")
else:
    print("Can't ride")
    """				pizza billing		"""
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
    
