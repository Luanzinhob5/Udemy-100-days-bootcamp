from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
 
is_on = True

while is_on:
    options = menu.get_items()
    guess = input(f"What would you like? ({options}): ")


    if guess == "off":
        is_on = False
    elif guess == "report":
        coffee_maker.report
        money_machine.report
    else:
        drink = menu.find_drink(guess)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


