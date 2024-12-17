#set is muteable(mean can add or remove) but frozen is immuteable
#set print unique elements
st = {'A', 'B', 'C', 'D', 'B'}
tes = set('abcde')
tes.add('z')
print(tes, st)
frset = frozenset("Mollvai")
print(frset)

strset = set("mollavai")
lstset = set([1, 2, "am", "ironman", 6, 9])
print(f"strset: {strset}\nlstset: {lstset}\n")
for i in lstset:
    print(i, end = " ")
