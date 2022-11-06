#create a function using following conditions
#it should accept employee name and salary and display both
#if salary is missing ,default=10000

def employee(name,salary=10000):
    print("Employee name is: ",name)
    print("Salary of",name,"is",salary)

employee("Anurag",10)
employee("Atul",1000000)
employee("Shubham")
