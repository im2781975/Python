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

ing = 'MollaVai'
upper = lambda string : string.upper()
print(upper(ing))
formatNumeric = lambda num : f"{num : e} " if isinstance(num, int) else f"{num :,.2f} "
print(formatNumeric(99999), formatNumeric(123.98))
data = [(1, 'apple'), (2, 'banana'), (3, 'orange')]
sortedData = sorted(data, key = lambda x : x[1])
print(sortedData)
"""				"""
foo, bar, baz = 1, 'bar', 3.1416
print('{}, {} & {}'.format(foo, bar, baz))
print('{0}, {1}, {2} & {1}'.format(foo, bar, baz))
print("X value {x}, Y value {y}".format(x = 2, y = 3))
"""            """
print('{:~<9s}, World'.format('Hello'))
print('{:~>9s}, World'.format('Hello'))
print('{:~^9s}'.format('Hello'))
print('{:0=6d}'.format(-123))
"""            """
foo = 'bar'
print(f'Foo is: {foo} ')
print(f'{foo : ^7s}')
"""            """
print('{0:.0f}'.format(42.12345))
print('{0:.1f}'.format(42.12345))
print('{0:.3f}'.format(42.12345))
print('{0:.5f}'.format(42.12345))
print('{0:.7f}'.format(42.12345))
print('{:.3f}'.format(42.12345))
print('{answer:.3f}'.format(answer=42.12345))
print('{0:.3e}'.format(42.12345))
print('{0:.0%}'.format(42.12345))
"""            """
ing = 'Hello'
a, b, c = 1.12345, 2.34567, 34.5678 
digits = 2
print('{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(ing, a, b, c, n = digits))
'{first} {last}'.format_map(data) 'Hodor Hodor!'
'{first} {last}'.format(first='Hodor', last='Hodor!')
"""            """
print('{:c}'.format(65))
print('{:d}'.format(0x0a))
print('{:n}'.format(0x0a))
print('{0:x}'.format(10))
print('{0:X}'.format(10))
print('{:o}'.format(10))
print('{:b}'.format(10))
print('{0:#b}, {0:#o}, {0:#x}'.format(42))
print('8 bit: {0:08b}; Three bytes: {0:06x}'.format(42))
"""            """
r, g, b = (1.0, 0.4, 0.0) 
print('#{:02X}{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))
print('{:.>10}'.format('foo'))
print('{:.>{}}'.format('foo', 10))
print('{:{}{}{}}'.format('foo', '*', '^', 15))
"""				"""
ing = "Aslam"
print("X£B".casefold(), ing.upper(), ing.lower(), ing.capitalize(), ing.title(), ing.swapcase())
print(str.upper('Here are'))
print(map(str.upper,["These","are","some","'strings'"]))
