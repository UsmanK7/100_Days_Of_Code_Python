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


# TODO: 5 Prompt user to enter coins if there are sufficient resources
def process_coins(flavor):
    quarters = float(input("how many quarters?"))
    dimes = float(input("how many dimes?"))
    nickles = float(input("how many nickles?"))
    pennies = float(input("how many pennies?"))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


user_order = True

while user_order != "off":
    # TODO: 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_order = input("What would you like? (espresso/latte/cappuccino):")

    # TODO: 2 When user input report print all the resources
    if user_order == "report":
        for value in resources:
            print(f"{value}: {resources[value]}ml")

    # TODO: 3 Turn off the machine when user input 'off'
    elif user_order == "off":
        exit()

    # TODO: 4 Check resource sufficient?
    elif user_order == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough water.")
        elif resources["milk"] < 150:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        else:
            monetary_value = process_coins(user_order)
            if monetary_value < 2.50:
                print("“Sorry that's not enough money. Money refunded.")
            else:
                if monetary_value != 2.50:
                    change = monetary_value - 2.50
                    print(f"Here is {change} dollars in change.")

                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24
                print(f"Here is your {user_order}☕  Enjoy!")
    elif user_order == "espresso":
        if resources["water"] < 50:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < 18:
            print("Sorry there is not enough coffee.")
        else:
            monetary_value = process_coins(user_order)
            if monetary_value < 1.5:
                print("“Sorry that's not enough money. Money refunded.")
            else:
                if monetary_value != 1.5:
                    change = monetary_value - 1.50
                    print(f"Here is {change} dollars in change.")

                resources["water"] -= 50
                resources["coffee"] -= 18
                print(f"Here is your {user_order}☕  Enjoy!")
    elif user_order == "cappuccino":
        if resources["water"] < 250:
            print("Sorry there is not enough water.")
        elif resources["milk"] < 100:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        else:
            monetary_value = process_coins(user_order)
            if monetary_value < 3.0:
                print("“Sorry that's not enough money. Money refunded.")
            else:
                if monetary_value != 3.0:
                    change = monetary_value - 3.0
                    print(f"Here is {change} dollars in change.")

                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24
                print(f"Here is your {user_order}☕  Enjoy!")
    else:
        print("invalid input! please try again")
