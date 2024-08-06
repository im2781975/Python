#scope
a = 15
def display():
    a = 10
    def show():
        print(a)
    show()
display()
#print(a)
####
a, b = 6, 9
def display():
    if a < b:
        c = a + b
    print(c)
display()
#Global
a = 10
def display():
    global a
    #without global keyword we can access the variable not modify
    a += 1
    print(a)
display()
####
def display():
    a = 20
    def show():
        #global a
        a += 5
    print(a)
    show()
    #print(a)
display()
#print(a)
