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

cash = 0


def check_resources(order):
    for i in order:
        if resources[i] <= order[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${cash}")


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_transaction(order):
    global cash
    money = process_coins()
    coffee_price = MENU[order]["cost"]
    if money < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if money > coffee_price:
            print(f"Here is ${money - coffee_price:.2f} in change.")
        make_coffee(order)
        cash += MENU[order]["cost"]


def make_coffee(order):
    for i in MENU[order]["ingredients"]:
        resources[i] -= MENU[order]["ingredients"][i]
    print(f"Here is your {order} ☕️. Enjoy!")


label = True

while label:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command in MENU:
        if check_resources(MENU[command]["ingredients"]):
            check_transaction(command)
    elif command == "off":
        label = False
        print("Turn off.")
    elif command == "report":
        report()
    else:
        print("Wrong command.")
