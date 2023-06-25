import datetime
def dayOfProgrammer(year):
    if year <= 1917:
        if year % 4 == 0:
            x = datetime.date(year, 9, 12)
            return x.strftime("%d.%m.%Y")
        else:
            x = datetime.date(year, 9, 13)
            return x.strftime("%d.%m.%Y")
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            x = datetime.date(year, 9, 12)
            return x.strftime("%d.%m.%Y")
        elif year == 1918:
            x = datetime.date(year, 9, 26)
            return x.strftime("%d.%m.%Y")
        else:
            x = datetime.date(year, 9, 13)
            return x.strftime("%d.%m.%Y")

print(dayOfProgrammer(1918))