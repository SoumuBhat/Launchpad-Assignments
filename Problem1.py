import datetime
c_year = int(datetime.datetime.now().year)
name=input("Enter Name").split()
age=int(input("Enter Age"))
current_age=c_year + 100 - age
print("Hey "+ name[0]+ "! You will turn 100 years old in " + str(current_age))