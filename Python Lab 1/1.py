from datetime import date


Name=input("Enter your Name: ")
age=int(input("Enter your age: "))
date=date.today()
year=date.year
dob=year-age
year_100=dob+100
print("Year When you turn hunderd years old is ",year_100)