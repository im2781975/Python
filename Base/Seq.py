name = 'ibrahimmolla'
name1 = 'Molla vai'
name3 = 'Molla\'s vai' #escape
name2 = "Molla's vai"
name4 = """Molla 
ibrahim """
print([name1],[name2],[name3])
print(name4)
print(name[3])
print(name[2:6])
print(name[0:12])
print(name[12:0:-1])
print(name[-1:-12:-1])
print(name.upper())
print(name.lower())
print(name.capitalize())
#string is immutable like name[0] = 'R' cant assign
for char in name2:
    print(char)
if 'molla' in name:
    print('exits')
else:
    print('No')
