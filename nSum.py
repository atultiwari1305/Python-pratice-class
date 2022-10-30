#Write a program to accept a number from user
#calculate the sum off all the numbers from 1 to given numbers

#eg user input 10
#output should be 55
#1+2+3+4+5+6+7+8+9+10

num=int(input("Enter your number: "))

sum=0
for i in range(1,num+1):
    sum+=i

print(sum)
