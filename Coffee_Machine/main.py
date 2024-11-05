from menu import MENU
import math

# Variables
coffee_menu = MENU
start_machine = True
money=[0]

def get_resources():
    resources = {"water": 300,"milk": 200,"coffee": 100}
    return resources
def is_resource_avilable(user_input,resources):
    for key in resources.keys():
       if resources[key] < coffee_menu[user_input]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True
    
def update_resources(resources, item):
    for key in resources.keys():
        resources[key] -= item["ingredients"][key]

def collect_coins():
    no_of_quarters = input("How many quarters? ")
    no_of_dimes = input("How many dimes? ")
    no_of_nickles = input("How many nickles? ")
    no_of_pennies = input("How many pennies? ")
    return [int(no_of_quarters),int(no_of_dimes), int(no_of_nickles), int(no_of_pennies)]

def calculate_amount(coins):
    amount = (0.25 * coins[0]) + (0.10 * coins[1]) + (0.05 * coins[2]) + (0.01 * coins[3])
    return round(amount,1)

def print_amount_left(left_amount):
    print(f"here is ${left_amount}  dollars in change.")

def transaction_successful(coins,item):
    total_amount = calculate_amount(coins)
    if total_amount >= item["cost"]:
        money[0] += item["cost"]
        change_left = total_amount - item["cost"]
        print_amount_left(round(change_left,2))
        return True
    return False
        




resources = get_resources()
def coffee_machine():
    while start_machine:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        report = resources
        if user_input == "report":
            print(report)
            print(f"Money: {money[0]}")
            coffee_machine()
        
        elif user_input == "espresso":
            if is_resource_avilable(user_input,report):
                coins = collect_coins()
                if transaction_successful(coins,coffee_menu[user_input]):
                    update_resources(report,coffee_menu[user_input])
                    print(f"Here is you {user_input} ☕️. Enjoy")
                else:
                    print("Sorry that's not enough money")
                    continue

            else:
                continue
                
        elif user_input == "latte":
            if is_resource_avilable(user_input,report):
                coins = collect_coins()
                if transaction_successful(coins,coffee_menu[user_input]):
                    update_resources(report,coffee_menu[user_input])
                    print(f"Here is you {user_input} ☕️. Enjoy")
                else:
                    print("Sorry that's not enough money")
                    continue

            else:
                continue
        elif user_input == "cappuccino":
            if is_resource_avilable(user_input,report):
                coins = collect_coins()
                if transaction_successful(coins,coffee_menu[user_input]):
                    update_resources(report,coffee_menu[user_input])
                    print(f"Here is you {user_input} ☕️. Enjoy")
                else:
                    print("Sorry that's not enough money")
                    continue

            else:
                continue
        elif  user_input == "off":
            break
        else:
            print("Sorry we don't serve it here ")


coffee_machine()

