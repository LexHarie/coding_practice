def add_time(start, duration,old_day=""):
    start = start.split(":")
    duration = duration.split(":")
    days_later = None
    New_AM_or_PM = None

    new_minutes = None
    old_day = old_day.title()
    days = ['Sunday','Monday', 'Tuesday','Wednesday', 'Thursday','Friday','Saturday']
    new_day = ''
    new_hour = 0
    # start[1][3:] = AM or PM
    # start[1][:2] = Minutes of the hour
    # start[0] = hours
    # duration[1] = minute of duration
    # let's start by adding the hours of the duration

    if start[1][3:] == 'AM':
        days_later = (int(start[0]) + (int(duration[1]) + int(start[1][:2])) // 60 + int(duration[0])) // 24 
        if (int(start[0]) + (int(duration[1]) + int(start[1][:2])) // 60 + int(duration[0])) % 24 >= 12:
            New_AM_or_PM = 'PM'
        else:
            New_AM_or_PM = 'AM'
    elif start[1][3:] == 'PM':
        days_later = (int(start[0]) + 12 + int(duration[0]) + (int(duration[1]) + int(start[1][:2])) // 60) // 24
        if (int(start[0]) + 12 + int(duration[0]) + (int(duration[1]) + int(start[1][:2])) // 60) % 24 >= 12:
            New_AM_or_PM = 'PM'
        else:
            New_AM_or_PM = 'AM'

    if start[1][3:] == 'AM':
        if (int(start[0]) + int(duration[0])) % 24 <= 12:
            if (int(start[0]) + int(duration[0])) % 24 == 0:
                new_hour += 12
            else:
                new_hour += (int(start[0]) + int(duration[0])) % 24
        else:
            new_hour += (int(start[0]) + int(duration[0])) % 24 - 12
    elif start[1][3:] == 'PM':
        if (int(start[0]) + 12 + int(duration[0])) % 24 <= 12:
            if (int(start[0]) + 12 + int(duration[0])) % 24 == 0:
                new_hour += 12
            else:
                new_hour += (int(start[0]) + 12 + int(duration[0])) % 24
        else:
            new_hour += (int(start[0]) + 12 + int(duration[0])) % 24 - 12
            
    # if the sum of duration[1] plus the start[1][:2] (minutes of the hour) is greater than 60, we add to the new_hour
    if int(duration[1]) + int(start[1][:2]) >= 60:
        new_hour += 1
        if int(duration[1]) + int(start[1][:2]) - 60 < 10:
            new_minutes = "0" + str(int(duration[1]) + int(start[1][:2]) - 60)
        else:
            new_minutes = str(int(duration[1]) + int(start[1][:2]) - 60)
    elif int(duration[1]) + int(start[1][:2]) < 60:
        if int(duration[1]) + int(start[1][:2]) < 10:
            new_minutes = "0" + str(int(duration[1]) + int(start[1][:2]))
        else:
            new_minutes = str(int(duration[1]) + int(start[1][:2]))

    for index, day in enumerate(days):
        if day == old_day:
            new_day = days[(index + days_later) % 7]
            break
        
    if old_day == "":
        if days_later == 1:
            return f"{new_hour}:{new_minutes} {New_AM_or_PM} (next day)"
        elif days_later > 1:
            return f"{new_hour}:{new_minutes} {New_AM_or_PM} ({days_later} days later)"
        elif days_later == 0:
            return f"{new_hour}:{new_minutes} {New_AM_or_PM}"
    else:
        if days_later == 1:
            return f"{new_hour}:{new_minutes} {New_AM_or_PM}, {new_day} (next day)"
        elif days_later > 1:
            return f"{new_hour}:{new_minutes} {New_AM_or_PM}, {new_day} ({days_later} days later)"
        elif days_later == 0:
            return f"{new_hour}:{new_minutes} {New_AM_or_PM}, {new_day}"

    result = add_time(start, duration)
    print(result)
