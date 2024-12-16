state = {
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H',
}
print(state['A'])
print(state.keys(), state.values())
for key in state.keys():
    print('{} is the capital of {}'.format(state[key], key))
#defaultdict
from collections import defaultdict
stateCapital = defaultdict(lambda: 'Boston',{
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H',
})
print(stateCapital['X'])
"""                    """
actress = [
    {'name' : 'A', 'age' : 12}, {'name' : 'B', 'age' : 17},
    {'name' : 'C', 'age' : 15}, {'name' : 'D', 'age' : 22}
    ]
junior = filter(lambda x : x['age'] < 20, actress)
fiver = filter(lambda x : x['age'] % 2 == 0, actress)
print(list(junior), list(fiver))

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = set(number)
num.add(10)
if 5 in num: num.remove(5)
print(num)
for i, item in enumerate(num):
    print(i, item)
A, B = {1, 2, 3}, {3, 4, 5, 6, 7, 8}
print(f"A & B: {A & B}\nA | B: {A | B} ")
comb = {}
comb = {(x, y)for x in A for y in B}
print(comb)
info = {'name' : 'A', 'Add' : 'B', 'age' : 22, 'job' : 'C'}
print(info, info['name'])
print(info.keys(), info.values())
info['lang'] = 'python'
info['name'] = 'X'
for key, value in info.items():
    print(key, value)
    
#num = {'A' : 23, 'B' : 34, 'C' : 45, 'A' : 56}
#num = dict({'A' : 23, 'B' : 34, 'C' : 45, 'A' : 56})
#Duplicate key will be ovverride
num = dict([('A', 23), ('B', 34), ('C', 45)])
num['D'] = {67, 78, 89}
num['B'] = {'Home' : 9876, 'work' : 5462}
num['A'] = 12
print(f"num: {num}\nnum['A']: {num['A']}\nnum['B']['work']: {num['B']['work']}\nnum.get(B): {num.get('B')}\n")
for i in num:
    print(i)
    print(num[i])
#print tuple
for i in num.items():
    print(i)
#copy dict
cpy = num.copy()
print(cpy, len(cpy))

Data = { 1 : 'abc', 2 : 'bcd', 3 : 'cde'}
print(f"data[1]: {Data[1]}\ndata.keys(): {Data.keys()}\ndata.values(): {Data.values()}\ndata.items(): {Data.items()} ")
del Data[2] #For delete data
print(Data.popitem())
print(Data.popitem())
Data.clear() #For.clear dict
print(Data)

Data = {
    "A" : {"roll" : 23, "age" : 22, "course" : "python"},
    "B" : {"roll" : 12, "age" : 24, "course" : "java", "num" : [234, 876]}
}
Data["A"]["num"] = 789
del Data["A"]["num"]
#print(Data["A"].pop("num"))
print(f"Data: {Data}\nData[A]: {Data['A']}\nData[B][num]: {Data['B']["num"]} ")
