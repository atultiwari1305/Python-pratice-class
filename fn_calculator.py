n1=int(input("Enter your 1st number: "))
n2=int(input("Enter your 2nd number: "))
opr=input("Enter your operator: ")

def cal(n1,n2,opr):
    if opr=="add":
        print("The sum is:",n1+n2)
    if opr=="sub":
        print("The difference is:",n1-n2)
    if opr=="multiply":
        print("The product is:",n1*n2)
    if opr=="divide":
        print("The quotient is:",n1/n2)
cal(n1,n2,opr)