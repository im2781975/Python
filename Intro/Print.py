print("print\n('here i am')")
print("hi",input("what is your name:") + "," + "How are you?")

name = input("whats your name:")
length = len(name)
b = "molla"
print(name, length)
print(name + ' ' + b)
print("name[3]:", name[3])
print(5* "\njenny\'s \"Lectures\"")
#swap
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
tmp = a
a = b
b = tmp
print("Value of a is:", a)
print("Value of b is:", b)
#calculate bmi
weight = input("Entet weight: ")
height = input("Enter height: ")
bmi = int(weight)/float(height)**2
print(round(bmi, 2))
