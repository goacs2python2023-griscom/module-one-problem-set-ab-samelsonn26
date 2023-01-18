def leapyear(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
print(leapyear(year))