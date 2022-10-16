from ast import operator


num1=float(input("Enter your number: "))
num2=float(input("Enter your number: "))
op=input("Enter your operator: ")

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
elif op=="**":
    print(num1**num2)
elif op=="%":
    print(num1%num2)
elif op=="//":
    print(num1//num2)