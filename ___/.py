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
ing, b = u'Café', 'Lorem ipsum'; print(isinstance(ing, str))
ing = b'Cafe'         
ing = 'Café'.encode(); print(isinstance(ing, str))
ing = b"abc"
print(ing[0] == 97, ing[0 : 1] == b"a", ing[1] == 98, ing[1 : 2] == b"b")
print(u"Hello, Here i am"[::-1])
print("Hello, Here i am"[::-1])
print("A", "B", "C", sep = "")
print("A", "B", "C", sep = ",")
print("A", "B", end = ".\n")
print("Flush this", flush = True)
ing = "Aslam"
print("X£B".casefold(), ing.upper(), ing.lower(), ing.capitalize())
print(ing.title(), ing.swapcase(), str.upper('Here i am'))
print(map(str.upper,["There", "are", " some", "string"]))
table = str.maketrans("aeiou", "12345")
ing = "This is a string"
print(ing.translate(table))
print('This is very useful'.translate(str.maketrans('', '', 'aeiou')))
print(5 * "Molla\'s \"Lecture\"\n")
upper = lambda string : string.upper(); print(upper('Molla'))
lower = lambda string : string.lower(); print(lower('Molla'))
ing = "Hello world!"
print([ing for ing in 'aeiou'], ing)
print(str[i] for i in [1, 2, 3, 4, 5])
ing = ""
for i in range(1, 22):
    ing += str(i)
    ing += ","
print(ing)
ing = bytearray(b'stack'); print(id(ing))
ing += b'overflow'
print(id(ing), bytearray(b'StackOverflow'))
rin = ing; rin += b'rock'
print(bytearray(b'StackOverflow rocks!'))
print(id(rin) == id(ing))

ing = 'thisisashorttext' 
print(ing.count('t'), ing.count('th'), ing.count('is'), ing.count('text'))
from collections import Counter
print(Counter(ing))
print(sorted( [" foo ", " bAR", "BaZ "], key = lambda s: s.strip().upper())) 
print(sorted( [" foo ", " bAR", "BaZ "], key = lambda s: s.strip()))
print(sorted(map(lambda s: s.strip().upper(), [" foo ", " bAR", "BaZ "])))
print(sorted(map(lambda s: s.strip(), [" foo", "bAR", "BaZ"])))
ing = "GFG"
ch = iter(ing)
print(next(ch), next(ch), next(ch))

import string
print(string.ascii_letters, "\n", string.ascii_lowercase, "\n", string.ascii_uppercase)
print(string.digits, string.hexdigits, string.octdigits)
#whitespace -> '\t\n\r\x0b\x0c'
print(string.punctuation,"\n", string.whitespace,"\n", string.printable)
print(" trailing space ".strip(), 'trailing space')
print("spacious string    ".rstrip("    "),'    spacious string')
print("    spacious string    ".rstrip(),'spaciuos string    ')
print(">> python prompt".strip('> '))
print("    This is a     word    ".split("    "))
print("    This is a     word    ".split())
print("        ".split())
print("Earth, Stars, Sun, Moon".split(', '))
ing = "This is a sentence"
print(ing.split('e'), "\n", ing.split('en'))
print(ing.split('e', maxsplit = 0), "\n", ing.split('e', maxsplit = 1))
print(ing.split('e', maxsplit = 2), "\n", ing.split('e', maxsplit = -1))
print(ing.split('e', maxsplit = 1), "\n", ing.split('e', maxsplit = 2))
print(ing.replace('is', 'x'))
print("""It can foo multiple if you want,  ... or you can limit the foo .""".replace('foo', 'spam', 1))
#Hello World, HelloWorld!, HELLO WORLD, hello world, Hello world
ing = "Hello2World!"
print(ing.isalpha(), ing.isupper(), ing.islower(), ing.istitle(), ing.isalnum(), "2016".isalnum())
print("".isupper(), "".islower(), "".istitle(), " ".isspace(), "\t\r\n".isspace())
print("foo" in "foo.baz.bar", "\n", "" in "test")
x = ["once", "upon", "a", "time"]
print(" ".join(x), "\n", "-".join(x))
print("£".lower(), "£".upper().lower())
ing = "This is a test string"
print(ing.startswith("T"), ing.startswith("is", 2), ing.startswith(('This', 'That')))
print(ing.startswith(('ab', 'bc')), ing.endswith('.'), ing.endswith('!'), ing.endswith('stop.'))
print(ing.endswith('Stop.'), ing.endswith(('.', 'something')), ing.endswith(('ab', 'bc')))

ing = "\222\110\220"; print(ing)
ing = r"\222\110\220"; print(ing)
ing = "x\222\110\220"; print(ing)
ing = r"x\222\110\220"; print(ing)

ing = "{} {} {}".format('how', 'are', 'him'); print(ing)
ing = "{1} {0} {2}".format('how', 'are', 'him'); print(ing)
ing = "{l} {f} {g}".format(g = 'how', f ='are', l = 'him'); print(ing)
ing = "|{:<10}|{:^10}|{:>10}|".format('Here', 'You', 'Are'); print(ing)
print('{:~<9s}, world'.format('Hello'))
print('{:~>9s}, world'.format('Hello'))
print('{:~^9s}, world'.format('Hello'))
print('{:.>10}'.format('foo'))
print('{:.>{}}'.format('foo', 10))
print('{:{}{}{}}'.format('foo', '*', '^', 15))
print('{:0=6d}'.format(-1234))

ing = "HELLO"
rev = reversed(ing); print(rev)
rev = "".join(reversed(ing)); print(rev)
print("HELLO"[::-1])
print([char for char in reversed("HELLO")])
print(''.join(reversed("HELLO")))

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
x = 42.12345678
print('{0:.0f}'.format(x), '{0:.1f}'.format(x))
print('{0:.3f}'.format(x), '{0:.5f}'.format(x))
print('{0:.7f}'.format(x), '{:.3f}'.format(x))
print('{0:.3e}'.format(x), '{0:.0%}'.format(x))
print('{res:.3f}'.format(res = x))
print('{:c}'.format(65), '{:d}'.format(0x0a))
print('{:n}'.format(0x0a), '{0:x}'.format(10))
print('{0:X}'.format(10), '{:o}'.format(10))
print('{:b}'.format(10))
print('{0:#b}, {0:#o}, {0:#x}'.format(42))
print('8 bit: {0:08b}, Three bytes: {0:06x}'.format(42))
ing = "{0:b}".format(8); print(ing)
ing = "{0:b}".format(16); print(ing)
ing = "{0:e}". format(165.789); print(ing)
ing = "{0:0.2f}". format(1/6); print(ing)
ing ="{0:^16} was founded in {1:<4}!".format("OfSport", 2009); print(ing)

r, g, b = 1.0, 0.4, 0.0
print('#{:02X} {:02X} {:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))

ing = 'Hello'
a, b, c, d= 1.12345, 2.34567, 34.5678, 478.23
dig = 2
print('{0}!, {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(ing, a, b, c, n = dig))
print(f"{f'${d : 0.2f}':*>20s}")
data = {"first" : "info", "last" : "nation"}
print('{first} {last}'.format_map(data))
print('{first} {last}'.format(first = "nation", last = " info"))

i, f, s, lst, dct = 10, 1.5, "foo", [" a", 1, 2], {'a' : 1, 2 : "foo"}
print('{} {} {} {} {}'.format(i, f, s, lst, dct))
print('{0} {1} {2} {3} {4}'.format(i, f, s, lst, dct))
print(str.format("{} {} {} {} {}", i, f, s, lst, dct))
print('{0:d} {1:0.2f} {2} {3!r} {4!r}'.format(i, f, s, lst, dct))
print('{i:d} {f:0.1f} {s} {l!r} {d!r}'.format(i = i, f = f, s = s, l = lst, d = dct))
print(f"{i} {f} {s} {lst} {dct}")
print(f"{i:d} {f:0.1f} {s} {lst!r} {dct!r}")
print("%(i)d %(f)0.1f %(s)s %(l)r %(d)r".format(i = i, f = f, s = s, l = lst, d = dct))
print("from {}.love cake from {}".format("BD", "BD"))
print("from {0}.love cake from {0}".format("BD"))
print("{'a' : 5, 'b' : 6}")
print("{{'{}' : {}, '{}' : {}}}".format("a", 5, "b", 7))
print(f"{{'{'a'}': {5}, '{'b'}': {6}}} ")

def reverse(ing):
    return ing[::-1]
print(reverse("HELLO"))
ing = "a : {a}, b : {b}, c : {c}"
print(ing.format(a = "1" * 1, b = "3" * 3, c = "5" * 5))
ing = ''
print(ing.isspace(), ing.isspace() or not ing, not ing.strip())

ing = "She sells seashells by the seashore"
start = 10
tr = ing[start:]
print(ing.count("sh"), ing.count("sea", start), tr.count("sea"))
length = {5 : (1381, 2222), 19 : (63, 102),    40 : (2555, 4112),}
for road, leng in length.items():
    miles, kms = leng
    print('{} -> {} mi.({} km)'.format(str(road).rjust(3), str(miles).ljust(5), str(kms).ljust(5)))
import re
a, b, c, d = r"\t123", "\t123zzb",r"123", "123zzb",
x = re.match(c, d); print(x.group(), x)
print(re.match(a, b).group())
x = re.match(r"(123)", "a123zzb"); print(x is  None)
x = re.search(r"(123)", "a123zzb"); print(x.group())

a, b, c, d = r"(your base)", "All your base are belong", r"^123", "123zzb"
x = re.search(a, b); print(x.group(1))
x = re.search(r"(belong.*)", b); print(x.group(1))
x = re.search(c, d); print(x.group(0), x is None)
print(re.search(r"123$", "zzb123").group(0))
print(re.search("b", "ABC") is None)
print(re.search("b", "ABC", flags = re.IGNORECASE).group())
print(re.search("a.b", "A\nBC", flags = re.IGNORECASE)is None)
x = re.search("a.b", "A\nBC", flags = re.IGNORECASE | re.DOTALL); print(x, x.group())
print(re.sub(r"t[0 - 9][0 - 9]", "foo", " name t13 age t44 year t99 age t44"))
print(re.sub(r"t([0 - 9])([0 - 9])", r"t\2\1", "t13 t19 t81 t25"))
print(re.sub(r"t([0-9])([0-9])", r"t\g<2>\g<1>", "t13 t19 t81 t25"))
items = ["zero", "one", " two"]
print(re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1], something, a[2]"))
print(re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899"))
res = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")
print(res)
for result in res:     
    print(result.group(0), end = " ")
import re
a, b = "This is a phone number 672-123-456-9910" , r".*(phone).*?([\d-]+)"
x = re.match(b, a);
print(x.group(),'\n', x.group(0),'\n',x.group(1),'\n',x.group(1, 2))
x = re.search(r'My name is (?P<name>[A-Za-z ]+)', 'My name is John Smith')
print(x.group('name'), x.group(1))
print(re.match(r'(\d+)(\+(\d+))?', '11+22').groups())
print(re.match(r'(\d+)(?:\+(\d+))?', '11+22').groups())
print(re.search(r'[b]', 'a[b]c').group())
print(re.search(r'\[b\]', 'a[b]c').group())
print(re.search(re.escape('a[b]c'), 'a[b]c').group())

username = 'A.C.'
print(re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!'))
print(re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!'))
text, pattern = 'You can try to find an ant in this string', 'an?\\w' 
for x in re.finditer(pattern, text):
    print('Match "{}" found at: [{},{}]'.format(x.group(), x.start(), x.end()))
