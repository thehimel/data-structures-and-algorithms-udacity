def isLeapYear(year):
    assert type(year) is int
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def daysInMonth(year, month):
    assert type(year) is int
    assert type(month) is int

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        return 28
    else:
        return 30


def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    if month < 12:
        return year, month + 1, 1
    return year + 1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    # assert the 2nd date is not before the 1st date
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    return days


def test():
    assert isLeapYear(2004) is True
    assert isLeapYear(2008) is True
    assert isLeapYear(2012) is True
    assert isLeapYear(1900) is False
    assert isLeapYear(1904) is True
    assert isLeapYear(2000) is True
    assert isLeapYear(2400) is True

    # assert dateIsBefore(2013, 1, 1, 2013, 1, 1) is True
    assert dateIsBefore(2013, 1, 1, 2013, 1, 2) is True

    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1

    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert nextDay(2013, 9, 30) == (2013, 10, 1)
    assert nextDay(2012, 2, 28) == (2012, 2, 29)

    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    assert daysBetweenDates(2013, 1, 24, 2013, 6, 29) == 156

    print("Test Successful")


test()
