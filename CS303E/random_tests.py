import os
class VendingMachine:

    def __init__(self, init_drink, price_drink, machine_cap):
        self.initial_drinks = init_drink
        self.price_per_drink = price_drink
        self.machine_capacity = machine_cap
        self.current_transaction = 0
        self.machine_money = 0

    def insert_money(self, add_money):
        self.current_transaction += add_money


    def can_dispense_one_drink(self):

        if self.initial_drinks > 0 and self.current_transaction >= self.price_per_drink:
            return True
        else:
            return False

    def dispense_one_drink(self):
        give_drink = self.can_dispense_one_drink()
        if give_drink:
            self.initial_drinks -= 1
            self.machine_money += self.price_per_drink
            self.current_transaction -= self.price_per_drink
            return 'ENJOY'
        elif self.initial_drinks == 0:
            return 'EMPTY'
        elif give_drink == False:
            return 'INSUFFICIENT FUNDS'

    def get_change(self):

        give_back = self.current_transaction
        self.current_transaction = 0
        return give_back


    def refill(self):

        self.initial_drinks = self.machine_capacity
        self.machine_money += self.current_transaction
        self.current_transaction = 0


def main():
    # file_length()
    file_test()


def file_test():
    with open('wbb12_e.txt', 'r') as file:
        for line in file:
            print(line)
            for char in line:
                print(char)

# def file_length():
#
#     file = input('Enter file to check how any lines: ')
#     line_count = 0
#     with open(file, 'r') as read_file:
#
#         line_check = read_file.readline().strip()
#
#         while line_check != '':
#             line_check = read_file.readline().strip()
#             line_count += 1
#     read_file.close()
#     print(f'This file has {line_count} lines')

main()
