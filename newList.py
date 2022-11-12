cars=["TATA", "Alto", "Nano","Jeep"]
newList=[]
for i in cars:
    if "A" in i or "a" in i:
        newList.append(i)
print(newList)