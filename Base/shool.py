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
    def student_admission(self, student):
        classname = student.classroom.name
        if classname in self.classrooms:
            self.classrooms[classname].add_student(student)
        else:
            print(f'{classname} isn\'t available ')
    @staticmethod
    def grade_calculate(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks <= 80:
            return 'A'
        elif 60 <= marks <= 70:
            return 'A-'
        elif 50 <= marks <= 60:
            return 'B'
        elif 40 <= marks <= 50:
            return 'C'
        elif 33 <= marks <= 40:
            return 'D'
        else:
            return 'F'
    
    @staticmethod
    def grade_to_val(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'E' : 0.00
        }
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value):
        if 4.50 <= value <= 5.00:
            return 'A+'
        elif 3.50 <= value < 4.50:
            return 'A'
        elif 3.00 <= value < 3.50:
            return 'A-'
        elif 2.50 <= value < 3.00:
            return 'B'
        elif 2.00 <= value < 2.50:
            return 'C'
        elif 1.00 <= marks <= 2.00:
            return 'D'
        else:
            return 'F'
    def __repr__(self)->str:
        for key, value in self.classrooms.items():
            print(key)
        eight = self.classrooms['eight']
        for student in eight.students:
            print(student.name)
        for subject in eight.subjects:
            print(subject.name,subject.teacher.name)
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value, student.subject_grade[key])
        return ''
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []
    def add_student(self, student):
        serial_id = f'{self.name} - {len(self. students) + 1 }'
        student.id = serial_id
        self.students.append(student)
    def add_subject(self, sub):
        self.subjects.append(sub)
    def take_final(self):
        for sub in self.subjects:
            sub.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()
    def __str__(self):
        return f'{self.name} - {len(self.students)} '
    def get_top_students(self):
        pass
class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 30

    def exam(self, students):
        for student in students:
            mark = self.teacher.take_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = school.grade_calculate(mark)
class Person:
    def __init__(self, name):
        self.name = name
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self) ->str:
        return f'{self.name}'
    def teach(self):
        pass
    def take_exam(self):
        marks = random.randint(0, 100)
        return marks
class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.__id = None
        self.classroom = classroom
        self.subjects = []
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = school.grade_to_val(grade)
            sum += point
            print(self.name, grade, point)
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, val):
        self.__id == val
school = school('A', 'B')
eight = ClassRoom('eight')
school.add_classroom(eight)

abul = Student('Abir khan', eight)
school.student_admission(abul)

A_teacher = Teacher('B')
A = Subject('A', A_teacher)
eight.add_subject(A)
eight.take_final()
print(school)
