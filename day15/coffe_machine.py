from menu import resources
from menu import MENU


# Funcao que printa o troco
def change_money(u_quarters,u_dimes,u_nickles,u_pennies,u_price):
    all_money = (u_quarters * 0.25) + (u_dimes * 0.10) + (u_nickles * 0.05) + (u_pennies * 0.1) 
    if all_money > u_price:
        print(f"Here is {all_money - u_price:.2f}$ in change.")
    elif all_money < u_price:
        print(f"Sorry that's not enought money. Money refunded.")


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


while True:
    report_while = True
    money_in_machine = 0

    while report_while:
        guess = input("What would you like? (espresso/latte/cappuccino): ")
        
        
        if guess == "report":
                print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money_in_machine}$")
        else:
            water_coffee = MENU[guess]["ingredients"]["water"]
            coffee_coffee = MENU[guess]["ingredients"]["coffee"]
            if guess != 'espresso':
                milk_coffee = MENU[guess]["ingredients"]["milk"]

            water -= water_coffee 
            coffee -= coffee_coffee 
            if guess != 'espresso':
                milk -= milk_coffee 

            if water < 0:
                print(f"Sorry theres not enought Water.")
            elif coffee < 0:
                print(f"Sorry theres not enought Coffee.")
            elif milk < 0:
                print(f"Sorry theres not enought Milk.")
            else:
                price = MENU[guess]["cost"]
                report_while = False


    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    change_money(quarters,dimes,nickles,pennies,price)
    print(f"Here is your {guess} Enjoy!")


