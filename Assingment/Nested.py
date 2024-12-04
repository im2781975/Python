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
    """
