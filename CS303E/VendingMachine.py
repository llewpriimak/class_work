# File: VendingMachine.py
#
# Description: CS303e programming assignment 13.
# Create a class that models a vending machine.
#
# Assignment Number: 13
#
# Name: Llewnouske Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


class VendingMachine:


    # This vending machine class will create the object that operates like a vending machine
    # The methods created here can be used like a real vending machine
    def __init__(self, init_drink, price_drink, machine_cap):
        self._initial_drinks = init_drink
        self._price_per_drink = price_drink
        self._machine_capacity = machine_cap
        self._current_transaction = 0
        self._machine_money = 0

    def insert_money(self, add_money):
        self._current_transaction += add_money

    def can_dispense_one_drink(self):

        if self._initial_drinks > 0 and self._current_transaction >= self._price_per_drink:
            return True
        else:
            return False

    def dispense_one_drink(self):
        give_drink = self.can_dispense_one_drink()
        if give_drink:
            self._initial_drinks -= 1
            self._machine_money += self._price_per_drink
            self._current_transaction -= self._price_per_drink
            return 'ENJOY'
        elif self._initial_drinks == 0:
            return 'EMPTY'
        elif not give_drink:
            return 'INSUFFICIENT FUNDS'

    def get_change(self):

        give_back = self._current_transaction
        self._current_transaction = 0
        return give_back

    def refill(self):

        self._initial_drinks = self._machine_capacity
        self._machine_money += self._current_transaction
        self._current_transaction = 0
        return self._machine_money


def main():


    """# Run a simulation using the Vending Machine objects."""
    if input('Run simple tests? ') == 'y':
        simple_tests()
    stress_tests()


def simple_tests():


    """Simple operations with a single Vending Machine.

     The VendingMachine has a capacity of 5 drinks, currently
     has 2 drinks, and it costs 50 cents per drink.
     """
    print('***** SIMPLE TESTS *****')
    vend1 = VendingMachine(2, 50, 5)
    vend1.insert_money(25)
    vend1.insert_money(10)
    vend1.insert_money(10)
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect False')
    print('dispense:', vend1.dispense_one_drink(), '-- expect INSUFFICIENT FUNDS')
    vend1.insert_money(10)
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect True')
    print('dispense:', vend1.dispense_one_drink(), '-- expect ENJOY')
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect False')
    print('get change:', vend1.get_change(), '-- expect 5')
    print('get change:', vend1.get_change(), '-- expect 0')
    vend1.insert_money(100)
    vend1.insert_money(25)
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect True')
    print('dispense:', vend1.dispense_one_drink(), '-- expect ENJOY')
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect False')
    print('dispense:', vend1.dispense_one_drink(), '-- expect EMPTY')
    money_collected = vend1.refill()
    print('Money collected when machine refilled:', money_collected,
          '-- expect 175')
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect False')
    print('dispense:', vend1.dispense_one_drink(), '-- expect INSUFFICIENT FUNDS')
    vend1.insert_money(50)
    vend1.insert_money(25)
    vend1.insert_money(5)
    vend1.insert_money(10)
    vend1.insert_money(5)
    vend1.insert_money(50)
    print('can dispense:', vend1.can_dispense_one_drink(), '-- expect True')
    print('dispense:', vend1.dispense_one_drink(), '-- expect ENJOY')
    print('dispense:', vend1.dispense_one_drink(), '-- expect ENJOY')
    print('get change:', vend1.get_change(), '-- expect 45')
    print()


def stress_tests():


    """Run stress tests.

    Given the same number of machines, the same number of operations,
    and the same initial seed, output will be the same.
    """
    # Get the seed, number of operations,
    # and number of machines from the user.
    random.seed(int(input('Enter random seed: ')))
    num_operations = int(input('Enter the number of operations: '))
    num_machines = int(input('Enter the number of machines: '))
    print('\n***** STRESS TESTS *****')

    # Create the required number of machines and run the tests.
    machines = create_machines(num_machines, 10)
    perform_stress_tests_ops(machines, num_operations)


def perform_stress_tests_ops(machines, num_operations):


    """# Run the actual operations for the stress tests."""
    # Only allow US coins, excluding pennies!
    # (We should get rid of pennies and probably nickels too!)
    coins = [5, 10, 25, 50, 100]
    last_coin_index = len(coins) - 1
    last_machine_index = len(machines) - 1

    # Pick a random operation.
    # 55% chance of insert_money.
    # 20% chance of can dispense one drink.
    # 21% chance of dispense one drink. (If we dispense, there is an 80%
    #       chance dispense is called directly after.)
    #  3% chance of get_change.
    #  1% chance of refill.
    for i in range(1, num_operations + 1):
        print('Operation =', i)
        machine_number = random.randint(0, last_machine_index)
        print('Machine =', machine_number)
        machine = machines[machine_number]

        random_op = random.randint(1, 100)
        if random_op <= 55:
            coin = coins[random.randint(0, last_coin_index)]
            print('Insert money, amount =', coin)
            machine.insert_money(coin)
        elif random_op <= 75:
            print('Can dispense:', machine.can_dispense_one_drink())
        elif random_op <= 96:
            result = machine.dispense_one_drink()
            print('Dispense:', result)
            if result == 'ENJOY':
                # Do they remember their change? 80% chance of yes.
                if random.randint(1, 5) <= 4:
                    print('Get change, amount =', machine.get_change())
                else:
                    print('Forgot change after dispense.')
        elif random_op <= 99:
            print('Get change, amount =', machine.get_change())
        else:
            print('Refill. ', end='')
            money_collected = machine.refill()
            print('Money collected when refilled: ' + str(money_collected))
        print()


def create_machines(num_machines, max_capacity):


    """Create a list with the required number of machines.

    I -- expect num_machines > 0.
    The first machine always has a price of 25, 1 drink,
    and a capacity of 3.
    All machines will have a price between
    25 and 200 in multiples of 25.
    All machines will have a capacity between 2 and max_capacity.
    """
    price_multiplier = 25
    machines = [VendingMachine(1, price_multiplier, 3)]
    print('Machine 0: price = 25, capacity = 3, initial drinks = 1')
    for i in range(1, num_machines):
        price = random.randint(1, 8) * price_multiplier
        capacity = random.randint(2, max_capacity)
        drinks = random.randint(0, capacity)
        print('Machine ', i, ': price = ', price, ', capacity = ', capacity,
              ', initial drinks = ', drinks, sep='')
        machines.append(VendingMachine(drinks, price, capacity))
    print()
    return machines


main()
