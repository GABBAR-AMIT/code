#Write a Python script to display the various Date Time formats -
#a) Current date and time
#b) Current year
#c) Month of year
#d) Week number of the year
#e) Weekday of the week
#f) Day of year
#g) Day of the month
#h) Day of week

import datetime
x = datetime.datetime.now()
print(x) # for current date & time 
print(x.year)# for current year 
print(x.month)# for current month 
# Month of year
month_of_year = x.strftime("%B")
print("Month of year:", month_of_year)
# Week number of the year
week_number = x.strftime("%U")
print("Week number of the year:", week_number)
# Weekday of the week
weekday = x.strftime("%A")
print("Weekday of the week:", weekday)
# Day of year
day_of_year = x.strftime("%j")
print("Day of year:", day_of_year)
# Day of the month
day_of_month = x.strftime("%d")
print("Day of the month:", day_of_month)
# Day of week 
day_of_week = x.strftime("%w")
 




