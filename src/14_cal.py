"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input
(in the initial call to run the file) and not
prompted input. Also, the brackets around year
are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call
`python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit
either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# Todays date
theday = str(datetime.today())

# Split on "-" to separate the year and month into their own index
theday_split = theday.split("-")

# Today's year
theyear = int(theday_split[0])

# Today's month
themonth = theday_split[1]

# Since python cannot have a 0 infront of a int,
# you have to remove it and convert the month into a int
if themonth[0] == '0':
    themonth = int(themonth[1])

# If the month is above September, just convert it into a int
else:
    themonth = int(themonth)

# Instansiate a calendar.TextCalendar class
thecalendar = calendar.TextCalendar()

# If there is more then 2 system arguments
if len(sys.argv) >= 2:
    # Create a month variable with the user's specified month
    month = int(sys.argv[1])

    # If the user specified a year
    if len(sys.argv) == 3:
        # Create a year variable with the user's specified year
        year = int(sys.argv[2])

        # Create a calendar with the user's month and year
        print(thecalendar.formatmonth(theyear=year, themonth=month))

    # If the user did not specify a year,
    # create a calendar with the user's month
    # and the current year
    else:
        print(thecalendar.formatmonth(theyear=theyear, themonth=month))

# if the user did not specify and month or year, create a calendar
# with the current month and year
else:
    print(thecalendar.formatmonth(theyear=theyear, themonth=themonth))
