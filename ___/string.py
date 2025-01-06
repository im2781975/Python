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
price = 478.23 
print(f"{f'${price : 0.2f}' :*>20s}")
"""            """
table = str.maketrans("aeiou", "12345")
ing = "This is a string"
print(ing.translate(table))
print('This syntax is very useful'.translate(str.maketrans('', '', "aeiou")))
"""            """
i, f, s, lst, dct = 10, 1.5, "foo", [" a", 1, 2], {'a' : 1, 2 : "foo"}
print("{} {} {} {} {}".format(i, f, s, lst, dct))
print(str.format("{} {} {} {} {}", i, f, s, lst, dct))
print("{0} {1} {2} {3} {4}".format(i, f, s, lst, dct))
print("{0:d} {1:0.1f} {2} {3!r} {4!r}".format(i, f, s, lst, dct))
print("{i:d} {f:0.1f} {s} {l!r} {d!r}".format(i = i, f = f, s = s, l = lst, d = dct))
print(f"{i} {f} {s} {lst} {dct}")
print(f"{i:d} {f:0.1f} {s} {lst!r} {dct!r}")
print("%(i)d %(f)0.1f %(s)s %(l)r %(d)r" % dict(i = i, f = f, s = s, l = lst, d= dct))
print("I am from {}. I love cupcakes from {}!".format("Australia", "Australia"))
print("I am from {0}. I love cupcakes from {0}!".format("Australia"))
print("{'a': 5, 'b': 6}")
print("{{'{}': {}, '{}': {}}}".format("a", 5, "b", 6))
print(f"{{'{'a'}': {5}, '{'b'}': {6}}} ")
"""				"""
import string
print(string.ascii_letters, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(string.ascii_lowercase, 'abcdefghijklmnopqrstuvwxyz')
print(string.ascii_uppercase,  'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(string.digits, '0123456789')
print(string.hexdigits, '0123456789abcdefABCDEF')
print(string.octdigits, '01234567')
print(string.punctuation, r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
print(string.whitespace, '\t\n\r\x0b\x0c')
print(string.printable,  '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c')
print(" a line with leading and trailing space ".strip(), 'a line with leading and trailing space')
print(">>> a Python prompt".strip('> '))
print("spacious string      ".rstrip(), '     spacious string')
print("     spacious string      ".rstrip(), 'spacious string      ')
print(reversed("Hello"))
print([char for char in reversed('hello')])
print(''.join(reversed('hello')))
print("This is a sentence.".split())
print(" This is    a sentence.  ".split())
print("            ".split())
print("This is a sentence.".split(' '))
print("Earth,Stars,Sun,Moon".split(','))
print(" This is    a sentence.  ".split(' '))
print("This is a sentence.".split('e'))
print("This is a sentence.".split('en'))
print("This is a sentence.".split('e', maxsplit = 0))
print("This is a sentence.".split('e', maxsplit = 1))
print("This is a sentence.".split('e', maxsplit = 2))
print("This is a sentence.".split('e', maxsplit =- 1))
print("This is a sentence.".rsplit('e', maxsplit = 1))
print("This is a sentence.".rsplit('e', maxsplit = 2))
print("Make sure to foo your sentence.".replace('foo', 'spam'))
print("It can foo multiple examples of foo if you want.".replace('foo', 'spam'))
print("""It can foo multiple examples of foo if you want,  ... or you can limit the foo with the third argument.""".replace('foo', 'spam', 1))
print("Hello World".isalpha())
print("Hello2World".isalpha())
print("HelloWorld!".isalpha())
print("HelloWorld".isalpha())
print("HeLLO WORLD".isupper())
print("HELLO WORLD".isupper())
print("".isupper())
print("Hello world".islower())
print("hello world".islower())
print("".islower())
print("hello world".istitle())
print("Hello world".istitle())
print("Hello World".istitle())
print("".istitle())
print("Hello2World".isalnum())
print("HelloWorld".isalnum())
print("2016".isalnum())
print("Hello World".isalnum())
print("\t\r\n".isspace())
print(" ".isspace())
print("".isspace())
print("foo" in "foo.baz.bar")
print("" in "test")
print(" ".join(["once","upon","a","time"]))
print("---".join(["once", "upon", "a", "time"]))
print("ß".lower(), "ß".upper().lower(), "ß".upper().lower())
"""            """
def reverse(ing):
    return ing[::-1]
print(reverse('Hello'))
ing = "Values are a: {a}, c: {c}, e: {e}"
print(ing.format(a = "1"*1, c = "3"*3, e = "5"*5))
"""            """
ing = ''
print(ing.isspace())
print(ing.isspace() or not ing)
print(not ing.strip())
"""            """
ing = "She sells seashells by the seashore."
start = 10
print(ing.count("sh"), ing.count("sea", start))
tr = ing[start:]
print(tr.count("sea"))
"""            """
lengths = {5: (1381, 2222), 19: (63, 102),    40: (2555, 4112), 93: (189,305),}
for road, length in lengths.items():    miles,kms = length
print('{} -> {} mi. ({} km.)'.format(str(road).rjust(4), str(miles).ljust(4), str(kms).ljust(4)))
"""            """
ing = "This is a test string"
print(ing.startswith("T"), ing.startswith("is", 2), ing.startswith(('This', 'That')))
print(ing.startswith(('ab', 'bc')), ing.endswith('.'), ing.endswith('!'), ing.endswith('stop.'))
print(ing.endswith('Stop.'), ing.endswith(('.', 'something')), ing.endswith(('ab', 'bc')))
"""            """
ing = b'\xc2\xa9 abc'
print(ing[0], type(ing))
u = ing.decode('utf-8')
print(u[0], type(u), u.encode('utf-8'))
print("£13.55".encode('ascii', errors = 'replace'))
print("£13.55".encode('ascii', errors = 'namereplace'))
print("£13.55".encode('ascii', errors = 'ignore'))
print("£13.55".encode('ascii', errors = 'xmlcharrefreplace'))
print("£13.55".encode('ascii', errors = 'backslashreplace'))
ing = "£13.55".encode('utf-8')
print(ing.decode('ascii', errors = 'replace'))
print(ing.decode('ascii', errors = 'ignore'))
print(ing.decode('ascii', errors = 'backslashreplace'))
print(type("f") == type(u"f"))
print(type(b"f"))
print("£13.55".encode('utf8'))
print("£13.55".encode('utf16'))
print(type(u"£13.55".encode('utf8')))
print(u"£13.55".encode('utf8'))
print(b'\xc2\xa313.55'.decode('utf8'))
"""            """
import re
pattern, ing = r"123", "123zzb"
re.match(pattern, ing)
match = re.match(pattern, ing)
print(match.group())

pattern, ing = r"\t123", "\t123zzb" 
print(re.match(pattern, ing).group())
print(re.match(pattern, "\t123zzb").group())  

pattern = r"\t123" 
print(re.match(pattern, ing).group())
match = re.match(r"(123)", "a123zzb")
print(match is None)
match = re.search(r"(123)", "a123zzb")
print(match.group())

pattern = r"(your base)"
sentence = "All your base are belong to us."
match = re.search(pattern, sentence)
print(match.group(1))
match = re.search(r"(belong.*)", sentence)
print(match.group(1))

match = re.search(r"^123", "123zzb")
print(match.group(0))
match = re.search(r"^123", "a123zzb")
print(match is None)
match = re.search(r"123$", "zzb123")
print(match.group(0))

print(re.search("b", "ABC") is None)
print(re.search("b", "ABC", flags=re.IGNORECASE).group())
print(re.search("a.b", "A\nBC", flags=re.IGNORECASE) is None)
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
print(m.group())
print(re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44"))
print(re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25"))
print(re.sub(r"t([0-9])([0-9])", r"t\g<2>\g<1>", "t13 t19 t81 t25"))
items = ["zero", "one", "two"]
print(re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1], something, a[2]"))
print(re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899"))
results = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")
print(results)
for result in results:     
    print(result.group(0), end = " ")
"""            """
def Isallowed(string):    
    characherRegex = re.compile(r'[^a-zA-Z0-9.]')    
    string = characherRegex.search(string)  
    return not bool(string)
print (Isallowed("abyzABYZ0099"))
print (Isallowed("#*@#$%^"))
print(re.split(r'\s+', 'James 94 Samantha 417 Scarlett 74'))
"""            """

import re
sentence, pattern = "This is a phone number 672-123-456-9910" , r".*(phone).*?([\d-]+)"
match = re.match(pattern, sentence)
print(match.group(), match.group(0), match.group(1), match.group(1, 2))
"""            """
match = re.search(r'My name is (?P<name>[A-Za-z ]+)', 'My name is John Smith')
print(match.group('name'), match.group(1))
print(re.match(r'(\d+)(\+(\d+))?', '11+22').groups())
print(re.match(r'(\d+)(?:\+(\d+))?', '11+22').groups())
match = re.search(r'[b]', 'a[b]c') 
print(match.group())
match = re.search(r'\[b\]', 'a[b]c') 
print(match.group())
re.escape('a[b]c')
match = re.search(re.escape('a[b]c'), 'a[b]c') 
print(match.group())
"""            """
username = 'A.C.'
print(re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!'))
print(re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!'))
"""            """
text = 'You can try to find an ant in this string' 
pattern = 'an?\\w' 
for match in re.finditer(pattern, text):
    sStart = match.start()
    sEnd = match.end()
    sGroup = match.group()
    print('Match "{}" found at: [{},{}]'.format(sGroup, sStart,sEnd))
