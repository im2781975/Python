age = 45
name = "ibrahim"
double = 3.4
is_single = True
print(age)
print(name)
print(double)
print(is_single)
print(age + double)

#print(type(name))
print(type(double))
print(type(is_single))
print('Ibrahim' + ' ' + 'Aslam')
test = f"Name {name}, age {age}, is_single {is_single}. "
print(test)
first = input("First Money: ")
print("First Money is:",first)
second = input("Second Money: ")
print("Second Money is:",second)
print("First money is: ",first,"Second Money is: ",second)

#concatenate string
total = first+second
first_int=int(first)
second_int=int(second)
t = first_int + second_int
print("Total Money (string) is: ",total)
print("Total Money (int) is: ",t)
string_first= str(first)
print("After Type conversion number is:",string_first)
float_first = float(first)
print("After Type conversion number is:",float_first)

print("Sum is:",first_int + second_int)
print("Diff is:",first_int - second_int)
print("Mult is:",first_int * second_int)
print("Division is:",first_int/second_int)
print("Modulo is:",first_int % second_int)
#it will return integer
print("Division is:",first_int//second_int)
print("Power is:",first_int**second_int)

# >, <, >=, <=, ==, !=
if first_int!=second_int:
    print("Varified")
elif first_int>second_int:
    print("Varified")
else:
    print("Not Varified")
