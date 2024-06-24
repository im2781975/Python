# valid variable name 
geeks = 1
Geeks = 2
Ge_e_ks = 5
_geeks = 6
geeks_ = 7
_GEEKS_ = 8
  
print(geeks, Geeks, Ge_e_ks) 
print(_geeks, geeks_, _GEEKS_)

# declaring the var 
Number = 100
  
# display 
print("Before declare: ", Number) 
  
# re-declare the var 
Number = 120.3
    
print("After re-declare:", Number)
////#assign value
a = b = c = 10
  
print(a) 
print(b) 
print(c) 
#assign diffrence
a, b, c = 1, 20.2, "GeeksforGeeks"
  
print(a) 
print(b) 
print(c) 
# different case
a = 10
a = "GeeksforGeeks"
  
print(a) 
# + operatir
a = 10
b = 20
print(a+b) 
  
a = "Geeksfor"
b = "Geeks"
print(a+b) 

#global python
# This function uses global variable s 
def f(): 
    s = "Welcome geeks"
    print(s) 
  
  
f()
#global 
# This function has a variable with 
# name same as s 
def f(): 
    print(s) 
  
# Global scope 
s = "I love Geeksforgeeks"
f() 
# global keyword
x = 15
  
def change(): 
  
    # using a global keyword 
    global x 
  
    # increment value of a by 5 
    x = x + 5
    print("Value of x inside a function :", x) 
  
  
change() 
print("Value of x outside a function :", x) 
# var type
# numberic 
var = 123
print("Numeric data : ", var) 
  
# Sequence Type 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 
  
# Boolean 
print(type(True)) 
print(type(False)) 
  
# Creating a Set with 
# the use of a String 
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 
  
# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

#class object
class CSStudent: 
    # Class Variable 
    stream = 'cse'
    # The init method or constructor 
    def __init__(self, roll): 
        # Instance Variable 
        self.roll = roll 
  
# Objects of CSStudent class 
a = CSStudent(101) 
b = CSStudent(102) 
  
print(a.stream)  # prints "cse" 
print(b.stream)  # prints "cse" 
print(a.roll)    # prints 101 
  
# Class variables can be accessed using class 
# name also 
print(CSStudent.stream)  # prints "cse" 

#
