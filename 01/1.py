import calendar
from datetime import date

def next_leap_year():
    today = date.today()
    year = today.year

    while not calendar.isleap(year):
        year += 1

    return year

def count_leap_years(y1: int, y2: int) -> int:
    count = calendar.leapdays(y1, y2)

    if calendar.isleap(y2):
        count += 1

    return count

def day_of_week(d: date) -> int:
    return calendar.weekday(d.year, d.month, d.day)

if __name__ == '__main__':
    print(next_leap_year())
    print(count_leap_years(2000,2050))
    print(day_of_week(date(day=29, month=7, year=2016)))