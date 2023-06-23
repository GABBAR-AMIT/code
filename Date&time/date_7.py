# Write a Python program to print yesterday, today, tomorrow.
import datetime

# Get the current date
today = datetime.date.today()

# Calculate the date for yesterday and tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

# Print the dates
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
