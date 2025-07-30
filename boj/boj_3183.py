def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


while True:
    day, month, year = map(int, input().split())
    if day == 0 and month == 0 and year == 0:
        break

    if month < 1 or month > 12 or day < 1:
        print("Invalid")
        continue

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            print("Invalid")
            continue
    elif month in [4, 6, 9, 11]:
        if day > 30:
            print("Invalid")
            continue
    elif month == 2:
        if is_leap_year(year):
            if day > 29:
                print("Invalid")
                continue
        else:
            if day > 28:
                print("Invalid")
                continue
    else:
        print("Invalid")
        continue
    print("Valid")
