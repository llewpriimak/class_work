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


    # This function will simulate multiple rounds of craps
    print('This program simulates the dice game of craps.')
    seed_check = input('Do you want to set the seed? Enter y for yes, anything else for no: ')
    seed = int(input('Enter an int for the initial seed: '))
    total_rounds = int(input('Enter the number of rounds to run: '))
    round_count = 0
    victory_tracker = 0
    final_max_roll = 0

    if seed_check == 'y':
        random.seed(seed)

    # This loop simulates the rounds of craps
    while round_count < total_rounds:
        dice_total = (random.randint(1, 6) + random.randint(1, 6))
        roll_count = 1
        round_count += 1

        # Initial Set of rules
        if dice_total == 7 or dice_total == 11:
            victory_tracker += 1
        elif dice_total == 2 or dice_total == 3 or dice_total == 12:
            victory_tracker += 0
        else:
            point = dice_total
            roll_count += 1
            new_roll = (random.randint(1, 6) + random.randint(1, 6))
            # second set of rules
            while new_roll != 7 and new_roll != point:
                new_roll = (random.randint(1, 6) + random.randint(1, 6))
                roll_count += 1
            if new_roll == point:
                victory_tracker += 1

        # This will track the max number of rolls
        max_roll = roll_count
        if max_roll >= final_max_roll:
            final_max_roll = max_roll

    if total_rounds < 0:
        total_rounds = 0
    if total_rounds == 1 and victory_tracker != 0:
        print(f'Player won {victory_tracker} time in {total_rounds} round.')
    elif victory_tracker == 1:
        print(f'Player won {victory_tracker} time in {total_rounds} rounds.')
    elif total_rounds == 1 and victory_tracker == 0:
        print(f'Player won {victory_tracker} times in {total_rounds} round.')
    else:
        print(f'Player won {victory_tracker} times in {total_rounds} rounds.')

    print(f'Maximum number of rolls in a round = {final_max_roll}')


main()


# 1. Yes this simulation does support the idea that in the long run casinos
# come out the winner. This is because the winrate in almost every simulation
# is less than 50%. If the winrate was greater than 50% the game would be favored
# by the player. Winning exactly 50% of the rounds would leave you coming out even.

# 2. Given that this game favors the casino it would be most likely that I would
# end up with less money than I started. For that reason I would not gamble the
# 2000$ on craps. Out of simulating 10 different 500 round games, I came up even
# on only one and loss on every other one.
