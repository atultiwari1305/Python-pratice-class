class Person:
    def __init__(self):
        self.name = "Atul"
        self.age = 19

    def change(self,name):
        self.name = name

    def compareAge(self,other):
        if (self.age == other.age):
            return True
        else:
            return False

person1 = Person()
person2 = Person()


person2.change("Raj")
person2.age = 22

if person1.compareAge(person2):
    print("They are of same age.")
else:
    print("They are of different age.")

print(person1.name)
print(person2.name)
