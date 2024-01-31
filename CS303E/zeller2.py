# File: zeller.py
# Description: <A DESCRIPTION OF YOUR PROGRAM>
# Assignment Number: 4
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.

def resolve_month(month, year):
    if month == 'January':
        return 13, (year - 1)
    elif month == 'February':
        return 14, (year - 1)
    elif month == 'March':
        return 3
    elif month == 'April':
        return 4, year
    elif month == 'May':
        return 5, year
    elif month == 'June':
        return 6, year
    elif month == 'July':
        return 7, year
    elif month == 'August':
        return 8, year
    elif month == 'September':
        return 9, year
    elif month == 'October':
        return 10, year
    elif month == 'November':
        return 11, year
    elif month == 'December':
        return 12, year
    else:
        print(f"Error: unable to recognize {month} as valid month. Sober up and do it again!")
        exit(-1)

def day_of_week_to_name(day_of_week):
    if day_of_week == 0:
        return "Saturday"
    elif day_of_week == 1:
        return "Sunday"
    elif day_of_week == 2:
        return "Monday"
    elif day_of_week == 3:
        return "Tuesday"
    elif day_of_week == 4:
        return "Wednesday"
    elif day_of_week == 5:
        return "Thursday"
    else:
        return "Friday"


def main(): #This function will tell you the day of the week when inputting a date

    month_input = input('Enter the month (for example, January, February, etc.): ')

    day_in_month = int(input('Enter the day (an integer): '))
    year = int(input('Enter the year (an integer): '))

    # This will convert the month to an integer value
    month_number, year = resolve_month(month_input, year)

    # Inputs algorithm
    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = (year // 4) + (year // 400)
    century_days = year // 100
    total_days = (day_in_month + variation_in_days_per_month + year + leap_year_days - century_days)
    day_of_week = total_days % 7

    day_of_week_name = day_of_week_to_name(day_of_week)
    print(f'The day of the week is {day_of_week_name}.')

main()
