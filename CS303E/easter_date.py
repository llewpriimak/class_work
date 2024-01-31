# File: easter_date.py
# Description: This program finds easter sunday of any year
# Assignment Number: 2
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
# Slip days used this assignment: <#>
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student. .
import dataclasses
from enum import IntEnum


# class Month(IntEnum):

@dataclasses.dataclass
class MonthAndDay:
    month: int
    day: int

class Foo:
    def __init__(self, x: int):
        self.x = x
        self.y = 10


def get_easter(year: int) -> MonthAndDay:
    lunar_year_cycle_position = year % 19
    weekday_slide_part_1 = year % 4
    weekday_slide_part_2 = year % 7
    leap_year_100 = int(year / 100)
    leap_year_400 = int(leap_year_100 / 4)
    lunar_orbit_correction = (int((13 + 8 * leap_year_100) / 25))
    century_start = (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) % 30
    sunday_offset = (4 + leap_year_100 - leap_year_400) % 7
    days_added = (19 * lunar_year_cycle_position + century_start) % 30
    day_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7
    total_days_added = 22 + days_added + day_of_week_offset
    day_of_easter = int(total_days_added % 31)
    month_of_easter = 3 + (int(total_days_added / 31))
    return MonthAndDay(month_of_easter, day_of_easter)


if __name__ == '__main__':
    # m = Foo(11)
    # print(m.x)
    x = 10
    print(x.__class__)
    # year = int(input('enter year: '))
    # easter_date: MonthAndDay = get_easter(year)
    # print('In', year, 'Easter Sunday is on month', easter_date.month, 'and day', easter_date.day)

