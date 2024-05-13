import random
class school:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, sub, teacher):
        self.teachers[sub] = teacher
    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'{classroom_name} isn\'t available ')
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        serial_id = f'{self.name} - {len(self. students) + 1 }'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)
    def __str__(self):
        return f'{self.name} - {len(self.students)} '
    def get_top_students(self):
        pass
class Person:
    def __init__(self, name):
        self.name = name
class Teacher(Person):
    def __init__(self, name, sub):
        super().__init(name)
        self.sub = subjects 
    def teach(self):
        self.teach = teach
    def take_exam(self, sub, students):
        for student in students:
            marks = random.randint(0, 100)
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__id = None
        self.classroom = None
        self.subjects = []
        self.marks = {}
        self.grade = None
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, val):
        self.__id == val
