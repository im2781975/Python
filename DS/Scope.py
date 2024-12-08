#scope
def counter():    
    num = 0    
    def incrementer():     
        nonlocal num
        num += 1        
        return num   
    return incrementer
c = counter()
for i in range(1, 12):
    print(c())
    
def readX():
    if True:
        x = 'Hi'
    print(x)
readX()

x = 'Hello'
def changeLocal():
    #global x
    x = 'Bye'
    print(x)
changeLocal()
print(x)

#del command
x = 5
print(x)
del x #delete x
print(x)

x = {'a': 1, 'b': 2} 
del x['a']
print(x) 

x = [0, 1, 2, 3, 4]
del x[1:3] 
print(x) 
