#string is immutable like a[0] = 'R' cant assign
s = """He'l" l\'"""
a, b, c, d = 'Molla vai', 'Molla\'s vai', "Molla's vai", """ibrahim 
molla """
print(a, b, c, d)
print(a.upper(), a.lower(), a.capitalize())
print(a,'\n',f"a[3]: {a[3]}\na[2 : 6]: {a[2:6]}\na[1 : 8]: {a[1 : 8]}")
print(f"a[8 : 0 : -1]: {a[8 : 0 : -1]}\na[-1 : -8: -1]: {a[-1 : -12 : -1]}")
for char in a:
    print(char, end = ' ')
if 'molla' in a: print("Exits")
else: print("Not exits")
#repr() : single quote (') in the string is escaped as \'.
print(s + "\n" + repr(s) + "\n" + str(s))
print(eval(repr(s)) + "\n" + eval(repr(s)) == s)

ing = "HELLO"
rev = reversed(ing); print(rev)
rev = "".join(reversed(ing)); print(rev)
print("HELLO"[::-1])

first = input("Enter: "); sec = input("Enter: ")
tmp = first; first = sec; sec = tmp; #swap
print("swap: ", first, sec);
a, b = "molla", "vai"
print("concatenation of str is:", first + sec, ",", a + b)
text = a + b #loop
for char in text:
    print(char, end = ' ')
