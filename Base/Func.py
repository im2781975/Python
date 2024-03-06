def double_it(num):
    num = num*2
    print(num)
    return num
double_it(8)
double_it(9)

def sum(a, b):
    res = a + b
    return res
total = sum(23, 24)
print(total)

final = double_it(total)
print("Final value is:",final)
