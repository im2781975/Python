def double_it(num):
    num = num*2
    print(num)
    return num
double_it(8)
double_it(9)

def sum(a, b, c = 0):
    res = a + b + c
    return res
#def sum(a, b):
    #res = a + b
    #return res
total = sum(23, 24)
print(total)

final = double_it(total)
print("Final value is:",final)

def all_sum(x, y, *args):
    print(args)
    s = 0
    for num in args:
        print(num)
        s+=num
    print(s)
        
t = all_sum(45, 56, 77, 89)
print(t)
