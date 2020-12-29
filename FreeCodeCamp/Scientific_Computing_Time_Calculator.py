def add_time(start_time, duration, day="None"):
    time = start_time.split(" ")
    # return (time[0])

    #Day of Week
    day_of_week=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

    #Deconstruct user input
    day = day.capitalize()
    start_hhmm = time[0].split(":")
    # return (start_hhmm)
    start_hh = start_hhmm[0]
    start_mm = start_hhmm[1]

    #convert start time to minutes based on AM/PM
    if time[1].lower() == "am":        
        start_total_min = int(start_hh) * 60 + int(start_mm)
    else: #assume time is in PM
        start_total_min = (int(start_hh) + 12) * 60 + int(start_mm)
        # return (start_total_min)

    usradd_time = duration.split(":")
    usradd_hh = usradd_time[0]
    usradd_mm = usradd_time[1]

    #Add time to minutes based on user provided input
    if int(usradd_hh) < 12 :        
        add_total_min = int(usradd_hh) * 60 + int(usradd_mm)
    else: #assume time is in PM
        add_total_min = int(usradd_hh) * 60 + int(usradd_mm)
        # return (add_total_min)

    #Final value in minutes
    total_time_min = start_total_min + add_total_min
    # return (total_time_min)

    #Calculate return value
    days = int(total_time_min / 1440)
    hours_24h = int(total_time_min % 1440 / 60)
    minutes = total_time_min % 60
    hours_12h_AM = True
    hours_12h = hours_24h

    #convert hours to 12H format if hours_24h is greater or equals to 12
    if hours_24h >= 12:
        hours_12h = hours_24h % 12
        hours_12h_AM = False

    #Convert hours and minutes into string for output
    hours_12h = str(hours_12h)
    if hours_12h == "0":
        hours_12h = "12"
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes) 
    
    if day != "None":
        day_index = int(day_of_week.index(day)) + 1
        day_index += days
        out_day = (day_index % 7) - 1
    separator = ", "

    #output variable starts getting constructed here
    if hours_12h_AM == True:
        output_val = hours_12h + ":" + minutes + " AM"
    else:
        output_val = hours_12h + ":" + minutes + " PM"
    
    # #detecting for same day
    # if days == 0:
    #     pass
    
    #if day argument is not provided
    if day == "None":
        #detecting for next day
        if days == 0 and day == "None":
            pass
        elif days == 1:
            output_val += " (next day)"
        
        #detecting for anything after 2 days
        else:
            output_val +=  " ("+ str(days) +" days later)" 

        #if day (optional argument) is NOT provided
        # return total_time_min

    #if day arguement is provided
    else:
                
        if days == 0:
            output_val += separator + day_of_week[out_day]
        
        #detecting for next day
        elif days == 1:
            output_val += separator + day_of_week[out_day] + " (next day)"
        
        #detecting for anything after 2 days
        else:
            output_val += separator + day_of_week[out_day] + " ("+ str(days) +" days later)" 
        # return (total_time_min)
    # return new_time
    return (output_val)

print(add_time("11:59 PM", "24:05", "sunday"))