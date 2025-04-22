from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


guess = input(f"What would you like? ({menu.get_items()}): ")

if guess =="report":
    coffee_maker.report()
    money_machine.report()
else:
    menu.find_drink(guess)
    
