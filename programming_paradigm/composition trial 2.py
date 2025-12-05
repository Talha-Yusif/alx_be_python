class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Classroom:
    def __init__(self,name,age):
        self.student=Student(name,age)
        self.students=[]
    def add_a_student(self,student):
        self.students.append(student)
    def list_all_students(self):
        for n in self.students:
            print(f'{n.name} ,{n.age}')
class School:
    def __init__(self,classroom):
        self.classroom=classroom
        self.classrooms=[]
    def add_a_classroom(self,classrooms):
        self.classrooms.append(classrooms)
    

student1=Student("bob",3)
student2=Student("plo",8)
student3=Student("tree",9)

rew=Classroom()
rew.add_a_student(student1)
rew.add_a_student(student2)
rew.add_a_student(student3)

rew.list_all_students()