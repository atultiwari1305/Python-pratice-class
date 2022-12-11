class Person:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def printOutput(self):
        print("The name is: ",self.name ,"and the roll no. is: ",self.rollNo)

person1=Person("Atul", 37)
person2=Person("Shubham", 61)

print(id(person1))
print(id(person2))

person1.printOutput()
person2.printOutput()