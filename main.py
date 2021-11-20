# Import Classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    options = menu.get_items()
    user_select = input(f"What would you like? ({options}): ").lower()
    if user_select == "off":
        print("Goodbye.")
        on = False
    elif user_select == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_select) # Create drink of user choice
        if coffee_maker.is_resource_sufficient(drink): # Check to see if resources are sufficient
            # Make Payment
            print(f"A {user_select} costs ${drink.cost}.") # Print the cost of the drink
            if money_machine.make_payment(drink.cost): # Allow user to insert coins and calculate if payment fulfills cost
                coffee_maker.make_coffee(drink) # Make Coffee




