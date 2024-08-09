class Instructor:
    def __init__(self):
        print("constructor")
a = Instructor()
a.name = "molla"
b = Instructor()
b.name = "vai"
print(a.name, b.name)
