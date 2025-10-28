"""            ARRAY            """
import array as arr
#from array import array
x = arr.array('d', [2.1, 3.4, 5.9, 7.8])
for i in range(4):    print(x[i], end = " ")
print("\r")
x = arr.array('i', [5, 9, 4, 7])
for i in range(0, 4):    print(x[i], end = " ")
x.insert(1, 9); x.append(10);print(x.pop(1))
for i in x:    print(x.pop(), end = " ")
if 2 in x:    x.remove(2)
for i in x:    print(x.pop(), end = " ")
print("\r")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = arr.array('i', x)
for i in l:    print(i, end = " ")
print(x[3 : 8], x[:], x.index(5), x.index(7))

x = arr.array('i', [9, 8, 7, 6, 5, 4])
x[2] = 2; x[4] = 6; x.extend([12, 13, 14]); x.reverse()
print(x.count(6), *x, x.tolist())
x.remove(4) #del first occurance
for i in x:    print(i, end = " ")
print("\r")
y = arr.array('i', [7, 8, 9]); x.extend(y)
c = [11, 12, 13]; x.fromlist(c)
print(x.buffer_info, x[0], x.index(9))
"""				STRING				"""
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
ing = "I Love Myself"
print(ing.center(40, " "))
print(ing.ljust(40, " "))
print(ing.rjust(40, " "))
print('G','F','G', sep = '')
print('09','12','2016', sep = '-') 
print('G','F', sep = '', end = '') 
print('09','12','2016', sep = '-', end = '\n') 
print('prtk','agarwal', sep = '', end = '@') 
print('apples', 'oranges', 'bananas', sep = ', ')
print('one', 'two', 'three', sep = ';') 
print('????', '????', '????', sep = '????')
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
print("Geeks : %2d, Portal : %5.2f" %(1, 05.333))
print("Total students : %3d, Boys : %2d" % (240, 120))   
print("%7.3o" % (25), "%10.3E" % (356.08977))
print('is {0}, {1}, and {other}.' .format('Molla', 'For', other = 'Now'))
print("Molla : {0:2d}, For : {1:8.2f}".format(12, 00.546))
print("Molla : {1:3d}, For : {0:7.2f}".format(47.42, 11))
print("Molla : {a:5d}, For : {b:8.2f}".format(a = 453, b = 59.058))
tab = {'Molla': 4127, 'for': 4098, 'Now': 8637678}
print('Molla: {0[Molla]:d}; For: {0[for]:d}; ' 'Now: {0[Now]:d}'.format(tab))
data = dict(fun = "Here I", go = " am")
print("{fun} {go}".format(**data))
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
num = 3.14167; print(f"{num :.2f} ")
name, age = "Aslam", 22; print("name {} age {}".format(name, age))
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
a, b, c, d = 1.12345, 2.34567, 34.5678, 478.23
dig = 2
print('{0}!, {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(ing, a, b, c, n = dig))
print(f"{f'${d : 0.2f}':*>20s}")
data = {"first" : "info", "last" : "nation"}
print('{first} {last}'.format_map(data))
print('{first} {last}'.format(first = "nation", last = " info"))
name, age = "Alice", 30
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")
print("Name: %s, Age: %d" % (name, age))
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
val = 3.14159; print(f"{val:.2f}" ,"{:.2f}".format(val))
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

ing = b'\xc2\xa9 abc'; print(ing[0], type(ing))
u = ing.decode('utf-8'); print(u[0], type(u), u.encode('utf-8'))
a, b, c, d, e = 'replace', 'namereplace', 'ignore','xmlcharrefreplace','backslashreplace'
print("£13.55".encode('ascii', errors = a))
ing = "£13.55".encode('utf-8')
a, b, c = 'replace', 'ignore','backslashreplace'
print(ing.decode('ascii', errors = a))
print(type("f") == type(u"f"), type(b"f"))
print("£13.55".encode('utf8'), "£13.55".encode('utf16'))
print(type(u"£13.55".encode('utf8')))
print(u"£13.55".encode('utf8'), b'\xc2\xa313.55'.decode('utf8'))

def Isallowed(string):    
    ch = re.compile(r'[^a-zA-Z0-9.]')    
    string = ch.search(string)  
    return not bool(string)
print (Isallowed("abyzABYZ0099"))
print (Isallowed("#*@#$%^"))
print(re.split(r'\s+', 'James 94 Samantha 417 Scarlett 74'))

"""                SET                """
x = {10, 56, 89, 90, True, 'Molla', 1}
#1 & True return same value
#if not present discard will return no error
x.add(99); x.remove(56); x.discard(10)
if 56 in x:    x.remove(56)
print(x)
for i in range(1, 6):    x.add(i)
for i in range(1, 5):    x.remove(i)
print(x, len(x), x.pop())
x.add((13, 14, 15)); print(x)
#x.add([16, 17, 18]) not work for immutable
x.clear(); y = {}; y.clear(); z = set()
print(type(x), type(y), type(z))
print(2 in {1, 2, 3}, 4 not in {1, 2, 3})
x, y, z = {1, 2, 3, 4}, {3, 4, 5, 6}, set()
print(type(x), type(y), type(z))
comb = {}
comb = {(i, j)for i in x for j in y}; print(comb)
print(f"union is: {x.union(y)}")
print(y.union(x), x | y, x.union((10, 11)))
x |= y
print(x, x.update(y), x.update([29, 30]), "\n", x)
print(x.intersection(y, z), x.intersection([19, 20]), x.intersection(y))
print(x & y, x & y & z)
x &= y
x &= y; x.intersection_update(y); print(x)
print(x.difference(y, z), x.difference((10, 11)), x - y)
x -= y; x.difference_update(y); print(x)
x.symmetric_difference(y); print(x, x ^ y)
#method take maximum one agr
print((x | y) - (x & y), (x ^ y ^ z))
y.symmetric_difference_update(x); print(y)
y.symmetric_difference_update((11, 15)); print(y)

x, y = {1, 2, 3, 4, 5}, {4, 10, 7, 8, -10}
print(x.isdisjoint(y), x.isdisjoint((['ab', 'bc'])))
print(len(x), len(y), len(x & y) == 0, (x & y) == set())
#method
print(x.issubset(y), x <= y, x.issuperset(y), x >= y)
#del y, it will remove whole set
y.clear(); print(x, y)

x = set(); print(x)
x = set("Molla vai"); print(x)
ing = "Here I am"; x = set(ing); print(x)
x = set(["Mah", "Abd"]); print(x)
print("Abd" in x)
x = ("Abd", "Mah"); print(set(x))
dic = {"ab" : 1, "bc" : 2, "cd" : 3}; print(set(dic))
x = set([1, 2, 4, 4, 3, 3, 3, 6, 5]); print(x)
x = set([1, 2, 'wx', 4, 'xy', 6, 'yz']); print(x)
x = {1, 2, 3}; print(x)
x = set([4, 5, (6, 7)]); x.update([10, 11]); print(x)

#set is muteable(mean can add or remove) but frozen is immuteable.set print unique elements
ing = ('M', 'o', 'l', 'l', 'a'); print(frozenset(ing), frozenset())
lst = [1, 2, 3, 3, 4, 5, 5, 6, 2]; print(set(lst))
x = {'A', 'B', 'C', 'D', 'B'}
y = set('abcde'); y.add('xyz'); print(y, x)
print(frozenset("Mollavai"))
x, y = set("mollavai"), set([1, 2, "am", "ironman", 6, 9])
print(x, y)
for i in y:    print(i, end = " ")
x = {1, 2, 3, 4, 5}; tmp = iter(x)
print(tmp, next(tmp), next(tmp), next(tmp))
for i in x:    print(i, end = " ")
a = list(x); b = [i * 2 for i in x if i > 2]; print(a, b)

x = [1, 2, 3, 1, 4, 5]; print(set(x), list(set(x)))
num = set(x); num.add(10)
if 5 in num:    num.remove(5)
for i, item in enumerate(num):    print(i, item)
    
"""            TUPLE            """
tup = (123, "Molla", " Ibra"); print(tup, tup[0])
for i in range(len(tup)):    print(tup[i], end = "\t")
def multi():    return 3, 4
print("\n", multi())
x = 'A', 'B', 'C', 'D', 'E', 'F'
print(type(x), x[0], x[-1], x[:: -1], x[5: 2: -1])
for item in x:    print(item, end = "\t")
print(item, len(item))
x = "red", " green", "blue"
print(x[::-1], tuple(reversed(x)))
#tuple is immuteable but it can hold muteable object like list
x = ([1, 2, 3], [4, 5, 6]); x[0][1] = 66
for i in range(len(x)):    print(x[i], end = " ")
#tuple are zero idx
a, b, c = (1, 7, -4, "jenny", True, 9, -5), (10, 12, 14, 16), (11,); print(a, b, c)
print(a[1], a[-2], a[5], a[-1], a[:-1], a[-1:], len(a), a[1 : 3], a[: 5])
for item in b:    print(item, end = "\t")
x = (a, b, c); print("\n", len(x), x[0], x)
x = a + b + c; print(len(x), x[0], x)
#should be same type not mixed
print(max(b), min(b), b.count(12), b.index(12))
obj = iter(b)
for item in b:    print(item, end = " ")
for item in obj:    print(item, end = " ")

print((10, ) * 6, ("MOLLA ") * 2)
x = [1, 2, 3, 4, 5, 6]; print(tuple(x))
x, y = (5, "molla", 7, " vai"), (9, 1)
print(x[0], x + y)
x = ('bear', 'weasel', 'bear', 'frog')
print(x.count('bear'), x.count('fox'))
obj = iter(x)
for index, item in enumerate(obj):
    print(item, end = " ")
    if index == 2:    break
print(next(obj), next(obj))
tup = ("molla", "vai", "aslam")
print(tup[:1], tup[: :-1])
a, b, c = tup; print(a, b, c)
x = ("MOLLA"); n = 2
for i in range(int(n)):
    x = (x, ); print(x)
man = ("Molla", "Fra", (1, 9, 2000))
*_, (*_, xz) = man; print(xz, *_)

def add(*put):
    put += (3, ); return put
print(add(2, 4, 6))
print(tuple('lupin'), tuple(range(3)))

x = (1, 2); y = x; x += y; print(y, x)
a = 1, 2, 3, 4; _, x, y, _ = a; print(x, y)
x, *y, z = (1, 2, 3, 4, 5); print(x, z, *y)
x = (12, 45, 22222, 103, 6)
print('{0} {2} {1} {2} {3} {4}'.format(*x))
x, y = ('a', 'b', 'c', 'd', 'e'), ('1', '2', '3')
z = x; print(x + y, x > y, y > x, x == y, len(x), max(x), min(x))

"""            LIST            """
#list is muteable
x = y = [12, 13, 14]
x = [9, 10, 11]; y[0] = -1; x.append(5)
x.sort(); x += [4]; x += [6]; print(x, y)
x = sorted(x); print(x, y)
x = [1, 2, 3, [4, 5, 6], 7]; print(x, x[3], x[3][2])
x, y = [1, 3.60, 'Hello', 'd'], ["Hello", "world"];x.insert(3, [2009])
x += y; print(x, x[0 : 2], x * 2)
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; print(x, x[0][0], x[0][1])
x = ['A', 'B', 'C', 'D', 'E']; x.insert(1,  'F'); 
import collections as col
print(col.OrderedDict.fromkeys(x).keys())
print(list(reversed(x))[0 : 2])
x.reverse(); print(x, len(x), 'A' in x, 'a' in x)
if 'B' in x:    x.remove('B')
for i in x:    print(i, end = " ")
print(); print(x.index('F'), x.count('A'))
for i in x:    print(i[: 1], end = " ")
for idx, i in enumerate(x):    print("%s has an index of %d" % (i, idx))
for i in range(2, 4):   print("%d contains %s" % (i, x[i]))
for s in x[1 :: 2]:
    print(s, end = " ")
    for i in range(1, len(x), 2):    print(x[i])
for item in x:    
    if item == 'C':    del x[0]
    print(item, end = " ")
for (idx, item) in enumerate(x):    print('pos {} is: {}'.format(idx, item))
for i in range(len(x)):    print(x[i], end = " ")
y = x[: :-1]; x.reverse()
if x == y:    print('TRUE')
print(len(['one', [2, 3], 'four']))
ing = "abcdef"
print(ing[-1], ing[:], ing[: :], ing[3:], ing[:4])
print(ing[2: 4], ing[: :2], ing[1: 4: 2], ing[5: None: -1], ing[: :-1], ing[5: 0: -1])
x = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]; x[0][0].append(1)
for row in x:
    for col in row:    print(col, end = " ")
print()
print([col for row in x for col in row])
x[1].insert(2, 15)
for row in range(len(x)):
    for col in range(len(x[row])):    print(x[row][col], end = " ")
print(x, x[1][1:])
values = [('a', 'b'), ('x', 'y'), ('1', '2')]
for item in values:    print(item[0], item[1], end = "\t")
for item in values:
    i1, i2 = item; print(item[0], item[1], end = "\t")
for i1, i2 in values:    print(i1, i2, end = "\t")
print()
data = "MOLLA IBRAHIM 22 2000"
name, age, salary = slice(0, 13), slice(13, 15), slice(15, None)
print(data[name], data[age], data[salary])
x, y = [1, 2, 3, 4, 5], ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']
print(map('{}'.format, x))
print(list(set(y)))
for item in x:
    for name in y:
        print(item, name, end = " ")
        if item == 4 and name == 'Cc':    break
    print("Inner")
print("Outer")
print('Cc' in y, 'Ff' in y, 'Cc' in set(y))
x, y = ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3', 'b4']
z = x[:]; z.append('d')
for a, b in zip(x, y):    print(a, b, end = " ")
print(len(list(zip(x, y))), z)
print("{[2]}".format(x))
*x, y = [1, 2, 3, 4, 5, 6]; print(*x, y, x[0], x[1:])
a, *x, b = [1, 2, 3, 4, 5]; print(a, b, *x)
a, x, b, x, c, *x = [1, 2, 3, 4, 5, 6]; print(a, b, c)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x[1: 3] = [6]; x[4 : 6] = [0, 1]
x[:] = [4, 5, 6]; x[-2:] = [4, 5, 6]
y = x[:]; print(y, x is y)
print(list(map(lambda i : i * i, x)))
print(x[len(x) - 1], x[3], x[-3], x[:], x[2 : 6], x[1 :], x[:7])
print(x[1 :8 :2], x[2 :8 :-1], x[8 :2 :-2], x[: :-1])
x.append(100); x.insert(6, -1); x.extend([46, 47, 48]); x.extend(range(3))
print(x.index(2), x.index(2, 3), x.pop(2), x.count(3))
if 5 in x:    x.remove(5)
if 6 in x:    print(x.index(6))
x.sort(); x.sort(reverse = True); x.reverse()
print(x, x.pop(), x.count(0))
print(len(x), max(x), min(x))
for i in range(0, 5):
    if i in x:    x.remove(i)
print(x.pop(2), x.pop())
x[1] = -1; x[2 : 4] = [34, 35, 36]
x = ["Molla"] * 3; print(x)
x = [2, 4, 6] * 3; print(x)
x = list(range(3)); del x[::2]; print(x)
del x[-1]; print(x)
x = [None] * 10; print(x)
x = [{1}] * 10; x[0].add(2); print(x)
print([{1} for _ in range(10)])
val = ["1", "2", "3", "4"]
print([int(item)for item in val], map(float, val))

num = int(input("Enter digits: "))
if num in x:    x.remove(num)
else:    print("Doesn't exit")
if len(x) > 1:    print(x.sort(), x.pop(), x.pop(1)) #return none, x.pop(idx)
while(i := len(x) > 2):
    x.pop(); print(i, end = " ")
x = [1, 10, 15, ["Aa", "Bb", "Cc"], 17, -20]
print(x[3][1], x[len(x) - 1], x[3][0 : 3], x[3][-1 : 3], x[3][::-1], len(x))

x, y = ["a", "b", "c", "d"], ["a", "b", "c", "d"] 
print(x is y)
if "b" in x:    print("True")
x = [["A", "B"], ["C", " D"]]; x.append((7, 9))
for i in range(1, 5):    x.append(i)
y = ["Z", "X"]; y.append(x); print(y)
x.extend([8, 'Geeks', 'Always']); x.reverse(); print(list(reversed(x)))
print(len(x), x[:], x[-1], x[::-1])

tup = [(0, 10), (1, 15), (2, 8)]
print(min(tup), min(tup, key = lambda x : x[0]), min(tup, key = lambda x : x[1]))
print(sorted(tup, key = lambda x : x[0]), sorted(tup, key = lambda x : x[1]))
import operator as op
print(max(tup, key = op.itemgetter(0)),"\n", max(tup, key = op.itemgetter(1)))
print(sorted(tup, key = op.itemgetter(0), reverse = True), sorted(tup, key = op.itemgetter(0), reverse = True))
print(max([], default = 42), max([], default = 0))
ing = input("Enter: "); print(ing.split())
n = int(input("Enter integer: "))
lst = list(map(int, input("Enter the integer elements:").strip().split()))[:n]; print(lst)
num, odd = [1, 2, 3, 4, 5, 6, 7, 8], []
for i in num:
    if i % 2 == 1:    odd.append(i)
print(odd)
#odd = [i for i in num if i % 2 == 1 if i % 2 == 0]
even = []
for x in range(10):
    if x % 2 == 0:    even.append(x)
print(even)
#print([x if x % 2 == 0 else None for x in range(10)])
player, age, comb = ['A', 'B', 'C'], [21, 22, 23], []
for pl in player:
    for ag in age:    comb.append([pl, ag])
print(comb)
#comb = [(pl, ag)for pl in player for ag in age]
num, sum = [5, 10, 15, 20], 0
for i in num:
    sum += i;    print(i, end = " ")
    if(sum > 20):    print(sum)
print(sum)
for i in num[:]:
    sum += i; num.append(sum)
print(num) 
x = [3, -4, -2, 5, 1, 7]
print(sorted(x, key = lambda i : abs(i)))
print(list(filter(lambda i: i > 0, x)), list(map(lambda i: abs(i), x)))
x = y = [1, 2, 3, 4, 5, 6, 7]
print([i for i in x if i % 2 != 0])
print([i * 2 for i in x])
print([i ** 2 for i in x])
print([i for i in [1, 2, 3]])
print([i for i in range(11) if i % 2 == 0])
print([x ** 2 for x in range(10)])
for i in[x ** 2 for x in range(10)]:    print(i, end = " ")
print({x for x in range(5)})
print({x for x in range(1, 11) if x % 2 == 0})
print([[j for j in range(3)]for i in range(3)])
print([i * 10 for i in range(1, 6)])
print(list(map(lambda i : i * 10, [i for i in range(1, 6)])))
print(["Even" if i % 2 == 0 else "Odd" for i in range(8)])
print([num for num in range(100) if num % 5 == 0 if num % 10 == 0])
print([n ** 2 for n in range(1, 11)])
grid = [[10, 20], [30, 40], [50, 60]]
print([[i[j] for i in grid] for j in range(len(grid[0]))])
ing = 'Molla4Now'
print(list(map(lambda i : chr(ord(i) ^ 32), ing)))
print([ing[: :-1]for ing in ('Molla', '4', 'Now')])
print([sorted(x)for x in [[2, 1], [4, 3], [0, 1]]])
from functools import reduce
print(filter(lambda x : x % 2 == 0, range(10)))
print(map(lambda x : 2 * x, range(10)))
print(reduce(lambda x, y : x + y, range(10)))

print([x + y for x, y in [(1, 2), (3, 4), (5, 6)]])
print([(x, y) for x, y in [(1, 2), (3, 4), (5, 6)]])
x, y, z = [1, 2, 3 , 4], ['a', 'b', 'c', 'd'], ['6', '7', '8', '9']
print([(i, j)for i, j in zip(x, y)])
print([(i, j, k)for i, j, k in zip(x, y, z)])
print([x + y + z for x, y, z in zip([1, 2, 3], [4, 5, 6], [7, 8, 9])])
for x, y in [(1, 2), (3, 4), (5, 6)]:    print(x + y, end = " ")
#print(sum(1 for x in range(1000) if x % 2 == 0 and '9' in str(x)))
print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])
print([[x + y for x in [2, 4, 6]]for y in [1, 3, 5]])
from random import randrange
print([randrange(1, 7)for _ in range(10)])
print([x for x in range(10) if x % 2 == 0])
print([2 * x for x in range(10)])
print([ing.upper() for ing in "hello"])
print([w.strip(',') for w in ["Here", "are,,", "we,here,"]])
ing = "beautiful is better than ugly"
print(["".join(sorted(word, key = lambda x: x.lower())) for word in ing.split()])
print({ch.lower() for ch in ing if ch.isalpha()})
print([x if x in 'aeiou' else '*' for x in 'apple'])
print([x * x for x in (1, 2, 3, 4)])
sqr = []
for x in (1, 2, 3, 4):    sqr.append(x * x)
print(sqr)
a = 1;
if a in (1, 2, 3):    print(f"{a} contained")
print(list(filter(lambda x : x.isalpha(), 'a1b2c3')))
lem = filter(lambda x : x.isalpha(), 'a1b2c3'); print(''.join(lem))
print(list(map(lambda x : x * x, [1, 2, 3])))
print(list(map(lambda x, y, z : (x, y, z), [1, 2, 3], [1, 2], [1, 2, 3, 4])))
print(list(zip([0, 1, 2], [2, 3, 4])))
print(list(map(lambda x : x[0] + x[1], zip(range(5), range(5)))))
print(list(range(1, 11)))
print(map(str, [1, 2, 3, 4, 5]), list(map(str, [1, 2, 3, 4, 5])))
def digsum(n):
    dsum = 0
    for val in str(n):    dsum += int(val)
    return dsum
x = [367, 111, 562, 945, 6726, 873] 
print([digsum(i)for i in x if i & 1])
print([i ** 3 for i in x])
lett = ["apple", "banana", "cherry", "orange"] 
print([len(word) for word in lett])
dx = []
for i in range(1, 6):    dx.append(i * 10)
print(dx)
lst = []
for y in [3, 4, 5]:
    tmp = []
    for x in [1, 2, 3]:    tmp.append(x + y)
    lst.append(tmp)
print(lst)
x, y = 5, 10; print(["Less than", "Equal", " Greater than"][(x > y) - (x < y) + 1])
data = [[1, 2], [3, 4], [5, 6]] 
#print([val for lst in data for val in lst])
def func():
    res = []
    for lst in data:
        for val in lst:    res.append(val)
    return res
print(func())
grid = []
for i in range(3):
    grid.append([])
    for j in range(5):    grid[i].append(j)
print(grid)
print([[j for j in range(5)]for i in range(3)])
data = ["a", "bbbbbbb", "ccc"] 
maxi = max(map(len, data)) 
for i in data:    print('{:>{}}'.format(i, maxi))
data = [[1], [2, 3], [4, 5]]
print([val for lst in data if len(lst) == 2 for val in lst if val != 5])
print([ch for ch in 'Molla 4 Now'])
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([[row[i] for row in grid]for i in range(len(grid))])
print([[[i + j + k for k in 'cd']for j in 'ab']for i in '12'])
lst = []
for ch in 'Molla 4 Now':    lst.append(ch)
if not lst:    print("list is empty")
else:    print(lst)
x, y, z = [1, 2, 3 , 4], ['a', 'b', 'c', 'd'], ['6', '7', '8', '9']
for item in range(len(y)):
    if item % 2 == 0:    item = 'even'
    print(y, end = "\t")
for idx, item in reversed(list(enumerate(x))):
    if item % 2 == 0:    x.pop(idx)
print(x)
for idx, val in enumerate(x):
    if idx == 8:    break
    x.insert(idx, 'a')
print(x)
for idx, val in enumerate(x):
    x.pop(idx); print(x)
while(x):
    print(x[0], end = " "); x.pop(0)
print(x)
ing = "Hello"; x.append(ing); print(x, x + y)
x, tmp, i = [1, 2, 3, 4, 5, 6, 7], [], 0
for item in x:
    if item % 2 != 0:    tmp.append(item)
print(tmp)
while len(x) > 1:
    print(x[0], end = " "); x.pop(0)
print(x)
while i < len(x):
    if x[i] % 2 == 0:    x.pop(i)
    else:    i += 1
print(x)
import copy as cp
lst = [[1, 2]]; x = cp.copy(lst); y = cp.deepcopy(lst)
print(lst is x, lst[0] is x[0], lst is y, lst[0] is y)
name = ['A', 'B', 'C', 'A']; print(list(map(len, name)))
res = [len(item)for item in name]
genex = (len(item)for item in name)
print(res, list(genex))
import operator as op
lst = [5, 8, 10, 20, 50, 100]
print(reduce(op.add, lst), reduce(op.mul, lst), reduce(op.add, ["Here", "I", " Am"]))
from functools import reduce
from itertools import accumulate
lst = [5, 8, 10, 20, 50, 100]
print(reduce((lambda x, y : x + y), lst))
print(reduce(lambda x, y : x if x > y else y, lst))
def reduce(func, able, init = None):
    it = iter(able)
    if init is None:
        try:    value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value")
    else:    value = init
    for ele in it:    value = func(value, ele)
    return value
res = reduce(lambda x, y: x + y, [1, 2, 3, 4]); print(res)
res = reduce(lambda x, y: x * y, [1, 2, 3, 4], init = 2); print(res)
tup = (2, 1, 0, 0, 0, 2, 2, 2)
print(reduce(lambda x, y : x + y, tup, 6))
print(list(accumulate(lst, lambda x, y : x + y)))
import datetime as dt
x = [{'nome' : 'Molla', 'Bdate' : dt.date(2000, 9, 1), 'height' : 176}, {'nome' : 'Kazi', 'Bdate' : dt.date(2001, 7, 1), 'height' : 172}, 
    {'nome' : 'Khan', 'Bdate' : dt.date(1998, 6, 27), 'height' : 174}, {'nome' : 'Hasan', 'Bdate' : dt.date(1997, 5, 17), 'height' : 178}]
x.sort(key = lambda item : item['nome']); print(x)
x.sort(key = lambda item : item['Bdate']); print(x)
x.sort(key = lambda item : item['height']); print(x)
x = [{'nome' : 'Molla', 'Bdate' : dt.date(2000, 9, 1), 'size': {'height' : 176, 'weight' : 100}}, {'nome' : 'Kazi', 'Bdate' : dt.date(2001, 7, 1), 'size' : {'height' : 172, 'weight' : 85}}, 
    {'nome' : 'Khan', 'Bdate' : dt.date(1998, 6, 27), 'size' : {'height' : 174, 'weight' : 89}}, {'nome' : 'Hasan', 'Bdate' : dt.date(1997, 5, 17), 'size' : {'height' : 178, 'weight' : 95}}]
x.sort(key = lambda item : item['size']['height']); print(x)
import datetime as dt
print(dt.datetime.today())
from operator import itemgetter
x = [{'nome' : 'Molla', 'age' : 27, 'salary' : 1500}, {'nome' : 'kazi', 'age' : 23, 'salary' : 1150}, 
    {'nome' : 'Khan', 'age' : 30, 'salary' : 1700}, {'nome' : 'Hasan', 'age' : 19, 'salary' : 900}]
x.sort(key = (itemgetter('age'))); print(x)
x.sort(key = (itemgetter('salary'))); print(x)
x = [(1, 2), (3, 4), (5, 0)]
print(x.sort(key = itemgetter(1)))
import operator, functools, itertools
x = [1, 2, 3, 4]; print(x, *x)
print(functools.reduce(operator.truediv, x))
print(list(itertools.zip_longest([1, 2, 3], [1, 2], [1, 2, 3, 4])))
x, y, z = ['a1', 'a2', 'a3'],  ['b1'], ['c1', 'c2', 'c3', 'c4']
for a, b, c in itertools.zip_longest(x, y, z):    print(x, y, z, end = " ")

x = [7, 'x', (1, 2), [5, 6], 5, 8.0, 'y', 1.2, [7, 8], 'z']; print(sorted(x, key = str))
ing = "hello world"; vowel = []
for ing in 'aeiou':    vowel.append(ing)
print(vowel, ing)
x = [[]] * 4; x[0].append(23) #x = [[23], [23], [23], [23]]
def add(x):
    x += [3]; return x # x.extend([3])
print(add([2, 3, 4]))
from itertools import filterfalse
names = ['Fred', 'Wilma', 'Barney']
def longname(name):    return len(name) > 5
print(filter(longname, names), list(filter(longname, names)), list(filterfalse(longname, names)))
print([name for name in names if len(name) > 5])
print(list(filter(None, [1, 0, 2, [], '', 'a'])))
print(list(filterfalse(None, [1, 0, 2, [], '', 'a'])))
print(list(filter(lambda x : x.startswith('d'), names)))
from operator import methodcaller
print(list(filter(methodcaller('startswith', 'd'), names)))
import time
def loop(n):
    res = []
    for i in range(n):    res.append(i ** 2)
    return res
def compresslist(n):
    return [i ** 2 for i in range(n)]
begin = time.time(); loop(10 ** 6); end = time.time()
print(round(end - begin, 2))
begin = time.time(); compresslist(10 ** 6); end = time.time()
print(round(end - begin, 2))
x, y = [], [[]]; x = y + y + y
y.append(1); print(x)
x = [[]] * 3; print(id(inner) for inner in x)
x = [[] for _ in range(3)];print(id(inner) for inner in x)
x = []
for i in range(3):    x.append([])
for k in x:    print(id(k))
for i, val in enumerate(x): print((i, val), end = " ")

def tion(x = None):
    if not x:
        x = []; x.append(1); print(x)
def func(x = []):
    x.append(1); print(x)
def unct(x = None):
    if x is None:
        x = []; x.append(1); print(x)
func([2]); func([3])
tion(); tion([]); tion(x = ""); tion(x = 0)
unct()   
def shift(x, pos):
    pos %= len(x); return(x[:-pos] + x[-pos:])
x = [3, -4, -2, 5, 1, 7]
print(shift(x, -7), shift(x, 5), shift(x, 3))
def append(val, y = None):
    if y is None:    y = []
    y.append(val); return y
print(append(2), append(3, []))
def func(x):
    x[0] = 9; print(x)
x = [4, 6, 8]; print(x); func(x); print(x)
def func(x):
    x[0] = 9; x = [1, 2, 3]; x[2] = -8
    print(x)
x = [4, 6, 8]; func(x)
def func(lst, incr): 
    result = lst[0] 
    lst[0] += incr 
    return result
lst = [0]
print(f'{func(lst, 2)} {func(lst, 3)}')
print(f'{func(lst, 2)} {func(lst, 3)}')
def func(i):
    return i, i + 0.5
def generate():
    for i in range(3):
        for x in func(i):    yield str(x)
print([str(x)for i in range(3)for x in func(i)], "\n", list(generate()))

lst = [2, 4, 6, 8]
print(any(x == 0 for x in lst))
print(type(a > b for a in lst if a % 2 == 1))
print(sum((i for i in range(10) if i % 2 == 0)))
lem = lambda x : x * x; print(lem(4))
print(map(len, ["Mary", "Isla", "Sam"]))
arr = [1, 2, 3, 4, 5, 6]
print([i for i in filter(lambda x : x > 4,arr)])
def addition(x):    return x + x
num = (2, 4, 6, 8)
print(list(map(addition, num)))
print(list(map(lambda x : x + x, num)))
print(list(map(lambda x : x ** 2, num)))
num, ber = [1, 2, 3], [4, 5, 6]
print(list(map(lambda x, y : x + y, num, ber)))
lst = ['sat', 'sun', 'mon', 'fri']; print(list(map(list, lst)))

x, y, z = [100, 111, 99, 97], [102, 117, 91, 102], [104, 102, 95, 101]
print(list(map(avrg, x, y, z)))
print(list(map(median, x, y, z)))
def func(lst):
    for item in lst:    print(item, end = " ")
import operator as op
lst = ['a', 'b', 'c', 'd']; func(lst)
x, y = [100, 111, 99, 97], [102, 117]
print(list(map(op.sub, x, y)), list(map(op.sub, y, x)))

insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x : x + ' is an insects'
print(list(map(f, insects)), list(map(len, insects)))
carnivores = ['lion', 'tiger', 'leopard', 'arctic fox'] 
herbivores = ['african buffalo', 'moose', 'okapi', 'parakeet'] 
omnivores = ['chicken', 'dove', 'mouse', 'pig']
def animals(w, x, y, z):    
    return '{0}, {1}, {2}, and {3} ARE ALL ANIMALS'.format(w.title(), x, y, z)
print(list(map(animals, insects, carnivores, herbivores, omnivores)))
