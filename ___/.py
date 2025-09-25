s = """He'l" l\'"""
#repr() : single quote (') in the string is escaped as \'.
print(s + "\n" + repr(s) + "\n" + str(s))
print(eval(repr(s)) + "\n" + eval(repr(s)) == s)
###                ###
ing = "HELLO"
rev = reversed(ing); print(rev)
rev = "".join(reversed(ing)); print(rev)
print("HELLO"[::-1])
