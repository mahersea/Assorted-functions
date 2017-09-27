#Function that converts given year to century

def centuryFromYear(year):
    y = str(year)
    start = y[:-2]
    end = y[-1:]
    print start
    print end
    if len(y) <= 2:
        y = 1
    else:
        if end == "0" and len(y) == 3:
            y = int(y[0:1])
        elif end != "0" and len(y) == 3:
            y = int(y[0:1]) + 1
        elif end == "0":
            y = int(start)
        else:
            y = 1 + int(start)
    return y

print centuryFromYear("1700")