""" date """
import datetime

current_date_time = datetime.datetime.now()
print(current_date_time)

year = current_date_time.year
print(year)

print(current_date_time.strftime("%A"))


# create a date object
created_date = datetime.datetime(2021, 10, 20)
print(created_date, type(created_date))
print(created_date.strftime("%B"))