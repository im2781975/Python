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

string = '''House
For
Rent '''
string = '''molla\'s "House" '''
print(string[ : : -1], string[3 : 12], string[3 : -2])
ing = "mollavai"
ing = "".join(reversed(ing))
print(ing)
"""                    """
lst = list(ing)
lst[1] = 'p'
tis = ''.join(lst)
print(tis)
"""                    """
string = ing[0 : 2] + ' ' + tis[::-1]
ing = "python\twork"
ing = "\110\220\221\223"
ing = r"\110\220\221\223"#Escape seq
ing = "there has x\23x\25"
ing = r"there has x\23x\25"
print(ing)
ing = "{} {} {}".format('Geeks', 'For', 'Life')
ing = "{1} {0} {2}".format('Hasan', 'Alom', 'mahmud')
ing = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
ing = "{0:b}".format(8)
ing = "{0:b}".format(16)
ing = "{0:e}".format(165.789)
ing = "{0:0.2f}". format(1/6)
ing = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
ing ="{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(ing)

integer = 12.3456789
print('The value of Integer is %3.2f' %integer)
print('The value of Integer is %3.4f' % integer)
