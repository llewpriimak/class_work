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

def main(): #This function will tell you the day of the week when inputting a date

    month_input = input('Enter the month (for example, January, February, etc.): ')

    day_in_month = int(input('Enter the day (an integer): '))
    year = int(input('Enter the year (an integer): '))

    # This will convert the month to an integer value
    if month_input == 'January':
        month_number = 13
        year = year - 1
    elif month_input == 'February':
        month_number = 14
        year = year - 1
    elif month_input == 'March':
        month_number = 3
    elif month_input == 'April':
        month_number = 4
    elif month_input == 'May':
        month_number = 5
    elif month_input == 'June':
        month_number = 6
    elif month_input == 'July':
        month_number = 7
    elif month_input == 'August':
        month_number = 8
    elif month_input == 'September':
        month_number = 9
    elif month_input == 'October':
        month_number = 10
    elif month_input == 'November':
        month_number = 11
    elif month_input == 'December':
        month_number = 12

    #Inputs alogorithm
    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = (year // 4) + (year // 400)
    century_days = year // 100
    total_days = (day_in_month + variation_in_days_per_month + year + leap_year_days - century_days)
    day_of_week = total_days % 7

    if day_of_week == 0:
        print('The day of the week is Saturday.')
    elif day_of_week == 1:
        print('The day of the week is Sunday.')
    elif day_of_week == 2:
        print('The day of the week is Monday.')
    elif day_of_week == 3:
        print('The day of the week is Tuesday.')
    elif day_of_week == 4:
        print('The day of the week is Wednesday.')
    elif day_of_week == 5:
        print('The day of the week is Thursday.')
    else:
        print('The day of the week is Friday.')

main()
