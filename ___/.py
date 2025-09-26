s = """He'l" l\'"""
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
 
