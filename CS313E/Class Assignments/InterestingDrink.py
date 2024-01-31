#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of black tea in each store, and a list of integers named money that contains the amount of money
#               Tim will spend in a given day, returns a list of integers representing how many different shops
#               Tim can buy a cup of black tea.

#  Student Name: Llewnosuke Priimak

#  Student UT EID: lp27636

#  Course Name: CS 313E

#  Unique Number:52020

import sys


# A binary search implementation
def binary_search (a, x):
  lo = -1
  hi = len(a)
  while lo < hi - 1:
    mid = (lo + hi) // 2
    if a[mid] <= x:
      lo = mid
    else:
        hi = mid
  return lo

# Input: prices a list of integers containing the price of black tea in each store
#        money  a list of integers containing the amount of money Tim will spend in a given day
# Returns: a list of integers representing how many different shops Tim can buy a cup of black tea.
def find_purchase_options(prices, money):

    prices.sort()
    can_get = []
    for cash in money:
        total = 0
        for price in prices:
            if cash >= price:
                total += 1
            else:
                break
        can_get.append(total)
    return can_get

#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
