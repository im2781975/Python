# Python code to illustrate
# working of try() 
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
 
# Look at parameters and note the working of Program
divide(3, 2)
////
# Python code to illustrate
# working of try() 
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
 
# Look at parameters and note the working of Program
divide(3, 0)
////
# code
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)
 
         
divide(3, "GFG") 
divide(3,0) 
////
# Program to depict else clause with try-except
  
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
/////
# Python program to demonstrate finally 
    
# No exception Exception raised in try block 
try: 
    k = 5//0 # raises divide by zero exception. 
    print(k) 
    
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
        
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')
