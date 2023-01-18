def times(date1, date2):
    month1, day1, year1 = map(int, date1.split("/"))
    month2, day2, year2 = map(int, date2.split("/"))
    if year1 == year2:
        if month1 == month2:
            if day1 == day2:
                print("same")
            elif day1 < day2:
                print("before")
            else:
                print("after")
        elif month1 < month2:
            print("before")
        else:
            print("after")
    elif year1 < year2:
        print("before")
    else:
        print("after")

date1 = input("Enter the first date: ")
date2 = input("Enter the second date: ")
times(date1, date2)