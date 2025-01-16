# We often need current date and time when logging errors or saving data.
# To get current date and time, we use the datetime library.
# We need to use the datetime library to get the current date and time.

from datetime import datetime
current_date = datetime.now()
print('Today is ' + str (current_date))
print(current_date)

#There are functions you can use with datetime objects to manipulate dates
# Timedelta is a duration expressing the difference between two dates or define a period of time.
from datetime import datetime, timedelta
current_date = datetime.now()
print('Today is ' + str(current_date))
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

# Using functions to control date formating
from datetime import datetime
current_date = datetime.now()
print('Today is ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# To get current date and time, we need to use the datetime library.
from datetime import datetime

# The current_date.now() function returns the current date and time as a datetime object.
# The now function returns the current date and time.
current_date = datetime.now()

# We need to convert the datetime object to a string before we can concatenate it with other strings.
print('Today is ' + str(current_date)) 