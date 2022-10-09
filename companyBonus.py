#company will give bonus based on following criteria

#time spent in company          #bonus
# >10 yrs                          10%
# >=6 and <=10                     8%
# <6                                5%
#ask the salary and time spent from the user
#print the net bonus amount accordingly

currentSalary = float(input("Enter your current salary: "))
servicePeriod = float(input("Enter your service period: "))

if servicePeriod > 10:
    print("The net bonus amount will be: ", ((currentSalary*0.1)+currentSalary))
elif servicePeriod >= 6 and servicePeriod <= 10:
    print("The net bonus amount will be: " , ((currentSalary*0.08)+currentSalary))
elif servicePeriod < 6:
    print("The net bonus amount will be: ", ((currentSalary*0.05)+currentSalary))
else:
    print("The net bonus amount will be: ", currentSalary)