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
add_cheese = input("Do you want peperoni: ")
if add_cheese == 'Y' or add_cheese == 'y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50
