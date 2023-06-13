# TODO ask for type of coffee
# TODO turn off the coffee machine
# TODO report
# TODO check resources
# TODO process coins
# TODO transaction status
# TODO make coffee

import static_data

resources = static_data.resources


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    if "money" in resources.keys():
        print(f"Money: ${resources['money']}")
    else:
        print(f"Money: $0")
    print()


def check_resources(ingredients):
    if ingredients["water"] > resources["water"]:
        print("There's not enough water to make you a drink!")
        return False
    if "milk" in ingredients and ingredients["milk"] > resources["milk"]:
        print("There's not enough milk to make you a drink!")
        return False
    if ingredients["coffee"] > resources["coffee"]:
        print("There's not enough coffee to make you a drink!")
        return False
    return True


def process_coins(money, coffee_type):
    if money < static_data.MENU[coffee_type]["cost"]:
        print(f"{coffee_type.title()} costs ${static_data.MENU[coffee_type]['cost']}. You still need "
              f"${round(static_data.MENU[coffee_type]['cost'] - money)} to purchase it. Your money has been refunded.")
        return False
    else:
        return True


def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    resources.pop("money")


def make_coffee(coffee_type, coins):
    ingredients = static_data.MENU[coffee_type]["ingredients"]
    money = coins["quarters"] * 0.25 + coins["dimes"] * 0.1 + coins["nickels"] * 0.05 + coins["pennies"] * 0.01

    if process_coins(money, coffee_type):
        if "money" in resources.keys():
            resources["money"] += money
        else:
            resources["money"] = money
    else:
        return

    if check_resources(ingredients):
        print(f"Your {coffee_type} will be ready soon! Here's your change: "
              f"${round(money - static_data.MENU[coffee_type]['cost'], 2)}")
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]
        print(f"Here's your {coffee_type}! \u2615")


def run_coffee_machine():
    todo = ""
    while todo != "off":
        todo = input(f"What would you like? \nespresso (${static_data.MENU['espresso']['cost']})"
                     f"\nlatte (${static_data.MENU['latte']['cost']})"
                     f"\ncappuccino (${static_data.MENU['cappuccino']['cost']})\n")
        if todo == "report":
            print_report()
        elif todo in ["espresso", "latte", "cappuccino"]:
            coins = {
                "quarters": int(input("How many quarters? ")),
                "dimes": int(input("How many dimes? ")),
                "nickels": int(input("How many nickels? ")),
                "pennies": int(input("How many pennies? "))
            }
            make_coffee(todo, coins)
        elif todo == "off":
            pass
        elif todo == "refill":
            refill()
        else:
            print("Please type a valid input!")


run_coffee_machine()
