name = ["Aa", "Bb", "Cc", "Dd", "Ee"]
length = len(name)
#reverse idx starting from -1
print(name[length -1], name[-1])

from random import *
#import randorm
#x = random.randint(a, b)
#x = randint(a, b)
x = randint(1, 7) #a <= x <= b
x = randrange(1, 9) #a <= x < b
x = random()
x = uniform(1, 3) #a < x <=b,it will return floating point
l = [2, 8, 5, 1, 9]
x = choice(l)
shuffle(l) #it shuffle the list
print(l)
print(x)

