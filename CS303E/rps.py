# File: rps.py
# Description: This program pits a human against a computer in ROCK PAPER SCISSORS
# Assignment Number: 7
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


    # The function takes in what the player wants to do and runs the game
    print('Welcome to ROCK PAPER SCISSORS. I, Computer, will be your opponent.')
    player_name, total_rounds = get_input()
    wins = 0
    round_number = 1
    # This while loop will play the total rounds until complete
    while round_number <= total_rounds:

        print()
        print(f'--- Round {round_number} ---')
        print(f'{player_name}, enter your choice for this round.')
        wins += rock_paper_scissors()
        round_number += 1

    print()
    if total_rounds == 1:
        print(f'We played {total_rounds} round of ROCK PAPER SCISSORS.')
    else:
        print(f'We played {total_rounds} rounds of ROCK PAPER SCISSORS.')
    if wins == 1:
        print(f'{player_name} won {wins} round.')
    else:
        print(f'{player_name} won {wins} rounds.')
    print('Well played.')


def get_input():


    # This function will get all the players inputs
    print('--- INITIAL INPUT ---')
    player_name = (input('Please enter your name: '))
    print('Thank you!')
    print()
    print('--- INITIAL INPUT ---')
    total_rounds = (int(input('Please enter the number of rounds to play: ')))
    print('Thank you!')
    print()
    print('--- INITIAL INPUT ---')
    seed_check = input('Please enter y if you want to set the seed: ')
    print('Thank you!')
    print()
    if seed_check == 'y':
        print('--- INITIAL INPUT ---')
        seed = int(input('Please enter an integer for the seed: '))
        print('Thank you!')
        random.seed(seed)

    return player_name, total_rounds


def rock_paper_scissors():


    # This function plays the human and computer moves
    player_move = input('R for Rock, P for Paper, S for Scissors: ')

    if player_move == 'R':
        player_move = 1
    elif player_move == 'P':
        player_move = 2
    else:
        player_move = 3

    computer_roll = random.randint(1, 3)
    if computer_roll == 1:
        print('I pick Rock.')
    elif computer_roll == 2:
        print('I pick Paper.')
    else:
        print('I pick Scissors.')

    return result_printer(computer_roll, player_move)


def result_printer(x, y):


    # Result printer will give the outcome of the round
    wins = 0
    if x == y:
        print('We picked the same thing. Round is a draw.')
    elif x == 1 and y == 2:
        print('Paper covers Rock. You win.')
        wins += 1
    elif x == 1 and y == 3:
        print('Rock breaks Scissors. I win.')
    elif x == 2 and y == 1:
        print('Paper covers Rock. I win.')
    elif x == 2 and y == 3:
        print('Scissors cut Paper. You win.')
        wins += 1
    elif x == 3 and y == 1:
        print('Rock breaks Scissors. You win.')
        wins += 1
    elif x == 3 and y == 2:
        print('Scissors cut Paper. I win.')

    return wins


main()
