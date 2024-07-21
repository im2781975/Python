import string, random
letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letters =list(string.ascii_letters)
spaces = list(string.whitespace)
printable =list(string.printable)
digit =list(string.digits)
punctuation = list(string.punctuation)
print("Password Generator: \n")
l = int(input("Enter Number of letter: "))
d = int(input("Enter Number of digits: "))
p = int(input("Enter Number of punctuation: "))
password = []
for i in range(1, l + 1):
    char = random.choice(letter)
    password += char
for i in range(1, d + 1):
    char = random.choice(digit)
    password += char
for i in range(1, p + 1):
    char = random.choice(punctuation)
    password += char
random.shuffle(password)
print(password)
Generated = ""
for i in password:
    Generated += i
print(Generated)
