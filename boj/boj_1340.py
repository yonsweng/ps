from sys import stdin


def solve():
    time = stdin.readline().strip()

    # Month DD, YYYY HH:MM format
    month, day, year, hour, minute = time.replace(",", "").replace(":", " ").split()
    day = int(day)
    year = int(year)
    hour = int(hour)
    minute = int(minute)

    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    month_days = {
        "January": 31,
        "February": 29 if is_leap_year else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }
    days_passed = (
        sum(month_days[m] for m in list(month_days)[: list(month_days).index(month)])
        + day
    )
    total_minutes = (days_passed - 1) * 24 * 60 + hour * 60 + minute

    total_minutes_in_year = 366 * 24 * 60 if is_leap_year else 365 * 24 * 60
    percentage = (total_minutes / total_minutes_in_year) * 100
    print(f"{percentage}")


if __name__ == "__main__":
    solve()
