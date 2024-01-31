# File: team_wins.py
# Description: This program will give the wins, losses and win % for a sports team
# of a certain season
# Assignment Number: 8
#
# Name: Llewnosuke Priimak
# EID: lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.
import os


def main():


    # This main function will open a data file based on a users input.
    print('This program reads a file for a sport\'s teams results.')
    file_name = input('Enter file name: ')

    # calls a different function depending the users input
    if os.path.isfile(file_name):
        wins, losses = run_game(file_name)
        win_percentage(wins, losses)
    else:
        print(f'{file_name} does not exist. Ending program.')


def run_game(file):


    #This function will give wins and losses for a sports team
    get_team = input('Enter team name: ')
    get_file = open(file, 'r')
    line_check = get_file.readline().strip()
    wins = 0
    losses = 0

    # While loop will vet through the file of game scores
    while line_check != '':

        team_1 = get_file.readline().strip()
        team_1_score = int(get_file.readline())
        team_2 = get_file.readline().strip()
        team_2_score = int(get_file.readline())
        line_check = get_file.readline().strip()

        if team_1 == get_team:
            win_plus, loss_plus = win_loss(team_1_score, team_2_score)
            wins += win_plus
            losses += loss_plus

        elif team_2 == get_team:
            win_plus, loss_plus = win_loss(team_2_score, team_1_score)
            wins += win_plus
            losses += loss_plus

    if wins + losses == 0:
        print(f'{get_team} did not appear in any games.')

    get_file.close()
    return wins, losses


def win_loss(x, y):


    # This function will track the number of wins and losses
    wins = 0
    loss = 0
    if x > y:
        wins += 1
    else:
        loss += 1

    return wins, loss


def win_percentage(wins, losses):


    # This function will calculate the win percentage
    win_percentage = 0
    if wins + losses != 0:
        win_percentage = (wins / (wins + losses)) * 100
        print(f'wins: {wins}')
        print(f'losses: {losses}')
        print(f'win percentage: {win_percentage:.1f}')

    elif losses > wins:
        print(f'win percentage: {win_percentage:.1f}')


main()
