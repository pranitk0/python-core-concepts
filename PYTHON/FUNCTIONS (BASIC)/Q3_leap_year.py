def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
yr = int(input("Enter a year: "))
if is_leap_year(yr):
    print(f"{yr} is a Leap Year")
else:
    print(f"{yr} is not a Leap Year")
