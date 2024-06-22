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

