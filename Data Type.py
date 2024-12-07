#keyword
import keyword
print(keyword.kwlist)

#assign value
a, b, _ = 1, 2, 3
print(a, b, _)
c = d = e = 1
print(c, d, e)
x = y = [12, 13, 14]
x = [9, 10, 11]
y[0] = -1
print(x, y)
n = [1, 2, [3, 4, 5], 6]
print(n[2], n[2][2])
print(reversed("Hello"))

#isinstance
i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i);
    i += 1
#convert sequence
a = "hello"
print(type(a), list(a), set(a), tuple(a))

#Muteable
def muteable(m):
    m.append(3)
x = [1, 2]
muteable(x)
if x == [1, 2]:
    print("Yes")
else:
    print("No")
print(x)
#tuple is immuteable

#list
name = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
name.insert(1, 'Sia')
name.remove('Bob')
name.index('Alice')
len(name)
name.reverse()
for element in name:
    print(element)
print(name.count('Alice'))

#dict
state = {
    'A' : 'B', 'C' : 'D',
    'E' : 'F', 'G' : 'H'
}
print(state['A'])
for k in state.keys():    
    print('{} is the capital of {}'.format(state[k], k))

#set
from collections import defaultdict
state_capitals = defaultdict(lambda: 'Boston', {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
})
print(state_capitals['Alabama'])

#string
s = """w'o"w""" 
print(repr(s))
print(str(s)) 
print(eval(repr(s)) == s)

#datetime
import datetime 
today = datetime.datetime.now() 
print(str(today))
print(repr(today))

#class
class Represent(object):    
    def __init__(self, x, y):       
        self.x, self.y = x, y    
    def __repr__(self):       
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)   
    def __str__(self):        
        return "Representing x as {} and y as {}".format(self.x, self.y)
r = Represent(1, "Hopper") 
print(r)
print(r.__repr__) 
rep = r.__repr__()  
print(rep)  
r2 = eval(rep) 
print(r2)  
print(r2 == r)
#string
ing = 'Helloword'
print(ing[0 : 6])
#set
et = {'A', 'B', 'C', 'A', 'C'} 
print(et)
st= set('abcded') 
st.add('z')
print(st)
frset = frozenset('Mollavai')
print(frset)
#set is muteable(mean can add or remove) but frozen is immuteable
#list
list = [123, 'abcd', 10.2, 'd']
list1 = ['hello', 'world']
print(list[0: 2])
print(list * 2)
print(list + list1)
#dictionary
dic={'name' : 'red', 'age' : 10}
print(dic, dic['name'])
print(dic.keys(), dic.values())
#tuple(immuteable)
tuple = (123, 'hello') 
tuple1 = ('world')
print(tuple, tuple[0])
