#nest dict to dict
studentData = {
    "A":{"roll": 10, "Age": 22, "course": "python",},
    "B": {"roll": 12, "Age": 24, "course": "java",}
}
studentData["A"]["num"] = 789
print(studentData["A"])
print(studentData["B"]["Age"])
#del studentData["A"]["num"]
print(studentData["A"].pop("num"))
print(studentData["A"])

#nesting dict to list
Data ={
    "A":["roll: 10", "Age: 12", "course: python"],
    "B": ["roll: 12", "Age: 24", "course: java"]}
print(Data)
#nest list to dict
studentData = [
    {"Name: ": "A", "roll": 10, "Age": 22, "course": "python",},
    {"Name: ":"B", "roll": 12, "Age": 24, "course": "java", "number": [2345, 7896]}
]
print(studentData)
print(studentData[1], studentData[1]["number"])
