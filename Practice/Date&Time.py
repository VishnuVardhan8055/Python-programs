# To Check Date and Time
import datetime
now = datetime.datetime.now()
print("Current Date & Time : ")
print(now.strftime("%Y-%m-%d  %H:%M:%s"))
import calendar
Year = 2023
print(calendar.calendar(Year))
month = 3
print(calendar.month(Year,month))
from calendar import calendar
yy = 20
print('Calendar',calendar(yy))