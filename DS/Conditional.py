n = 5
print("Hello") if n > 10 else print("Goodbye") if n > 5 else print("Good day")
#Boolean Logic
print(1 and 2)
print(1 and "Hello")
print(" " and "Hello")
print(1 or 2)
print(None or 1)
print(0 or [])

def print_me():        
    print('I am here!')
0 and print_me()

a = 1 
if a == 3 or 4 or 6:
    print('yes')
else:
    print('no')
if a in (3, 4, 6): 
    print('yes') 
else:
    print('no')
    
x, y = 5, 10
print( ['less than', 'equal', 'greater than'][ (x > y) - (x < y) + 1 ])

import datetime
if not aDate:
    aDate = datetime.date.today()

