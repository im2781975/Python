#isinstance
i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1
print(i)
#control statement
cnt = 1
while cnt <= 10:
    print(cnt)
    cnt += 1
    if cnt == 7:
        #continue
        break
    print("inner loop")
print("outer loop")
#range
for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)

for i in range(5):
    print("a")
    print("b")
    if i == 2:
        print("Welcome")
        if True:
            print("Hello")
print("Bye")

def display():
    for i in range(1, 11):
        print(i)
display()
