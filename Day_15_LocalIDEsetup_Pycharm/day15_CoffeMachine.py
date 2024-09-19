
def get_report(resources_available: dict, money_stored: float):
    print("Resources:")
    print(f"Water: {resources_available['water']}ml")
    print(f"Milk: {resources_available['milk']}ml")
    print(f"Coffee: {resources_available['coffee']}g")
    print(f"Money: ${money_stored:.2f}")


def sufficient_resources(menu_item: str, complete_menu: dict, complete_resources: dict):

    for resource in complete_menu[menu_item]["ingredients"]:
        if complete_menu[menu_item]["ingredients"][resource] > complete_resources[resource]:
            print(f"Insufficient {resource}")
            print(f"{resource} required: {complete_menu[menu_item]['ingredients'][resource]}")
            print(f"{resource} available: {complete_resources[resource]}")
            return False

    return True


def update_resources(complete_resources: dict, item_resources: dict, item: str) -> dict:
    for resource in item_resources:
        complete_resources[resource] -= item_resources[resource]

    return complete_resources


def dispense(item: str, complete_menu: dict, complete_resources: dict, coins: dict) -> dict:

    if not sufficient_resources(item, complete_menu, complete_resources):
        return {"resources": complete_resources,
                'money': 0,
                }

    if not cashier(coins, complete_menu[item]["cost"], item):
        return {"resources": complete_resources,
                'money': 0,
                }

    print(f"Here is you {item}. Enjoy!")

    return {"resources": update_resources(complete_resources, complete_menu[item]["ingredients"], item),
            'money': complete_menu[item]["cost"]
            }


def cashier(coins: dict, item_cost: int, item_name: str) -> bool:

    user_payment: float = 0
    print(f"Your {item_name} costs: ${item_cost}")
    print("Please insert coins.")

    for coin in coins:
        print(f"${user_payment} / ${item_cost} ")
        coin_amount = int(input(f"How many {coin} (${coins[coin]}):"))
        user_payment += coins[coin] * coin_amount

    if user_payment < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    print(f"You payed: ${user_payment:.2f}")
    print(f"Here is your ${user_payment-item_cost:.2f} in change.")
    return True


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

money: float = 0

while True:

    user_choice = input("What would you like? (espresso/latte/cappuccino):\n ").lower()

    if user_choice == "off":
        break

    if user_choice == "report":
        get_report(resources, money)
        continue

    if user_choice not in MENU:
        continue

    resources_after_transaction = dispense(user_choice, MENU, resources, coins_value)
    resources = resources_after_transaction["resources"]
    money += resources_after_transaction["money"]


print("Thank you, please come back soon")
exit()




