#string is immutable like a[0] = 'R' cant assign
s = """He'l" l\'"""
a, b, c, d = 'Molla vai', 'Molla\'s vai', "Molla's vai", """ibrahim 
molla """
ing = '''House
For Rent'''
print(ing, ing[ : : -1], ing[3 : 12], ing[3 : -2])
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
print(5 * "Molla\'s \"Lecture\"\n")
upper = lambda string : string.upper(); print(upper('Molla'))
lower = lambda string : string.lower(); print(lower('Molla'))

ing = "\222\110\220"; print(ing)
ing = r"\222\110\220"; print(ing)
ing = "x\222\110\220"; print(ing)
ing = r"x\222\110\220"; print(ing)

ing = "{} {} {}".format('how', 'are', 'him'); print(ing)
ing = "{1} {0} {2}".format('how', 'are', 'him'); print(ing)
ing = "{l} {f} {g}".format(g = 'how', f ='are', l = 'him'); print(ing)
ing = "{0:b}".format(8); print(ing)
ing = "{0:b}".format(16); print(ing)
ing = "{0:e}". format(165.789); print(ing)
ing = "{0:0.2f}". format(1/6); print(ing)
ing ="{0:^16} was founded in {1:<4}!".format("OfSport", 2009); print(ing)
ing = "|{:<10}|{:^10}|{:>10}|".format('Here', 'You', 'Are'); print(ing)
print('{:~<9s}, world'.format('Hello'))
print('{:~>9s}, world'.format('Hello'))
print('{:~^9s}, world'.format('Hello'))
print('{:0=6d}'.format(-1234))

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

name = input("whats your name:")
cog = "molla"
print(name + ' ' + cog, len(name))

ing = "molla vai"
lst = list(ing); print(lst)
lst[1] = 'p'; print(lst)
tis = ''.join(lst); print(tis)
print(ing[0 : 2] + ' ' + tis[: : -1])

data = [(1, 'apple'), (3, 'banana'), (2,  'orange')]
info = sorted(data, key = lambda x : x[0]); print(info)

a, b, c = 1, 'hero', 3.95
print('{}, {} & {}'.format(a, b, c))
print('{0}, {1}, {2} & {1}'.format(a, b, c))
print("x = {x}\ny = {y}".format(x = 2, y = 5))
print(f"b is: {b : ^7s}")

dig = 12.345; print("digit's: %3.2f" %dig)
ric = lambda num : f"{num :e}" if isinstance(num, int) else f"{num : ,.2f}"
print(ric(9999), '\n', ric(2.87))

