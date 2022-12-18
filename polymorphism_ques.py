class Vehicles:
    def seatingcapacity(self):
        print("Seating capacity is 4")

class car1(Vehicles):
    pass

class car2(Vehicles):
    pass

class bus(Vehicles):
    def seatingcapacity(self):
        print("Seating capacirty is 10")

bmw = car1()
audi = car2()
bus1 = bus()

bmw.seatingcapacity()
audi.seatingcapacity()
bus1.seatingcapacity()