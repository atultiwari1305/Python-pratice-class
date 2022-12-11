class Student:
    numberOfSubject = 5

    @classmethod
    def classMethodExample(cls):
        return cls.numberOfSubject

    @staticmethod
    def staticMethodExample():
        print("This is an example of static method")

print(Student.classMethodExample())

Student.staticMethodExample()