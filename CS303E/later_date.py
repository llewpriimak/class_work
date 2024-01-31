# File: later_date.py
# Description: This is a program that will skip days after a given date
# Assignment Number: 5
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():


    # This function will tell the user a date that is based on the starting date and days skipped
    print('This program asks for a date and days to skip.')
    print('It then displays the date that many days after the given date.')
    print()

    # This makes adds a space in the output
    month = input('Enter the month: ')
    day_of_month = int(input('Enter the day of the month: '))
    year = int(input('Enter the year: '))
    print()
    skip_days = int(input('Enter the number of days to skip: '))
    print()
    leap_year_true = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    new_year = year

    # Skips the month and finds new day of month
    if month == 'January' and 32 <= (day_of_month + skip_days):
        new_month = 'February'
        month_difference = 31 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'February' and 30 <= (day_of_month + skip_days) and leap_year_true:
        new_month = 'March'
        month_difference = 29 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'February' and leap_year_true == True:
        new_day_of_month = day_of_month + skip_days
        new_month = month
    elif month == 'February' and 29 <= (day_of_month + skip_days):
        new_month = 'March'
        month_difference = 28 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'March' and 32 <= (day_of_month + skip_days):
        new_month = 'April'
        month_difference = 31 - day_of_month
        new_day_of_month= skip_days - month_difference
    elif month == 'April' and 31 <= (day_of_month + skip_days):
        new_month = 'May'
        month_difference = 30 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'May' and 32 <= (day_of_month + skip_days):
        new_month = 'June'
        month_difference = 31 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'June' and 31 <= (day_of_month + skip_days):
        new_month = 'July'
        month_difference = 30 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'July' and 32 <= (day_of_month + skip_days):
        new_month = 'August'
        month_difference = 31 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'August' and 32 <= (day_of_month + skip_days):
        new_month = 'September'
        month_difference = 31 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'September' and 31 <= (day_of_month + skip_days):
        new_month = 'October'
        month_difference = 30 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'October' and 32 <= (day_of_month + skip_days):
        new_month = 'November'
        month_difference = 31 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'November' and 31 <= (day_of_month + skip_days):
        new_month = 'December'
        month_difference = 30 - day_of_month
        new_day_of_month = skip_days - month_difference
    elif month == 'December' and 32 <= (day_of_month + skip_days):
        new_month = 'January'
        new_year = new_year + 1
        month_difference = 31 - day_of_month
        new_day_of_month = skip_days - month_difference
    else:
        new_day_of_month = day_of_month + skip_days
        new_month = month

    # This makes the skip day plural or not
    if skip_days != 1:
        print(f'{skip_days} days after {month} {day_of_month}, {year} is {new_month} {new_day_of_month}, {new_year}.')
    else:
        print(f'{skip_days} day after {month} {day_of_month}, {year} is {new_month} {new_day_of_month}, {new_year}.')


main()
