# File: movies.py
# Description: Determine average rating for movie reviews
# that contains a given word. Words can be entered by the
# user or read from files.
# Assignment Number: 10
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.

import os


def main():


    """Read the main data file and run the menu loop."""
    # This main function will find the users choice and call another function
    # based on that
    print('Welcome to the movie sentiment program.')
    print('Enter a word to see the average rating of movies with that word.')
    file_name = input('Enter file name with reviews: ')
    reviews = get_reviews(file_name)
    choice = get_choice()


    # List of our functions. They all take a single parameter,
    # the reviews.
    functions = [print_word_sentiment, print_sentiments_from_file,
                 print_longest_review, print_shortest_review]

    while '1' <= choice <= '4':
        # Get the index of the function to call.
        index = ord(choice) - ord('1')
        functions[index](reviews)
        choice = get_choice()


def get_choice():


    # This shows the options
    """Display the menu and get the users choice.

    Returns the user's choice as a String.
    """
    print()
    print('OPTIONS:')
    print('1. See average rating for a word.')
    print('2. Show average reviews for all words in a file.')
    print('3. See the longest review.')
    print('4. See the shortest review.')
    result = input('Please enter your choice: ')
    print()
    return result


def get_reviews(file_name):


    """Given the file name, return a list of lists with the reviews.

    We expect one review per line. The first element will be an int [0, 4].
    The rest of the line shall be the review.
    All letters in the reviews are converted to lower case.
    """
    # This function will manipulate the txt file into a list of lists
    review_list = []
    with open(file_name, 'r') as reviews:

        read_review = reviews.readline().strip()

        while read_review != '':
            read_review = read_review.lower()
            review_list.append(read_review.split())
            read_review = reviews.readline().strip()

    return review_list


def print_word_sentiment(reviews):


    """Get a word from the user.

     Determine the average rating of reviews that contain that word.
     reviews is a list of lists that contains the reviews.
     We assume the user types in a word with no spaces although the
     word can contain non letters, but no spaces.
    """
    # Function will find the number of times the user inputed
    # words appears in the reviews
    word_count = 0
    rating_count = 0
    total_rating = 0
    get_word = input('Enter the word to search for: ')

    for review_element in reviews:
        if get_word.lower() in review_element[1:]:
            total_rating += int(review_element[0])
            rating_count += 1
            word_count += 1

    rating_output(rating_count, total_rating, get_word)


def print_sentiments_from_file(reviews):


    """Ask the user for the name of a file with words and phrases.

    We assume one word per line in the file.
    For each word in the file, determine and show
    the average rating of reviews that contain the given word.
    We assume there won't be any spaces in the file.
    """
    # This will find the number of occurrences of the words in a file
    # throughout all the reviews
    get_words = input('Enter file name with words to check: ')

    word_number = 1
    with open(get_words, 'r') as word_file:
        word_check = word_file.readline().strip()

        # This while loop will check for the words of a file
        # in the review list
        while word_check != '':

            word_count = 0
            rating_count = 0
            total_rating = 0
            print(f"Word number {word_number} is '{word_check}'. Results: ")

            for review_element in reviews:
                if word_check.lower() in review_element[1:]:
                    total_rating += int(review_element[0])
                    rating_count += 1
                    word_count += 1
            word_number += 1
            rating_output(rating_count, total_rating, word_check)
            print()
            word_check = word_file.readline().strip()


def print_longest_review(reviews):


    """Print information about the longest review."""
    # This will print out the longest review and how many words it has
    main_review = reviews[0]
    longest_review = len(reviews[0])
    for review_check in reviews:
        if len(review_check) > longest_review:
            main_review = review_check
            longest_review = len(review_check)

    print(f'Longest review has {longest_review - 1} words.')
    print(f'Review as list: {main_review[1:]}')


def print_shortest_review(reviews):


    """Print information about the shortest review."""
    # This will print the shortest review and how many words it has
    main_review = reviews[0]
    shortest_review = len(reviews[0])
    for review_check in reviews:
        if len(review_check) < shortest_review:
            main_review = review_check
            shortest_review = len(review_check)

    print(f'Shortest review has {shortest_review - 1} words.')
    print(f'Review as list: {main_review[1:]}')


def rating_output(rating_count, total_rating, word):


    #This will output a message based on the files
    if rating_count == 1:
        average_rating = (total_rating / rating_count)
        print(f'{word} appeared in {rating_count} review. '
              f'Average review score = {average_rating}', end = '')
        print()
    elif rating_count == 0:
        print(f'{word} did not appear in any reviews')
    else:
        average_rating = (total_rating / rating_count)
        print(f'{word} appeared in {rating_count} reviews. '
              f'Average review score = {average_rating}', end = '')
        print()


main()
