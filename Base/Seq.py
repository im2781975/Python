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
#tuple
def multi():
    return 3, 4
print(multi())
things = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
print(things)
print(things[0])
print(things[-1])
print(things[5:2:-1])
print(type(things))
for item in things:
    print(item)
print(len(things))
mega = ([1, 2, 3],[4, 5, 6])
#change able in 2D tuple
mega[0][1] = 66
print(mega)
