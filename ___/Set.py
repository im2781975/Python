#set is muteable(mean can add or remove) but frozen is immuteable
#set print unique elements
st = {'A', 'B', 'C', 'D', 'B'}
tes = set('abcde')
tes.add('z')
print(tes, st)
frset = frozenset("Mollvai")
print(frset)

