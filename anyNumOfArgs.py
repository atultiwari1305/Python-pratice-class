#create a function in such a way that we can pass any number of arguements to this and it should display each arg value

def things(*arg):
    for i in arg:
        print(i)

things("car","bike","cycle","scooter")