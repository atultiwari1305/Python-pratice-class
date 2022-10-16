a=input("Enter your Name: ")

x=len(a)

print("First letter is: ",a[0])
print("Last letter is: ",a[-1])

if x%2!=0:
    print("Middle letter is: ",a[(int(x//2))])
elif x%2==0:
    print("Middle letter is: " , a[(int((x/2)-1))])
    print("Middle letter is: " , a[(int(x/2))])