attended=float(input("Enter the no. of lectures attended: "))
total=float(input("Enter total lectures in semester: "))

percentage= (attended/total)*100
print("Your attendence is:", percentage,"%")
if percentage >= 75:
    print("YOU ARE ALLOWED TO GIVE EXAM.")
else:
    print("YOU ARE NOT ALLOWED TO GIVE EXAM.")