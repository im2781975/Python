
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
"""				"""
print('python' == 'py' + 'thon')
print('this is not a common string' == 'this is not' + ' a common string')
print('this is not a common string' == 'this is not' + ' a common string')
ing, b = u'Café', 'Lorem ipsum'
print(isinstance(ing, str))
ing = b'Cafe'          
ing = 'Café'.encode()
print(isinstance(ing, str))
ing = b"abc"
print(ing[0] == 97, ing[0 : 1] == b"a", ing[1] == 98, ing[1 : 2] == b"b")
print(u"Hello, Here i am"[::-1])
print("Hello, Here i am"[::-1])
print("A", "B", "C", sep = "")
print("A", "B", "C", sep = ",")
print("A", "B", end = ".\n")
print("Flush this", flush = True)
"""            """
ing = "Hello world!"
print([ing for ing in 'aeiou'], ing)
print(str[i] for i in [1, 2, 3, 4, 5])
ing = ""
for i in range(1, 22):
    ing += str(i)
    ing += ","
print(ing)
ing = bytearray(b'stack')
print(id(ing))
ing += b'overflow'
print(id(ing), bytearray(b'StackOverflow'))
rin = ing
rin += b'rock'
print(bytearray(b'StackOverflow rocks!'))
print(id(rin) == id(ing))
"""					"""
ing = 'thisisashorttext' 
print(ing.count('t'), ing.count('th'), ing.count('is'), ing.count('text'))
print(Counter(ing))
print(sorted( [" foo ", " bAR", "BaZ "], key = lambda s: s.strip().upper())) 
print(sorted( [" foo ", " bAR", "BaZ "], key = lambda s: s.strip()))
print(sorted(map(lambda s: s.strip().upper(), [" foo ", " bAR", "BaZ "])))
print(sorted(map(lambda s: s.strip(), [" foo", "bAR", "BaZ"])))

string = "GFG"
ch_iterator = iter(string)
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
