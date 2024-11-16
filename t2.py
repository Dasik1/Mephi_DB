# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sun Nov 10 19:28:27 2024
in Tims II Lab

@author: Stark
"""


import icalendar

# Open the ICS file
with open('1.ics', 'rb') as f:
    cal = icalendar.Calendar.from_ical(f.read())

# Loop through each event in the calendar
for event in cal.walk('VEVENT'):
    # Get the event summary
    summary = event['SUMMARY']
    print('Summary:', summary)

    # Get the event start and end dates
    start = event['DTSTART'].dt.weekday()
    end = event['DTEND'].dt
    print('Start:', start)
    print('End:', end)

    # Get the location of the event
    location = event['LOCATION']
    print('Location:', location)

    # Get the description of the event
    description = event['DESCRIPTION']
    print('Description:', description)
    print("\n\n")