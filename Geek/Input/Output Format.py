# Python program showing how to use string modulo operator(%)

print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 

print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value

print("%7.3o" % (25))   # print octal value

print("%10.3E" % (356.08977))   # print exponential value
#----
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and referring a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

# using format() method and referring a position of the object
print(f"{'Geeks'} and {'Portal'}")
#----
# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks'))

# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))

print("Geeks: {a:5d},  Portal: {p:8.2f}".
     format(a = 453, p = 59.058))

#----
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))

data = dict(fun ="GeeksForGeeks", adj ="Portal")

print("I love {fun} computer {adj}".format(**data))

#----
cstr = "I love geeksforgeeks"

# Printing the center aligned string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))
#----
name = "Alice"
age = 30
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)
# Output: Name: Alice, Age: 30
#----
name = "Alice"
age = 30
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)
# Output: Name: Alice, Age: 30
#----
name = "Alice"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)
# Output: Name: Alice, Age: 30
#----
value = 3.14159
formatted_value = f"{value:.2f}"
print(formatted_value)
# Output: 3.14
#---*
value = 3.14159
formatted_value = "{:.2f}".format(value)
print(formatted_value)
# Output: 3.14
#----
name = "Alice"
formatted_string = "Hello, %s!" % name
print(formatted_string)
# Output: Hello, Alice!
#----

