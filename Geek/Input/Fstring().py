# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")


name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")
#-----
# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
#----
print(f"'GeeksforGeeks'")

print(f"""Geeks"for"Geeks""")

print(f'''Geeks'for'Geeks''')
#-----
english = 78
maths = 56
hindi = 85

print(f"Ram got total marks {english + maths + hindi} out of 300")
#-----
newline = ord('\n')

print(f"newline: {newline}")
#----
# Printing single braces
print(f"{{Hello, Geek}}")

# Printing double braces
#Dict
print(f"{{{{Hello, Geek}}}}")
#----
Geek = { 'Id': 100,
         'Name': 'Om'}

print(f"Id of {Geek['Name']} is {Geek['Id']}")

#-----
name = "Alice"
age = 30
sentence = f"My name is {name} and I am {age} years old."
print(sentence)
Output:
My name is Alice and I am 30 years old.
#----
num = 3.14159
formatted = f"{num:.2f}"
print(formatted)  # Output: 3.14
#----
name = "Alice"
age = 30
json_data = f'{{ "name": "{name}", "age": {age} }}'
print(json_data)
Output:
{ "name": "Alice", "age": 30 }
#----
name = input("Enter your name: ")
message = f"Hello, {name}!"
print(message)
#----
name = "Alice"
age = 30
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)
Output:
My name is Alice and I am 30 years old.
