
import datetime
 
# Function to convert string to datetime
def convert(date_time):
    format = '%d %m %Y'  # The format
    datetime_str = datetime.datetime.strptime(date_time, format).isocalendar()[1]
 
    return datetime_str
 
 
# Driver code
date_time = '20 05 2018'
print(convert(date_time))