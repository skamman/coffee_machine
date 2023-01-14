from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_on = True

money = 0


# Prompt user
def user_prompt():
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    return user_choice


def check_resource(user_choice):
    global resources
    global MENU

    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]
    water_required = MENU[user_choice]["ingredients"]["water"]
    milk_required = MENU[user_choice]["ingredients"]["milk"]
    coffee_required = MENU[user_choice]["ingredients"]["coffee"]
    if water_available >= water_required and milk_available >= milk_required and coffee_available >= coffee_required:
        return True
    else:
        print("Insufficient resources!!")
        return False


def process_coins(user_choice):
    global MENU
    global resources
    global money
    coffee_cost = MENU[user_choice]["cost"]
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    money_inserted = quarters + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    # Check transaction successful
    if coffee_cost > money_inserted:
        print("Money insufficient. Please collect your coins")
    else:
        balance = round(money_inserted - coffee_cost, 2)
        money += coffee_cost
        print(f"Cost of the {user_choice} is {coffee_cost}. Please collect the balance {balance}")

        return money

def make_coffee(user_choice):
    global MENU
    global resources

    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]

    return resources
while turn_on:

    choice = user_prompt().lower()
    # Turn off the Coffee Machine for technical persons
    if choice == "off":
        turn_on = False
    # Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")
    #coffee
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        # Check resources sufficient
        if check_resource(choice):
            bill = MENU[choice]['cost']
            print(f"Ingredients available for your choice of drink {choice}")
            print(f"Please insert {bill}")


            # Process coins.
            process_coins(choice)

            # make coffee
            make_coffee(choice)

    else:
        print("Please enter a valid response")

    system("cls")

