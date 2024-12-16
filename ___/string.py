s = """w'o"w"""
#repr() : single quote (') in the string is escaped as \'.
print(repr(s), str(s))
print(eval(repr(s)))
print(eval(repr(s)) == s)

ing = "Hello"
rev = reversed("Hello")
print(rev)

#concatenate string
first = input("Enter first:")
sec = input("Enter second: ")
print(first + sec)

text = "ibrahim"
for char in text:
    print(char)

name = input("whats your name: ")
length = len(name)
cog = "Molla"
print(name + ' ' + cog, length)
print("name[3]:", name[3])
print(5 * "Molla\'s \"Lecture\"\n")
#swap
a = input("Enter a: ")
b = input("Enter b: ")
tmp = a 
a = b 
b = tmp
print(a, b)
