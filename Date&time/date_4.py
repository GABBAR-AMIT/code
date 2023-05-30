# Write a Python program to get the current time in Python.
#Sample Format :  13:19:49.078205
import datetime

current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
print("Current Time:", current_time)
