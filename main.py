from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Look at Menu init, those are facts regardless of how customer interacts with the machine
menu = Menu()
items = menu.get_items()
items_as_str = menu.get_items_as_str()
# Look at CoffeeMaker init, those exist at the start of the machine serving the customer
coffee_maker = CoffeeMaker()
# This will accumulate profit, thus initiating before any interaction happens
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    user_choice = input(f'What would you like? ({items_as_str}): ').lower()

    if user_choice == 'off':
        machine_is_on = False

    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    elif user_choice in items:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    else:
        print(f"Your instruction is invalid. Please input one of these: {items}.")
