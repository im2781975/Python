i = 0
while i < 7:    
    print(i)    
    if i == 4:        
        print("Breaking from loop")
        break    
    i += 1
    
for i in (0, 1, 2, 3, 4):    
    print(i)    
    if i == 2:        
        break
    
for i in (0, 1, 2, 3, 4, 5):    
    if i == 2 or i == 4:
        continue    
    print(i)
    
while True:    
    for i in range(1,5):        
        if i == 2:            
            break 
        
def break_loop():    
    for i in range(1, 5):        
        if (i == 2):            return(i)        
        print(i)    
    return(5)
    
def break_all():    
    for j in range(1, 5):        for i in range(1,4):            if i*j == 6:                    return(i)            print(i*j)
    
for i in [0, 1, 2, 3, 4]:
    print(i)
for i in range(5):    
    print(i)
for x in ['one', 'two', 'three', 'four']:    
    print(x)
for x in range(1, 6):    
    print(x)
for index, item in enumerate(['one', 'two', 'three', 'four']):   
    print(index, '::', item)

x = map(lambda e :  e.upper(), ['one', 'two', 'three', 'four']) 
print(x)

for i in range(3):    
    print(i) 
else:   
    print('done')
    
i = 0
while i < 3:    
    print(i)    
    i += 1 
else:    
    print('done')
    
for i in range(2):    
    print(i)    
    if i == 1:        
        break 
else:    
    print('done')

a = [1, 2, 3, 4] 
for i in a:    
    if type(i) is not int:        print(i)        
        break 
    else:    
        print("no exception")

a = 10 
while True:    
    a = a-1    
    print(a)    
    if a<7:        
        break
print('Done.')

i = 0 
while i < 4:
    i = i + 1
