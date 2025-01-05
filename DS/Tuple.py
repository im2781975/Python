t = ('a', 'b', 'c', 'd', 'e')
t0 = () #Empty tuple
t = tuple('lupins') 
print(t)              
t = tuple(range(3)) 
print(t)    

t = (1, 2) 
q = t 
t += (3, 4)
print(q, t)

a = 1, 2, 3, 4
_, x, y, _ = a
first, *more, last = (1, 2, 3, 4, 5)

tuple1 = ('a', 'b', 'c', 'd', 'e') 
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')
print(tuple1 + tuple2)
cmp(tuple1, tuple2)
cmp(tuple2, tuple1)
cmp(tuple1, tuple3)
len(tuple1)
max(tuple1)
min(tuple1)
list = [1,2,3,4,5] tuple(list)

hash( (1, 2) ) 
hash( ([], {"hello"}) 

x = (1, 2, 3)
print(x[0], x[1], x[2], x[-1], x[-2], x[-3], x[:-1], x[-1:], x[1 : 3])

colors = "red", "green", "blue" 
rev = colors[::-1]
colors = rev

rev = tuple(reversed(colors))
colors = rev

t = (12, 45, 22222, 103, 6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.
