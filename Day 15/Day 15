# Coffee Machine

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,}

def check(ordered_resource):
    for i in ordered_resource:
        if ordered_resource[i] > resources[i]:
            print(f"​Sorry there is not enough {i}.")
            return False
    return True

def payment():
    money = int(input("Please Enter no. of 10 Ruppee Note: " )) *10
    money += int(input("Please Enter no. of 50 Ruppee Note: " )) *50
    money += int(input("Please Enter no. of 100 Ruppee Note: " )) *100
    money += int(input("Please Enter no. of 200 Ruppee Note: " )) *200
    return money

is_on = True
while is_on:
    choice = input(" ​What would you like? (espresso/latte/cappuccino) : \n​")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        for i in resources:
            print(f"{i} : {resources[i]}")
    else:
        drink = menu[choice]
        check(drink["ingredients"])
        inserted_money = payment()


