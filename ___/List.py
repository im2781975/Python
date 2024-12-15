#list is Muteable
#Assign & access value 
x = y = [12, 13, 14]
x = [9, 10, 11]
y[0] = -1
print(f"x:{x}, y:{y}")
x = [1, 2, 3, [4, 5, 6], 7]
print(f"x:{x},\nx[3]:{x[3]}, \nx[3][2]:{x[3][2]} ")

lst = [1, 3.60, 'Hello', 'd']
tisl = ["Hello", "world"]
lst += tisl
print(lst, lst[0 : 2], lst * 2)
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

l1 = [1, 2, 3, 4, 5]
l2 = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']
for item in l1:
    for name in l2:
        print(item, name)
        if item == 4 and name == 'Cc':
            break
    print("Inner")
print("outer")

number = [5, 10, 15, 20]
sum = 0
for num in number:
    sum += num
    print(num)
    if sum > 20:
        print(f"{sum} is Greater than 20")
print(sum)
for i in number[:]:
    sum += i
    number.append(sum)
print(number)
