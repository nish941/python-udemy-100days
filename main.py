from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MenuItem:  name cost ingredients[dictionary)]
# Menu: get_items() , find_drink(order_name)
# CoffeeMaker: report(),is_resource_sufficient(drink),  make_coffee(MenuItem)
# MoneyMachine: report()- profit , make_payment(cost)

# Off machine, report of machine, refill the machine.
# Choice. Make the program repeatable.
# check resources, transaction then make coffee

menu = Menu() # menu is the blueprint so we created objects from that
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True
while (is_on):
    start = input("Would you like to- 1: order 2:report 3: refill 4: off?\n")
    if start == "1":
       choice = input(menu.get_items())
       coffeechoice = menu.find_drink(choice)
       if coffeemaker.is_resource_sufficient(coffeechoice) and moneymachine.make_payment(coffeechoice.cost):
          coffeemaker.make_coffee(coffeechoice)
    elif start == "2":
       coffeemaker.report()
       moneymachine.report()
    elif start == "3":
       print("halo")
    else:
       is_on = False