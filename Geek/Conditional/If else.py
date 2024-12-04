# python program to illustrate If statement
i = 10

if (i > 15):
    print("10 is less than 15")
print("I am Not in if")
////
# python program to illustrate else if in Python statement
#!/usr/bin/python

i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")

/////
# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)
////
# python program to illustrate nested If statement

i = 10
if (i == 10):
  
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
        
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
////
# Python program to illustrate if-elif-else ladder
#!/usr/bin/python

i = 25
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")
////
# Python program to illustrate short hand if
i = 10
if i < 15: print("i is less than 15")
///
# Python program to illustrate short hand if-else
i = 10
print(True) if i < 15 else print(False)
////

x = 0

# traditional python if elif else statement
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
////
x = 0

# Python one liner if elif else statement
result = {x > 0: "Positive", x < 0: "Negative"}.get(True, "Zero")

print(result)
/////
x = 0

{x > 0: print("Positive"), x < 0: print("Negative")}.get(True, print("Zero"))
////
# if statement example 
if 10 > 5: 
    print("10 greater than 5") 
  
print("Program ended") 
////
# if..else statement example 
x = 3
if x == 4: 
    print("Yes") 
else: 
    print("No") 
////
# if..else chain statement 
letter = "A"
  
if letter == "B": 
    print("letter is B") 
  
else: 
  
    if letter == "C": 
        print("letter is C") 
  
    else: 
  
        if letter == "A": 
            print("letter is A") 
  
        else: 
            print("letter isn't A, B and C")
////
# Nested if statement example 
num = 10
  
if num > 5: 
    print("Bigger than 5") 
  
    if num <= 15: 
        print("Between 5 and 15") 
////
# if-elif statement example 
letter = "A"
  
if letter == "B": 
    print("letter is B") 
  
elif letter == "C": 
    print("letter is C") 
  
elif letter == "A": 
    print("letter is A") 
  
else: 
    print("letter isn't A, B or C")
////
# Python code to demonstrate the syntax of if statement

gfg = 9

# if statement with true condition
if gfg < 10:
    print(f"{gfg} is less than 10")

# if statement with false condition
if gfg > 20:
    print(f"{gfg} is greater than 20")
////
# Python program to demonstrate 
# nested if with multiple if statements

i = -15; 
# condition 1
if i != 0:
    # condition 2
    if i > 0:
        print("Positive")
    # condition 3
    if i < 0:
        print("Negative")
///
i = 0; 

# if condition 1
if i != 0:
    # condition 1
    if i > 0:
        print("Positive")
        
    # condition 2
    if i < 0:
        print("Negative")
else:
    print("Zero")
    
/////
