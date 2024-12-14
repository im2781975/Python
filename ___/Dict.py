state = {
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H',
}
print(state['A'])
for key in state.keys():
    print('{} is the capital of {}'.format(state[key], key))
