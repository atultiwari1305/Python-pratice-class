#A company decided to give 1000rs bonus to employee
#if his/her service is more than 5 years
#Ask user their salary and years of service
#print the net bonus amount

currentSalary = float(input("Enter your current salary: "))
servicePeriod = float(input("Enter your service period: "))

if servicePeriod > 5:
    print("Net salary will be: ", (currentSalary+1000))
else:
    print("Net salary will be: ", currentSalary)