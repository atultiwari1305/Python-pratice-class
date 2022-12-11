class Student:
    def __init__(self, marks1, marks2, marks3):
        self.web = marks1
        self.python = marks2
        self.maths = marks3

    def average(self):
        return (self.web + self.python + self.maths)/3

student1 = Student(5,4,3)
student2 = Student(7,8,9)
student3 = Student(3,6,9)

print(student1.average())
print(student2.average())
print(student3.average())