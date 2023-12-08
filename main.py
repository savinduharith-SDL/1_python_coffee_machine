import time

from resouces import MENU, resources
from constants import COIN_VALUES

is_machine_on = True
wallet = 0
selected_coffee = ""


def get_user_choice():
    global selected_coffee
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "espresso":
        selected_coffee = "espresso"
        return MENU["espresso"]
    elif choice.lower() == "latte":
        selected_coffee = "latte"
        return MENU["latte"]
    elif choice.lower() == "cappuccino":
        selected_coffee = "cappuccino"
        return MENU["cappuccino"]
    elif choice.lower() == "off":
        turn_machine_off()
        return False
    elif choice.lower() == "report":
        print_report(wallet)
        return False
    else:
        print("Invalid command")
        return False


def turn_machine_off():
    global is_machine_on
    is_machine_on = False
    return


def print_report(current_money):
    print(
        f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ${current_money}")


def check_resource_availability(selected_coffee, current_resources):
    required_resources = selected_coffee['ingredients']
    if required_resources['water'] > current_resources['water']:
        print("Sorry there is not enough water")
        return False
    elif required_resources['coffee'] > current_resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    elif required_resources['milk'] > current_resources['milk']:
        print("Sorry there is not enough milk")
        return False
    else:
        return True


def process_coins(coffee):
    quarters = int(input("Enter the number of quaters : "))
    dimes = int(input("Enter the number of dimes : "))
    nickles = int(input("Enter the number of nickles : "))
    pennies = int(input("Enter the number of pennies : "))
    total_coin_value = COIN_VALUES['quarters'] * quarters + COIN_VALUES['dimes'] * dimes + COIN_VALUES[
        'nickles'] * nickles + COIN_VALUES['pennies'] * pennies
    required_cost = MENU[coffee]["cost"]
    if total_coin_value >= required_cost:
        global wallet
        wallet += required_cost
        print(f"The remainder is : {total_coin_value - required_cost}")
        return True
    else:
        print(
            f"For the {coffee} you have to put the coins worth ${required_cost}.\n\nShortage : ${total_coin_value - required_cost}\n\nReturning ${total_coin_value}")
        return False


def make_coffee(coffee):
    print("Coffee is on the way ! ...")
    ingredient_list = ["water", "milk", "coffee"]
    for ingredient in ingredient_list:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
    for i in range(1, 4):
        print(...)
        time.sleep(1)
    print(f"Here is your {coffee}")


def process_coffee_request():
    global selected_coffee
    coffee_info = get_user_choice()
    if coffee_info:
        if check_resource_availability(coffee_info, resources):
            if process_coins(selected_coffee):
                make_coffee(selected_coffee)

while(is_machine_on):
    process_coffee_request()
