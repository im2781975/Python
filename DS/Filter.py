names = ['Fred', 'Wilma', 'Barney']
def long_name(name):   
    return len(name) > 5
filter(long_name, names)
list(filter(long_name, names))
[name for name in names if len(name) > 5]

from itertools import ifilter
ifilter(long_name, names)
list(ifilter(long_name, names))
(name for name in names if len(name) > 5)

list(filter(None, [1, 0, 2, [], '', 'a']))

car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
def find_something_smaller_than(name_value_tuple):  
    print('Check {0}, {1}$'.format(*name_value_tuple)    
    return name_value_tuple[1] < 100 
    next(filter(find_something_smaller_than, car_shop))
    
from itertools import filterfalse
list(filterfalse(None, [1, 0, 2, [], '', 'a'])) 

names = ['Fred', 'Wilma', 'Barney']
def long_name(name):   
    return len(name) > 5
list(filterfalse(long_name, names))

car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)] 
def find_something_smaller_than(name_value_tuple):
    print('Check {0}, {1}$'.format(*name_value_tuple)
    return name_value_tuple[1] < 100 
next(filterfalse(find_something_smaller_than, car_shop))

car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)] 
generator = (car for car in car_shop if not car[1] < 100) 
next(generator)
