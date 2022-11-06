def characters(names):
    more=0
    less=0
    for i in names:
        if len(i)>5:
            print(i)
            more+=1
        else:
            less+=1
    return more,less

names=["Atul", "Shubham", "Anurag", "Rahul", "Dev", "Roy"]
more,less=characters(names)
print("More than 5:",more)
print("Less or equal to 5:",less)