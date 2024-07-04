x = 0

# traditional python if elif else statement
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
////
x = 0

# Python one liner if elif else statement
result = {x > 0: "Positive", x < 0: "Negative"}.get(True, "Zero")

print(result)
/////
x = 0

{x > 0: print("Positive"), x < 0: print("Negative")}.get(True, print("Zero"))
////

