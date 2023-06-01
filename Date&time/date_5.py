#Write a Python program to subtract five days from the current date.
#Sample Date :
#Current Date : 2015-06-22
#5 days before Current Date : 2015-06-17
import datetime

current_date = datetime.date.today()
five_days_ago = current_date - datetime.timedelta(days=5)

print("Current Date:", current_date)
print("5 days before Current Date:", five_days_ago)
