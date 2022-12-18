# def add(a,b,c=0):
#     return a+b+c

# print(add(1,2))
# print(add(1,2,3))

class Area_calc:
    def calculateArea(self, length=None, breadth=None):
        if length!= None and breadth!= None:
            return length*breadth
        elif length!= None:
            return length*length

area1=Area_calc()

print(area1.calculateArea(2,3))
print(area1.calculateArea(2))