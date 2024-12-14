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
