def add_time(start, duration, day=None):
    #Transforming start to 24h clock
    start_split = start.split(":")
    if start[-2:] == "PM":
        start_split[0] = str(int(start_split[0])+12)
        start_split[1] = start_split[1].replace(" PM", "") 
        #start_split = ":".join(start_split)
    start_split[1] = start_split[1].replace(" AM", "")
    
    #Summing the time passed
    time_sum = []
    duration_split = duration.split(":")
    time_sum.append(int(start_split[0])+int(duration_split[0]))
    time_sum.append(int(start_split[1])+int(duration_split[1]))
    if time_sum[1] > 60:
        hours = int(time_sum[1]/60)
        time_sum[0] += hours
        time_sum[1] -= hours*60

    #dividing days
    days_count = 0
    if time_sum[0] >= 24:
        days_count += int(time_sum[0]/24)

    #days of the week
    if day != None:
        day = day.lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = days.index(day)
        days.extend(days)
        days.extend(days)
        day_index += days_count
        week_day = days[day_index]

    #converting back to 12h clock
    converted = []
    converted.append(time_sum[0] % 24)
    converted.append(time_sum[1])
    if len(str(converted[1])) < 2:
        converted[1] = "0" + str(converted[1])
    if converted[0] > 12:
        converted[0] = str(converted[0]-12)
        converted[1] = str(converted[1]) + " PM"
    else:
        if converted[0] == 12:
            converted[0] = str(converted[0])
            converted[1] = str(converted[1]) + " PM"
        if converted[0] == 0:
          converted[0] += 12
        
        converted[0] = str(converted[0])
        converted[1] = str(converted[1]) + " AM"
    converted = ":".join(converted)
    if converted[-5:] == "PM AM":
      converted = converted[:-3]

    

    #Output
    if day == None:
        if days_count == 0:
            return converted 
        if days_count == 1:
            return converted + " (next day)"
        else:
            return converted + f" ({days_count} days later)"
    else:
        if days_count == 0:
            return converted + ", " + week_day.title()
        if days_count == 1:
            return converted + ", " + week_day.title() + " (next day)"
        else:
            return converted + ", " + week_day.title() + f" ({days_count} days later)"