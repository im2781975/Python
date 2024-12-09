my_array = array('i', [1,2,3,4,5]) 
print(my_array[1]) 
print(my_array[2]) 
print(my_array[0])

from array import *
my_array = array('i', [1,2,3,4,5]) 
my_array.append(6)
my_array.insert(0,0)
my_array.remove(4)
my_array.pop()
my_array.reverse()
my_array.count(3)
print(my_array.index(5))
my_extnd_array = array('i', [7,8,9,10]) 
my_array.extend(my_extnd_array)
c=[11,12,13] 
my_array.fromlist(c)
my_array.buffer_info() (33881712, 5)
for i in my_array:    
    print(i)
    
my_char_array = array('c', ['g','e','e','k'])
print(my_char_array.tostring())

my_array = array('i', [1,2,3,4,5]) c = my_array.tolist()
my_char_array = array('c', ['g','e','e','k']) 
my_char_array.fromstring("stuff") 
print(my_char_array)
