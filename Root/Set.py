num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num)
number = set(num)
print(number)
number.add(10)
print(number)
if 5 in number:
    number.remove(5)
print(number)
for i,item in enumerate(number):
    print(i,item)
A = {1, 2, 3}
B = {3, 4, 5, 6, 7}
print(A & B)
print(A | B)
#dictionary or key value pair
person = ['A', 'B', 22, 'C' ]
info = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p = {'name': 'A', 'add' : 'B', 'age' : 22, 'job' : 'C'}
print(p)
print(p['job'])
print(p.keys())
print(p.values())
p['lang'] = 'python'
p['name'] = 'X'
print(p)
for key,value in p.items():
    print(key, value)
