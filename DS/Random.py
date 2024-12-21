
from string import punctuation, ascii_letters, digits
symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom() 
password = "".join(secure_random.choice(symbols) for i in range(10)) 
print(password)

import string 
alphabet = string.ascii_letters + string.digits 
while True:    
    password = ''.join(choice(alphabet) for i in range(10)
    if (any(c.islower() for c in password)
        and any(c.isupper() for c in password) 
        and sum(c.isdigit() for c in password) >= 3): 
        break
    
from random import SystemRandom 
secure_rand_gen = SystemRandom()
print([secure_rand_gen.randrange(10) for i in range(10)])
print(secure_rand_gen.randint(0, 20))

import random
laughs = ["Hi", "Ho", "He"]
random.shuffle(laughs) 
print(laughs)
print(random.choice(laughs))
print(random.sample(    laughs   ,     1    ))
print(random.sample(laughs, 3)) 
print(random.sample(laughs, 4))
random.randint(1, 8)
random.randrange(100)
random.randrange(20, 50)
random.rangrange(10, 20, 3)
random.random()
random.uniform(1, 8)

random.seed(5)  
print(random.randrange(0, 10)) 
print(random.randrange(0, 10))
random.seed(5)
print(random.randrange(0, 10))

save_state = random.getstate() 
print(random.randrange(0, 10))
print(random.randrange(0, 10))
random.setstate(save_state)
print(random.randrange(0, 10))
print(random.randrange(0, 10))
random.seed(None)
random.seed()

import random 
probability = 0.3 
if random.random() < probability:    
    print("Decision with probability 0.3") 
else:    
    print("Decision with probability 0.7")

