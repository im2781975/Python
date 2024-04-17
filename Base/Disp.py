age = 45
name = "ibrahim"
double = 3.4
is_single = True
print(age)
print(name)
print(double)
print(is_single)
print(age + double)
print(age * double)
print(type(name))
print(type(double))
print(type(is_single))
#Alt + shift + A - Multiline comment
#Ctrl + / - Single line comment
print("******")
print('Ibrahim' + ' ' + 'Aslam')
test = f"Name {name}, age {age}, is_single {is_single}, interest rate {double}%."
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
print("Signed Division is:",first_int//second_int)
print("Power is:",first_int**second_int)

# >, <, >=, <=, ==, !==
if first_int!=second_int:
    print("Varified")
elif first_int>second_int:
    print("Varified")
else:
    print("Not Varified")

# +=, -=, *=, /=
#in, not, not in, is, is not
# and, or
a = 34
boss = False
a+=23
print(a)
if a > 5:
    print("True")
elif a > 3:
    print("True")
elif a==2:
    print("True")
else:
    print("False")
if boss is True or boss is not False:
    print("True")
else:
    print("False")
coin = 'head'
if boss == False:
    print("False")
    if coin == 'tail':
        print("Batting")
    else:
        print("Bowling")
else:
    print("True")
if a > 5:
    if a%2 == 0 and a > 7:
        print("Even")
    else:
        print("Odd")
else:
    print("less than 5")

num = 1
while num <=10:
    num += 1
    if num == 2 or num %2 == 0:
        continue
    print(num)
    if num == 8:
        break
    
number = [5, 10, 15, 20]
sum = 0
for num in number:
    print(num)
    sum +=num
    if sum > 20:
        print("Max", sum)
print(sum)
text = "ibrahim"
for char in text:
    print(char)
#for i in range(1, 10)
for i in range(1, 10, 2):
#range(start, end, step)
    print(i)
friends = ['A', 'B', 'C']
for friend in friends:
    print(friend)
