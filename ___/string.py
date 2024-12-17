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
a, b = "molla", "vai"
print("concatenate a & b: ",a + b)

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

#string is immutable like a[0] = 'R' cant assign
a, b, c, d, e = 'ibrahimmolla', 'Molla vai', 'Molla\'s vai', "Molla's vai", """ibrahim
molla """
print(a, b, c, d)
print(e)
print(a)
print(f"a[3]: {a[3]}\na[2 : 6]: {a[2 : 6]}\na[0 : 12]: {a[0 : 12]}\na[12 : 0 : -1]: {a[12 : 0 : -1]}\na[-1 : -12 : -1]: {a[-1 : -12 : -1]} ")
print(a.upper(), a.lower(), a.capitalize())

for char in b: print(char)
if 'molla' in b: print("Exits")
else: print("Not Exits")
