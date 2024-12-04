x = 20
y = 10.2
print(x + y)
print(type(x))
print(0o123, 0O123)
#converted octal to decimal to decimal
print(0b101, 0B101)
#converted binary to decimal to decimal
print(0x87, 0X87)
#converted hexa to decimal to decimal
print(type(0x87))
length = len("ibrahim")
print("Your name has " + str(length) + " characters");
print(int("10") + int("10"))
first = input("Enter integer:")
sec = input("Enter integer:")
sum = int(first) + int(sec)
print(sum)

#indentation
for i in range(5):
    print("a")
    print("b")
    if i == 2:
        print("welcome")
        if True:
            print("Hello")
print("Bye")
