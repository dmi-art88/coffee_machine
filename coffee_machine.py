import sys


class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.user = input("Write action (buy, fill, take, remaining, exit):\n")

    def action(self):
        if "buy" in self.user:
            buy()
            print("")
        if "fill" in self.user:
            fill()
            print("")
        if "take" in self.user:
            take()
            print("")
        if "remaining" in self.user:
            remaining()
            print("")
        if "exit" in self.user:
            sys.exit()


def buy():
    print("")
    buy_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if "1" in buy_coffee:
        espresso()
    if "2" in buy_coffee:
        latte()
    if "3" in buy_coffee:
        capuccino()
    if "back" in buy_coffee:
        return CoffeeMachine().action()


def espresso():
    if CoffeeMachine.water < 250 or CoffeeMachine.beans < 20 or CoffeeMachine.cups < 1:
        print("Sorry, not enough resources!")
        return print("")
    else:
        print("I have enough resources, making you a coffee!")
        CoffeeMachine.water -= 250
        CoffeeMachine.beans -= 16
        CoffeeMachine.cups -= 1
        CoffeeMachine.money += 4


def latte():
    if CoffeeMachine.water < 350:
        print("Sorry, not enough water!")
        return print(""), CoffeeMachine().action()
    elif CoffeeMachine.milk < 75:
        print("Sorry, not enough milk!")
        return print(""), CoffeeMachine().action()
    elif CoffeeMachine.beans < 20:
        print("Sorry, not enough coffee beans!")
        return print(""), CoffeeMachine().action()
    elif CoffeeMachine.cups < 1:
        print("Sorry, not enough cups")
        return print(""), CoffeeMachine().action()
    else:
        print("I have enough resources, making you a coffee!")

        CoffeeMachine.water -= 350
        CoffeeMachine.milk -= 75
        CoffeeMachine.beans -= 20
        CoffeeMachine.cups -= 1
        CoffeeMachine.money += 7


def capuccino():
    if CoffeeMachine.water < 300:
        print("Sorry, not enough water!")
        return print(""), CoffeeMachine().action()
    elif CoffeeMachine.milk < 200:
        print("Sorry, not enough milk!")
        return print(""), CoffeeMachine().action()
    elif CoffeeMachine.beans < 12:
        print("Sorry, not enough coffee beans!")
        return print(""), CoffeeMachine().action()
    elif CoffeeMachine.cups < 1:
        print("Sorry, not enough cups")
        return print(""), CoffeeMachine().action()
    else:
        print("I have enough resources, making you a coffee!")

        CoffeeMachine.water -= 200
        CoffeeMachine.milk -= 100
        CoffeeMachine.beans -= 12
        CoffeeMachine.cups -= 1
        CoffeeMachine.money += 6


def take():
    print(f"I gave you ${CoffeeMachine.money}")
    CoffeeMachine.money -= CoffeeMachine.money


def fill():
    print("")
    water_add = int(input("Write how many ml of water you want to add:\n"))
    milk_add = int(input("Write how many ml of milk you want to add:\n"))
    beans_add = int(input("Write how many grams of coffee beans you want to add:\n"))
    cups_add = int(input("Write how many disposable coffee cups you want to add:\n"))

    CoffeeMachine.water += water_add
    CoffeeMachine.milk += milk_add
    CoffeeMachine.beans += beans_add
    CoffeeMachine.cups += cups_add


def remaining():
    print("")
    print("The coffee machine has:")
    print(f"{CoffeeMachine.water} of water")
    print(f"{CoffeeMachine.milk} of milk")
    print(f"{CoffeeMachine.beans} of coffee beans")
    print(f"{CoffeeMachine.cups} of disposable cups")
    if CoffeeMachine.money == 0:
        print(f"{CoffeeMachine.money} of money")
    else:
        print(f"${CoffeeMachine.money} of money")


while True:
    CoffeeMachine().action()
