#take input of age from 3 person
#determine the oldest and youngest

age1=int(input("Enter age of 1st person : "))
age2=int(input("Enter age of 2nd person : "))
age3=int(input("Enter age of 3rd person : "))

if age1>age2 and age1>age3:
    print("1st person is oldest")
elif age2>age1 and age2>age3:
    print("2nd person is oldest")
elif age3>age1 and age3>age2:
    print("3rd is oldest")

if age1<age2 and age1<age3:
    print("1st person is youngest")
elif age2<age1 and age2<age3:
    print("2nd person is youngest")
elif age3<age1 and age3<age2:
    print("3rd is youngest")
else:
    print("all are of same age")