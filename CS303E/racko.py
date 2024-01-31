# File: racko.py
# Description: A program that simulates the card and number game
# Rack-O. Players use the keyboard and take turns.
# Assignment Number: 9
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


    """Play one game of Rack-O."""
    # Get the rack size, create the deck, and deal the initial racks.
    rack_size = prep_game()
    deck = list(range(1, 61))
    random.shuffle(deck)
    player_1_rack = get_rack(deck, rack_size)
    player_2_rack = get_rack(deck, rack_size)
    discard = [deck.pop(0)]
    if is_sorted(player_1_rack):
        print('Player 1 wins!')
    elif is_sorted(player_2_rack):
        print('Player 2 wins!')
    else:
        another_round = True
        switch_player = True
        # This while loop will play the turns of the game and
        # check for a winner
        while another_round:

            if len(deck) == 0:
                print('Deck is empty. Shuffling discard pile')
                deck = random.shuffle(discard)
                discard = [deck.pop(0)]
            if switch_player == True:
                print('Player 1\'s turn.')
                deck, discard, player_1_rack = take_turn(deck, discard, player_1_rack)
                if is_sorted(player_1_rack):
                    another_round = False
                    print('Player 1 wins!')
                else:
                    switch_player = False
            else:
                print('Player 2\'s turn.')
                deck, discard, player_2_rack = take_turn(deck, discard, player_2_rack)
                if is_sorted(player_2_rack):
                    another_round = False
                    print('Player 2 wins!')
                else:
                    switch_player = True


def prep_game():


    """Get ready to play 1 game.

    Show the instructions if the user wants to see them.
    Set the seed for the random number generator.
    Return the size of the rack to use.
    """
    # This function will set the rack size to start the game
    # as well as provide instructions
    print('----- Welcome to Rack - O! -----')
    if input('Enter y to display instructions: ') == 'y':
        instructions()
    print()
    random.seed(int(input('Enter number for initial seed: ')))
    rack_size = int(input('Enter the size of the rack to use. '
                          + 'Must be between 5 and 10: '))
    while not 5 <= rack_size <= 10:
        print(rack_size, 'is not a valid rack size.')
        rack_size = int(input('Enter the size of the rack to use. '
                              + 'Must be between 5 and 10: '))
    print()
    return rack_size


def instructions():


    """Print the instructions of the game."""
    print()
    print('The goal of the game is to get the cards in your rack of cards')
    print('into ascending order. Your rack has ten slots numbered 1 to 10.')
    print('During your turn you can draw the top card of the deck or take')
    print('the top card of the discard pile.')
    print('If you draw the top card of the deck, you can use that card to')
    print('replace a card in one slot of your rack. The replaced card goes to')
    print('the discard pile.')
    print('Alternatively you can simply choose to discard the drawn card.')
    print('If you take the top card of the discard pile you must use it to')
    print('replace a card in one slot of your rack. The replaced card goes')
    print('to the top of the discard pile.')


def take_turn(deck, discard, player_rack):


    """Take the player's turn.

    Give them the choice of drawing or taking the top card of the
    discard pile. If they draw they can replace a card or discard the
    draw. If they take the top card of the discard pile they must
    replace a card in their rack.
    """
    # This function will give the player their rack and top of discard pile
    # It then will give options to how to change your cards
    print(f'Your current rack  {player_rack}')
    print(f'Top of discard pile  {(discard[0])}' )
    if input('Enter d to draw anything else to take top of discard pile: ') == 'd':
        new_card = deck.pop(0)
        print()
        print(f'drew the {new_card}')
        if input('Enter p to place card, anything else to discard it: ') == 'p':
            discard, player_rack = place_card(player_rack, new_card, discard)
        else:
            discard.insert(0, new_card)
            print(f'The rack after the turn  {player_rack}')
            print()

    else:
        print()
        new_card = discard.pop(0)
        discard, player_rack = place_card(player_rack, new_card, discard)


    return deck, discard, player_rack


def place_card(player_rack, new_card, discard):


    """Ask the player which card to replace in their rack.

    Replace it with the given new card. Place the card removed
    from the player's rack at the top of the discard pile.
    Error checks until player enters a card that is currently
    in their rack.
    """
    # This function will allow you to choose which card in your hand to replace
    replace_card = int(input(f'Enter the card number to replace with the {new_card}: '))
    while replace_card not in player_rack:
        print(f'{replace_card} is not in your rack.')
        replace_card = int(input(f'Enter the card number to replace with the {new_card}: '))
    replace_index = player_rack.index(replace_card)
    player_rack[replace_index] = new_card
    print(f'The rack after the turn  {player_rack}')
    print()
    discard.insert(0, replace_card)

    return discard, player_rack


def is_sorted(rack):


    """Return if this rack is sorted in ascending order.

    CS303e assignment limitation:
    Do not create any new lists in this function.
    """
    # This function just checks to see if a players hand is sorted or not
    card_check = 0
    rack_check = 0

    for card in range(len(rack) - 1):

        if rack[card_check] < rack[card_check + 1]:
            rack_check += 1
        card_check += 1

    if rack_check == (len(rack) - 1):
        return True
    else:
        return False


def get_rack(deck, rack_size):


    """Deal the top rack_size cards of the deck into a new rack.

    The first card goes in the first slot, the second card goes in
    the second slot, and so forth. We assume len(deck) >= rack_size.
    Return the list of ints representing the rack.
    """
    # This function will give the player their starting hand
    player_rack = []
    for i in range(0, rack_size):
        next_card = deck.pop(0)
        player_rack.append(next_card)

    return player_rack


main()
