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
