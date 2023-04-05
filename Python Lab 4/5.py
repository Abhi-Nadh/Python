from datetime import date

fYear = int(input('Enter the year: '))
fMonth = int(input('Enter the month: '))
fDay = int(input('Enter the day: '))
sYear = int(input('Enter the year: '))
sMonth = int(input('Enter the month: '))
sDay = int(input('Enter the day: '))

day1=date(fYear,fMonth,fDay)
day2=date(sYear,sMonth,sDay)

difference=(day2-day1)
print(difference.days,"days")