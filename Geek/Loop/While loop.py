# Python program to illustrate 
# while loop 
count = 0
while (count < 3): 
    count = count + 1
    print("Hello Geek")
////
age = 28
  
# the test condition is always True 
while age > 19: 
    print('Infinite Loop')
////
# Prints all letters except 'e' and 's' 
i = 0
a = 'geeksforgeeks'
  
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
          
    print('Current Letter :', a[i])
    i += 1
////
# break the loop as soon it sees 'e' 
# or 's' 
i = 0
a = 'geeksforgeeks'
  
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        break
          
    print('Current Letter :', a[i]) 
    i += 1
////
# An empty loop 
a = 'geeksforgeeks'
i = 0
  
while i < len(a): 
    i += 1
    pass
    
print('Value of i :', i) 
////
# Python program to demonstrate 
# while-else loop 
  
i = 0
while i < 4: 
    i += 1
    print(i) 
else:  # Executed because no break in for 
    print("No Break\n") 
  
i = 0
while i < 4: 
    i += 1
    print(i) 
    break
else:  # Not executed as there is a break 
    print("No Break") 
////
a = int(input('Enter a number (-1 to quit): ')) 
  
while a != -1: 
    a = int(input('Enter a number (-1 to quit): '))
////
# Initialize a counter 
count = 0
  
# Loop infinitely 
while True: 
    # Increment the counter 
    count += 1
    print(f"Count is {count}") 
  
    # Check if the counter has reached a certain value 
    if count == 10: 
        # If so, exit the loop 
        break
  
# This will be executed after the loop exits 
print("The loop has ended.") 
////
# checks if list still 
# contains any element 
a = [1, 2, 3, 4] 
  
while a: 
    print(a.pop())
////
# Python program to illustrate 
# Single statement while block 
count = 0
while (count < 5): 
    count += 1
    print("Hello Geek") 
////
initial_height = 10 
bounce_factor = 0.5 
height = initial_height 
while height > 0.1:   
    print("The ball is at a height of", height, "meters.") 
    height *= bounce_factor   
print("The ball has stopped bouncing.")
////
countdown = 10
while countdown > 0: 
    print(countdown) 
    countdown -= 1
print("Blast off!") 
