def cubo(x): 
   r=x**3 
   return r
////
# Python program to 
# demonstrate return statement 

def add(a, b):

    # returning sum of a and b
    return a + b

def is_true(a):

    # returning boolean of a
    return bool(a)

# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))

res = is_true(2<5)
print("\nResult of is_true function is {}".format(res))
////
# A Python program to return multiple  
# values from a method using class 
class Test: 
    def __init__(self): 
        self.str = "geeksforgeeks"
        self.x = 20   
  
# This function returns an object of Test 
def fun(): 
    return Test() 
      
# Driver code to test above method 
t = fun()  
print(t.str) 
print(t.x)
////
# A Python program to return multiple  
# values from a method using tuple 
  
# This function returns a tuple 
def fun(): 
    str = "geeksforgeeks"
    x = 20
    return str, x;  # Return tuple, we could also 
                    # write (str, x) 
  
# Driver code to test above method 
str, x = fun() # Assign returned tuple 
print(str) 
print(x) 
///
# A Python program to return multiple  
# values from a method using list 
  
# This function returns a list 
def fun(): 
    str = "geeksforgeeks"
    x = 20   
    return [str, x];   
  
# Driver code to test above method 
list = fun()  
print(list) 
////
# A Python program to return multiple  
# values from a method using dictionary 
  
# This function returns a dictionary 
def fun(): 
    d = dict();  
    d['str'] = "GeeksforGeeks"
    d['x']   = 20
    return d 
  
# Driver code to test above method 
d = fun()  
print(d) 
////
# Python program to illustrate functions 
# can return another function 

def create_adder(x): 
    def adder(y): 
        return x + y 

    return adder 

add_15 = create_adder(15) 

print("The result is", add_15(10)) 

# Returning different function
def outer(x):
    return x * 10

def my_func():
    
    # returning different function
    return outer

# storing the function in res
res = my_func()

print("\nThe result is:", res(10))
///
print(type(10))        # Output: <class 'int'>
print(type(3.14))      # Output: <class 'float'>
print(type("hello"))   # Output: <class 'str'>
print(type([1, 2, 3])) # Output: <class 'list'>

# Creating a new class
MyClass = type('MyClass', (object,), {'attr': 5})
print(type(MyClass))   # Output: <class 'type'>
////
def add(a, b):
    return a + b  # The function returns the result of a + b

result = add(5, 3)
print(result)  # Output: 8
////
def multiply(x, y):
    return x * y  # Returns the product of x and y

result = multiply(4, 5)
print(result)  # Output: 20
/////
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"  # This return statement is reached only if num is 0

print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
