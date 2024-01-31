# File: dice.py
# Description: This program runs a simplified version of the game craps
# Assignment Number: 6
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

def main():
    print('This program simulates the dice game of craps.')
    seed = int(input('Enter an int for the initial seed: '))


    random.seed(seed)
    dice_total = (random.randint(1, 6) + random.randint(1, 6))
    point = dice_total
    roll_again = True
    print(dice_total)


    if dice_total == 7 or dice_total == 11:
        print('Congratulations you have won on the first roll!')
        roll_again = False
    elif dice_total == 2 or dice_total == 3 or dice_total == 12:
        print('Im sorry you have lost on the first roll!')
        roll_again = False
    else:
        print('Roll again')

    while roll_again:
        print(dice_total, end = '')
        if point == 7:
            print('Im sorry you lose')
            roll_again = False
        elif point == dice_total:
            print ('Congratulations you win!')
            roll_again = False
        else:
            roll_again = True
            dice_total = (random.randint(1, 6) + random.randint(1, 6))


    #seed_check = input('Do you want to set the seed? Enter y for yes, anything else for no: ')
    #total_rounds = int(input('Enter the number of rounds to run: '))


main()

if point == 7 and rule_set == False:
            round_count += 1
            rule_set = True
            #print('end 4')
        elif point == dice_total and rule_set == False:
            #print('end 5')
            round_count += 1
            victory_tracker += 1
            rule_set = True
        else:
            rule_set = False
