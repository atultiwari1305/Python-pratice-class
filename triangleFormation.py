a=float(input("Enter 1st side: "))
b=float(input("Enter 2nd side: "))
c=float(input("Enter 3rd side: "))

if a+b>c and b+c>a and c+a>b:
    print("THIS WILL FORM A TRIANGLE")
else:
    print("IT WILL NOT FORM A TRIANGLE")