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
