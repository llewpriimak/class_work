#Llewnosuke Priimak vending machine program
#EID lp27636



class Milk:

    def get_calories(self):
        return 10
    def get_price(self):
        return 1
    def get_lactose_content(self):
        return 5

class Sugar:

    def get_calories(self):
        return 10
    def get_price(self):
        return 1
    def get_lactose_content(self):
        return 0

class Coffee:
    def get_calories(self):
        pass
    def get_price(self):
        pass
    def get_lactose_content(self):
        pass

class Tea:
    def get_calories(self):
        pass
    def get_price(self):
        pass
    def get_lactose_content(self):
        pass

class Espresso(Coffee):
    def get_calories(self):
        return 40
    def get_price(self):
        return 3
    def get_lactose_content(self):
        return 0

class Americano(Coffee):
    def get_calories(self):
        return 50
    def get_price(self):
        return 2
    def get_lactose_content(self):
        return 0

class LatteMacciato(Coffee):
    def get_calories(self):
        return 60
    def get_price(self):
        return 4
    def get_lactose_content(self):
        return 5

class BlackTea(Tea):
    def get_calories(self):
        return 20
    def get_price(self):
        return 3
    def get_lactose_content(self):
        return 0

class GreenTea(Tea):
    def get_calories(self):
        return 20
    def get_price(self):
        return 3
    def get_lactose_content(self):
        return 0

class YellowTea(Tea):
    def get_calories(self):
        return 25
    def get_price(self):
        return 3
    def get_lactose_content(self):
        return 0

class VendingMachine:

    def request_drink(self):

        print('We have Espresso, Americano, Latte Machiato, Black Tea, Green Tea, and Yellow Tea')
        dispense = input('Would you like a drink? Y for yes N for no: ')
        if dispense == 'Y':
            print(f'Press 1 for Espresso, 2 for Americano, 3 for Latte Machiato, 4 for black tea, 5 for green tea, and 6 for yellow Tea')
            beverage_wishes = int(input('What beverage would you like: '))
            while beverage_wishes > 6:
                print("Please select 1 through 6")
                beverage_wishes = int(input('What beverage would you like: '))
        return beverage_wishes

    def request_milk(self):
        get_milk = int(input('How much milk would you like in your beverage? 0 - 3: '))
        while get_milk > 3 or get_milk < 0:
            print('Please select an amount')
            get_milk = int(input('How much milk would you like in your beverage? 0 - 3: '))
        my_milk = Milk()
        milk_calories = my_milk.get_calories()
        milk_price = my_milk.get_price()
        milk_lactose = my_milk.get_lactose_content()
        return milk_calories, milk_price, milk_lactose

    def request_sugar(self):
        get_sugar = int(input('How much sugar would you like in your beverage? 0 - 3: '))
        while get_sugar > 3 or get_sugar < 0:
            print('Please select an amount')
            get_sugar = int(input('How much sugar would you like in your beverage? 0 - 3: '))
        my_sugar = Sugar()
        sugar_calories = my_sugar.get_calories()
        sugar_price = my_sugar.get_price()
        sugar_lactose = my_sugar.get_lactose_content()
        return sugar_calories, sugar_price, sugar_lactose

    def mix_drink(self, beverage_wishes, milk_calories, milk_price, milk_lactose,sugar_calories, sugar_price, sugar_lactose):

        if beverage_wishes == 1:
            your_drink = Espresso()
        elif beverage_wishes == 2:
            your_drink = Americano()
        elif beverage_wishes == 3:
            your_drink = LatteMacciato()
        elif beverage_wishes == 4:
            your_drink = BlackTea()
        elif beverage_wishes == 5:
            your_drink = GreenTea()
        elif beverage_wishes == 6:
            your_drink = YellowTea()
        else:
            (f'Please choose a drink option')
        calories = your_drink.get_calories() + milk_calories + sugar_calories
        price = your_drink.get_price() + milk_price + sugar_price
        lactose = your_drink.get_lactose_content() + milk_lactose + sugar_lactose
        return calories, price, lactose

    def give_drink(self, beverage, calories, price, lactose):
        if beverage == 1:
            your_drink = 'Espresso'
        elif beverage == 2:
            your_drink = 'Americano'
        elif beverage == 3:
            your_drink = 'LatteMacciato'
        elif beverage == 4:
            your_drink = 'BlackTea'
        elif beverage == 5:
            your_drink = 'GreenTea'
        elif beverage == 6:
            your_drink = 'Yellow Tea'
        print (f'Here is your {your_drink},it is ${price}, has {calories} calories, and {lactose} grams of lactose')


### Interface ###
def machine_interface():
        again = 1
        while again == 1:
            vending_machine = VendingMachine()
            beverage = vending_machine.request_drink()
            milk_calories, milk_price, milk_lactose = vending_machine.request_milk()
            sugar_calories, sugar_price, sugar_lactose = vending_machine.request_sugar()
            calories, price, lactose= vending_machine.mix_drink(beverage,milk_calories, milk_price, milk_lactose,sugar_calories, sugar_price, sugar_lactose)
            vending_machine.give_drink(beverage, calories, price, lactose)
            again = int(input('1 for another drink:'))


machine_interface()
