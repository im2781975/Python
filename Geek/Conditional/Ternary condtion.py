# Python program to demonstrate nested ternary operator
a = 10
b = 20

print("Both are equal" if a == b else "a is greater"
      if a > b else "b is greater")
////
# Python program to demonstrate nested ternary operator
a = 10
b = 20

print("Both are equal" if a == b else "a is greater"
      if a > b else "b is greater")
////
# Program to demonstrate ternary operator
a = 10
b = 20

# python ternary operator usinf tuple
print(("b is minimum", "a is minimum") [a < b])
////
# Python program to demonstrate ternary operator
a, b = 10, 20

print({True: "a is minimum", False: "b is minimum"} [a < b])
////
# Python program to demonstrate ternary operator
a = 10
b = 20

print((lambda: "b is minimum", lambda: "a is minimum")[a < b]())
////
a = 10
b = 20

# ternary operator with print statement
print(a,"is minimum") if (a < b) else print(b,"is minimum")
////
a = 5
b = 10
max_value = a if a > b else b  # max_value will be 10
////
a = 5
b = 10
my_dict = {'max': a if a > b else b}  # my_dict will be {'max': 10}
/////
# Example
result = "Positive" if num > 0 else "Negative"
# Read as: "If num is greater than 0, then result is 'Positive', otherwise result is 'Negative'."
/////
# Instead of this:
if a > b:
    max_value = a
else:
    max_value = b

# Use this:
max_value = a if a > b else b
////

