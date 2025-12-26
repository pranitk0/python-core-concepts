def convert_time_24_to_12(hour, minute):
    
    if hour == 0:
        hour_12 = 12
        period = "AM"
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    elif hour > 12:
        hour_12 = hour - 12
        period = "PM"
    else:
        hour_12 = hour
        period = "AM"
    
    return f"{hour_12:02d}:{minute:02d} {period}"

h = int(input("Enter hour (0-23): "))
m = int(input("Enter minute (0-59): "))

time_12hr = convert_time_24_to_12(h, m)
print("12-hour format:", time_12hr)
