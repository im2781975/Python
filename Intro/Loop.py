#for loop
name = ['Ab', 'Bc', 'Cd']
name1 = 'Molla'
for i in name:
    print(i)
    if i == 'Ab':
        print('Hey')
for x in name1:
    print(x)
num = {2, 3, 5, -2, 10}
number = [2, 3, 5, -2, 10]
sq = set()
sqr = []
for i in num:
    square = i**2
    sq.add(square)
    print(sq)
for i in number:
    sq = i**2
    sqr.append(sq)
    print(sqr)
print("List Of Square is: ", square)
