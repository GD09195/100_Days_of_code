from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_CoffeMaker = CoffeeMaker()
my_MoneyMachine = MoneyMachine()

while True:

    user_order = input(f"What would you like? ({my_menu.get_items()}):").lower()

    if user_order == 'off':
        break
    if user_order == 'report':
        my_CoffeMaker.report()
        my_MoneyMachine.report()
        continue

    drink = my_menu.find_drink(user_order)

    if not my_CoffeMaker.is_resource_sufficient(drink):
        print("Sorry there are not enough resources")
        continue


exit()
