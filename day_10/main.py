import os
from art import logo


def clear_console():
    os.system('clear')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def muliply(a, b):
    return a * b

def divide(a, b):
    return a / b



operators = {"+": add, "-": subtract, "*": muliply, "/": divide}
working = True

while working:
    clear_console()
    print(logo)
    first_num = float(input("Input first number > "))
    operation = input("Input operation (+, -, *, /) > ")
    second_num = float(input("Input second number > "))

    if operation in operators.keys():
        print(f"{first_num} {operation} {second_num} = {operators[operation](first_num, second_num)}")
    else:
        print("You're type wrong operator!")
    
    triger = input("Run program againe? (Y/n)")
    if triger == "n":
        working = False
