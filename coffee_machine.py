# check the supplies if they are enough
# check if the cost provided is enough or not and do the transaction
# deduct the cost of the resources according to the order after transaction
# check for repeatability of the function and other options like refilling

MENU = {
    "espresso": {
        "ingredients": { "water": 50, "coffee": 18, }, "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24, },"cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24,}, "cost": 3.0,
    }
}

resources = { "water": 300, "milk": 200,"coffee": 100,}

# for change add new options
# for change ask if customer packets of creamer or sugar in addition 
profit= 0

coffeelogo = '''
  Please enjoy!!
     )))
    (((
  +-----+
  |     |]
  `-----'    
___________
`---------     '''

def resources_check(drink):
    for item in drink:
        if resources[item]< drink[item]:
            print(f"Sorry! There is not enough{item}.")
            return False
        else:
            return True

def payment_check(money_given, money_required):
    if money_given< money_required:
        print("Sorry! The money is not enough. Your ${money_given} are refunded.")
        return False
    else:
        global profit 
        profit += round(money_given,2)
        change = round(money_given - money_required,2)
        print(f"Here's your change: ${change}")
        return True

def calculatemoney():
    total_cost = int(input("Enter the number of quarters:"))*0.20
    total_cost += int(input("Enter the number of dimes:"))*0.10
    total_cost += int(input("Enter the number of nickels:"))*0.05
    total_cost += int(input("Enter the number of pennies:"))*0.01 
    return total_cost 

def make_coffee(coffeechoice, ingredients):
    for item in ingredients:
        resources[item]-= ingredients[item]
    print(f"Here's your {coffeechoice}!")
    print(coffeelogo)


is_on = True

while is_on:
    coffeechoice = input("What would you like to drink ? latte/cappuccino/espresso? \n")
    if coffeechoice == "off":
        is_on = False
    elif coffeechoice == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"coffee = {resources['coffee']}gm")
        print(f"money = ${round(profit,2)} ")
    
    elif coffeechoice in MENU:
        drink = MENU[coffeechoice]  # important step of creating a list 
                                    # to store the details of resources of the coffeechoice
        if resources_check(drink["ingredients"]):
            money_given = calculatemoney()
            if payment_check(money_given , drink["cost"]):
                make_coffee( coffeechoice, drink["ingredients"])

    else:
        print("Please enter a valid choice!")