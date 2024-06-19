
def get_report(resources_available: dict):
    print("Resources:")
    print(f"Water: {resources_available['water']}")
    print(f"Milk: {resources_available['milk']}")
    print(f"Coffee: {resources_available['coffee']}")


def sufficient_resources(menu_item: str, complete_menu: dict, complete_resources: dict):
    for resource in complete_resources:
        if complete_menu[menu_item][resource] < complete_resources[resource]:
            print(f"Insufficient {resource}")
            print(f"{resource} required: {complete_menu[menu_item][resource]}")
            print(f"{resource} available: {complete_resources[resource]}")
            return False

    return True

def dispense(item: str, complete_menu: dict, complete_resources: dict, coins: dict)->None:

   if not sufficient_resources(item, complete_menu, complete_resources):
       return

   cashier(coins, complete_menu[item]["cost"])


def cashier(coins: dict, item_cost: int)->None:

    user_payment: float = 0

    print("Please insert coins.")

    for coin in coins:
        coin_amount = int(input(f"How many {coin}:"))
        user_payment += coins[coin] * coin_amount



    print(f"User payed: {user_payment}")
    print(f"Here is your ${user_payment-item_cost} in change.")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


while True:

    user_choice = input("What would you like? (espresso/latte/cappuccino)").lower()

    if user_choice == 'report':
        get_report(resources)
        continue
    elif user_choice == 'off':
        break

    dispense(user_choice,MENU,resources,coins_value)

print("Thank you, please come back soon")
exit()




