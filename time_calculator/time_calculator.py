# apparently can not use any
# packages, so no re package sadge


# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday
#
# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM
#
# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)
#
# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)
# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)

def add_time(start, duration, day=None):
    """
    Taking user starting day and iterate through week depending on
    duration added on to start
    """
    days = {'MONDAY': 'Monday', 'TUESDAY': 'Tuesday', 'WEDNESDAY': 'Wednesday',
            'THURSDAY': 'Thursday', 'FRIDAY': 'Friday', 'SATURDAY': 'Saturday',
            'SUNDAY': 'Sunday'}
    days_no = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
               4: 'Thursday', 5: 'Friday', 6: 'Saturday',
               7: 'Sunday'}

    """
    Alternating am pm meridian for every 12 hour shift
    """
    am_pm_dic = {'AM': 'PM', 'PM': 'AM'}

    """
    Making string more appropriate case wise
    """
    if day is not None:
        day = day.upper()
    """
    Splitting the start and duration time into list 
    with hours and minutes and setting format 
    """
    starting_time = start.split()
    if len(starting_time[0]) == 4:
        hour = int(starting_time[0][0:1])
        minutes = starting_time[0][2:]
        temp = starting_time[0].replace(':', '.')
        am_pm = starting_time[1]
    else:
        hour = int(starting_time[0][0:2])
        minutes = starting_time[0][3:]
        temp = starting_time[0].replace(':', '.')
        am_pm = starting_time[1]

    tmp_add = ''
    test_temp = ''
    for i in duration:
        if i != ":":
            tmp_add += i
        test_temp += i.replace(':', '.')
    hour_add = tmp_add[:-2]
    minutes_add = tmp_add[-2:]
    # total_min = float(temp) * 60 + float(test_temp)*60
    counter = 0
    no_days = 0
    new_min = int(minutes_add) + int(minutes)
    new_hour = hour
    #new_min_str = str(new_min)
    """
    Adding hours if minutes exceeds 60 minutes and 
    resetting minutes
    """
    counter_temp = 0
    if new_min >= 60:
        new_min = new_min % 60
        new_hour += 1
        if new_min < 10:
            new_min_str = '0' + str(new_min)
        else:
            new_min_str = str(new_min)
        if new_hour == 12 and int(hour_add) == 0:
            am_pm = am_pm_dic[am_pm]
    elif new_min < 10:
        new_min_str = '0' + str(new_min)
    else:
        new_min_str = str(new_min)
    """
    Adding duration hours to start hours, 
    incrementing # days
    """
    if int(hour_add) != 0:
        while counter < int(hour_add):
            if new_hour == 12:
                if am_pm == 'PM':
                    no_days += 1
                new_hour = 0
                counter_temp += 1
                # if counter_temp % 2 == 0:
                #     no_days += 1
                am_pm = am_pm_dic[am_pm]

            new_hour += 1
            counter += 1
        if new_hour == 12:
            am_pm = am_pm_dic[am_pm]
            no_days += 1
    # print(temp,hour, minutes,am_pm, hour_add,minutes_add)
    # print(test_temp,new_min,new_min_str, no_days)
    """
    Corresponding to day #, getting the 
    string of day
    """
    new_day = ''
    if day is not None:
        for c, d in days_no.items():
            if days[day] == d:
                for i in range(no_days):
                    if c == 7 and i == no_days - 1:
                        c = 1
                        #new_day = days_no[c]
                    elif c == 7:
                        c = 1
                        continue
                    else:
                        c+=1
                new_day = days_no[c]
    """
    Output as per conditions set by
    project
    """
    if day is None:
        if no_days == 1:
            output = str(new_hour) + ":" + new_min_str + " " + am_pm + " " + "(next day)"
        elif no_days == 0:
            output = str(new_hour) + ":" + new_min_str  + " " + am_pm
        else:
            output = str(new_hour) + ":" + new_min_str + " " + am_pm + " " + f"({no_days} days later)"
    elif day is not None and no_days == 0:
        output = str(new_hour) + ":" + new_min_str + " " + am_pm + "," + " " + new_day
    elif day is not None and no_days == 1:
        output = str(new_hour) + ":" + new_min_str + " " + am_pm + "," + " " + new_day + " " + "(next day)"
    else:
        output = str(new_hour) + ":" + new_min_str + " " + am_pm + "," + " " + new_day + " " + f"({no_days} days later)"

    return output
