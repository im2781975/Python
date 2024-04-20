class Student:
    def __init__(self, name, id, cur):
        self.name = name
        self.id = id
        self.cur = cur
        
    def __repr__(self) -> str:
        return f'name:{self.name} id:{self.id} cur:{self.cur} '

class Teacher:
    def __init__(self, name, sub, id):
        self.name = name
        self.sub = sub
        self.id = id
        
    def __repr__(self) -> str:
        return f'name:{self.name} sub:{self.sub} id:{self.id} '

class school:
    def __init__(self, name):
        self.name = name
        self.Teachers = []
        self.Students = []
        
    def add(self, name, sub):
        id = len(self.Teachers) + 101
        teacher = Teacher(name,sub,id)
        self.Teachers.append(teacher)
        
    def enroll(self, name, fee):
        if fee < 6500:
            return f'please provide more'
        else:
            id = len(self.Students) + 1
            student = Student(name, 'C', id)
            self.Students.append(student)
            return f'student enrolled with name {name} id {id} extra money {fee - 6500 }'

    def __repr__(self) -> str:
        result = f"{self.name}\n"
        for t in self.Teachers:
            result += f"{t}\n"
        for s in self.Students:
            result += f"{s}\n"
        return result

a = school('a')
a.enroll('b', 5200)
a.enroll('c', 6700)
a.add('d', 'e')
a.add('f', 'g')
print(a)

