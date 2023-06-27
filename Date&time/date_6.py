#Write a Python program to convert a Unix timestamp string to a readable date.
#Sample Unix timestamp string : 1284105682
#Expected Output : 2010-09-10 13:31:22
import datetime

def convert_unix_timestamp(unix_timestamp):
    timestamp = int(unix_timestamp)
    date = datetime.datetime.fromtimestamp(timestamp)
    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date

# Specify the Unix timestamp string
unix_timestamp_string = '1284105682'

converted_date = convert_unix_timestamp(unix_timestamp_string)
print("Converted Date:", converted_date)
