def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n=int(input("Enter your number: "))
product=fact(n)
print(product)