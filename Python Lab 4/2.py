from datetime import date, timedelta
sub_five_days = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',sub_five_days)
