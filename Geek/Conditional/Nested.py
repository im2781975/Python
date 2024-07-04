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

