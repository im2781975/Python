#import pyautogui
from math import *
from random import *
from time import sleep
res = ceil(4.0001)
result = floor(3.9000)
print(res, result)
print(random())
print(randint(1, 100))
sleep(4)
print(choice(['A', 'B', 'C', 'D', 'E']))
"""
sleep(5)
for i in range(0, 3):
    pyautogui.write('i am here',interval = 0.25)
    pyautogui.press('enter')

with open('message.txt','w') as file:
    file.write('python')
with open('message.txt','a') as file:
    file.write('python')
with open('message.txt','r') as file:
    text = file.read()
    print(text)
"""
try:
    x = 45/1
    print(x)
except:
    print("Error happened")
finally:
    print("Done")
