class bird:
    def category(self):
        print("This is a category of bird")
    def fly(self):
        print("I can fly")

class sparrow(bird):
    def sizeParameter(self):
        print("I am small in size")
class crow(bird):
    pass
class ostrich(bird):
    def fly(self):
        print("I can't fly, sorry")

objBird = bird()
objSparrow = sparrow()
objcrow = crow()
objOstrich = ostrich()

objBird.category()
objBird.fly()
objSparrow.category()
objSparrow.fly()
objcrow.category()
objcrow.fly()
objOstrich.category()
objOstrich.fly()