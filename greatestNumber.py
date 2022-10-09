#take two inputs from user an be int or float
#print the greatest number

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if num1>num2:
    print("the greatest number is:", num1)
elif num2>num1:
    print("The greatest number is:", num2)
else:
    print("Both are equal")