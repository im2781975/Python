#list is Muteable
#Assign & access value 
x = y = [12, 13, 14]
x = [9, 10, 11]
y[0] = -1
print(f"x:{x}, y:{y}")
x = [1, 2, 3, [4, 5, 6], 7]
print(f"x:{x},\nx[3]:{x[3]}, \nx[3][2]:{x[3][2]} ")

#insert
name = ['A', 'B', 'C', 'D', 'E']
name.insert(1, 'F')
print(len(name))
name.reverse()
if 'B' in name:
    name.remove('B')
for i in name:
    print(i)
print(name.count('A'))
print(f"name: {name}, \nname.index[F]: {name.index('F')} ")
