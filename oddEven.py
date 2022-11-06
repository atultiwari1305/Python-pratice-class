def oddcheck(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even, odd

list=[32, 21, 64, 100, 13]
even,odd=oddcheck(list)

print("No. of even:",even)
print("No. of odd=",odd)