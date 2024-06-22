"""
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
    """
