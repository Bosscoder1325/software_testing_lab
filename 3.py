def check(day, month):
    if (month == 4 or month == 6 or month == 9  or month == 11) and day == 31:
        return 1
    else:
        return 0
    
def isleap(year):
    if (year % 4 == 0 and year %100 == 0) or year % 400 == 0:
        return 1
    else:
        return 0

res = False
flag = False
while not flag:
    day = int(input("Enter day "))
    month = int(input("Enter month "))
    year = int(input("Enter year "))

    tomm_month = month
    tomm_year = year
    
    if day<1 or day>31:
        print("Value of day, not in the range 1...31")
        flag = True
        res = True
    
    if month<1 or month>12:
        print("Value of month, not in the range 1...12")
        flag = True
        res = True
    elif check(day,month):
        print("value of day, not in the range day<=30")
        flag = True
        res = True
    
    if year<1812 or year>2015:
        print("value of year, not in the range 1812...2015")
        flag = True
        res = True
    
    if month==2:
        if isleap(year) and day>29:
            print("invalid date input for leap year")
            flag = True
            res = True
        elif (not(isleap(year)) and day>28):
            print("invalid date input for not a leap year")
            flag = True
            res = True
    flag = True
    
tomm_day = 0
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day<31:
        tomm_day = day + 1
    else:
        tomm_day = 1
        tomm_month = month + 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day<30:
        tomm_day = day + 1
    else:
        tomm_day = 1
        tomm_month = month + 1

elif month == 12:
    if day<31:
        tomm_day = day+1
    else:
        tomm_day = 1
        tomm_month = 1
        if year == 2015:
            print("The next day is out of boundray value of year")
            tomm_year = year + 1
        else:
            tomm_year = year + 1

else:
    if day<28:
        tomm_day = day + 1
    elif isleap(year) and day == 28:
        tomm_day = day + 1
    elif day == 28 or day == 29:
        tomm_day = 1
        tomm_month = 3
      
if not res:
    print(f"next day is {tomm_day} {tomm_month} {tomm_year}")
    
