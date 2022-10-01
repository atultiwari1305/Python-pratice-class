#take inputs from user for two numbers (x and y)

x=input("Enter the first number: ")
y=input("Enter the second number: ")
temp=x
x=y
y=temp
print("The 1st swapped number is:", int(x))
print("The 2nd swapped number is:", int(y))