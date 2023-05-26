from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True

while isOn:
    myMenu = Menu()
    myCoffeMaker = CoffeeMaker()
    myMoneyMachine = MoneyMachine()
    options = myMenu.get_items()
    user_order = input(f"What would you like {options}")

    if user_order == "report":
        myCoffeMaker.report()
        myMoneyMachine.report()
    elif user_order == "off":
        isOn = False
    else:
        drink = myMenu.find_drink(user_order)
        if myCoffeMaker.is_resource_sufficient(drink) and myMoneyMachine.make_payment(drink.cost):
            myCoffeMaker.make_coffee(drink)
