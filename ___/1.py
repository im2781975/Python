state = {
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H' }
print(state['A'], "\n", state.keys(), "\n", state.values())
for key in state.keys():
    print('{} is the cap of {}'.format(state[key], key))
from collections import defaultdict
state = defaultdict(lambda : 'Boston',{
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H' })
print(state['X'], "\n", state.keys(), "\n", state.values())
for key, value in state.items():
    print(key, value, end = " ")
guy = [
    {'name' : 'A', 'age' : 12}, {'name' : 'B', 'age' : 17},
    {'name' : 'C', 'age' : 15}, {'name' : 'D', 'age' : 22}]
print(list(filter(lambda x : x['age'] < 20, guy)))
print(list(filter(lambda x : x['age'] % 2 == 0, guy)))
info = {'name' : 'A', 'add' : 'B', 'age' : 22, 'job' : 'C'}
info['lang'] = 'python'; info['name'] = 'x'
print(info, info['name'], info.keys(), info.values())
for key, value in info.items():
    print(key, value, end = " ")
