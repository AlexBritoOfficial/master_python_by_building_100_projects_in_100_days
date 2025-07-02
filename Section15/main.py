MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 250,
            "coffee": 150,
            "milk": 24
        },
        "cost": 1.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 100,
            "milk": 24
        },
        "cost": 1.5
    }
}

resources = {
    "water": 1300,
    "coffee": 1200,
    "milk": 1100,
    "money": 0
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}

if __name__ == "__main__":

    isDrinkDispensed = False

    while not isDrinkDispensed:

        # Reset flags and counters for each order
        isResourcesEnough = True
        isMoneyHanded = False
        userTotalDict = {coin: 0 for coin in COIN_VALUES}
        userTotal = 0.0

        userResponse = input("Would you like to order an espresso/latte/cappuccino? \n").lower().strip()

        if userResponse == "no":
            print("Thank you, have a nice day")
            break

        elif userResponse == "off":
            print("Machine shutting down")
            break

        elif userResponse == "report":
            for key, value in resources.items():
                if key in ["milk", "water"]:
                    print(f"{key.capitalize()}: {value}ml")
                elif key == "coffee":
                    print(f"{key.capitalize()}: {value}g")
                else:
                    print(f"{key.capitalize()}: ${value}")
            continue

        elif userResponse == "":
            print("Please enter something")
            continue

        elif userResponse not in MENU:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")
            continue

        # Check resources for the selected drink
        for ingredient, required_amount in MENU[userResponse]["ingredients"].items():
            if required_amount > resources.get(ingredient, 0):
                print(f"Sorry, not enough {ingredient}.")
                isResourcesEnough = False

        if not isResourcesEnough:
            # Skip coin processing and take a new order
            continue

        cost = round(MENU[userResponse]["cost"], 2)
        print(f"\nThe total for your {userResponse} comes out to ${cost}\n")

        # Process coins
        while not isMoneyHanded:

            userMoney = input(
                "Insert quarters, dimes, nickels, and pennies into machine\n"
                "Please enter DONE when you are done inserting your coins.\n"
            ).strip()

            if userMoney.lower() == "done":

                moneyInserted = sum(
                    userTotalDict[coin] * COIN_VALUES[coin] for coin in userTotalDict
                )
                moneyInserted = round(moneyInserted, 2)
                print(f"Money inserted: ${moneyInserted}")

                if moneyInserted < cost:
                    print(f"\nSorry that's not enough money. ${moneyInserted} has been refunded.")
                    # Reset money counters for retry
                    userTotalDict = {coin: 0 for coin in COIN_VALUES}
                    userTotal = 0.0
                    # Continue coin insertion loop
                    continue

                else:
                    change = round(moneyInserted - cost, 2)
                    resources["money"] += cost
                    print(f"Here is ${change} dollars in change.")

                    for ingredient in MENU[userResponse]["ingredients"]:
                        resources[ingredient] -= MENU[userResponse]["ingredients"][ingredient]

                    print(f"\nHere is your {userResponse} ☕️. Enjoy!\n")

                    isMoneyHanded = True
                    # After successful purchase, reset for next order (flags and counters)
                    # Actually, loop will restart, so flags reset at top again
                    break

            elif userMoney == "":
                print("Please insert coins or type DONE.")

            else:
                try:
                    coin = float(userMoney)
                    if coin not in COIN_VALUES.values():
                        print("Please only insert quarters, dimes, nickels, and pennies")
                        continue
                except ValueError:
                    print("Invalid input.")
                    continue

                # Map coin value back to coin name
                coin_name = None
                for name, val in COIN_VALUES.items():
                    if val == coin:
                        coin_name = name
                        break

                if coin_name:
                    userTotalDict[coin_name] += 1
                    userTotal += coin
                    print(f"\nTotal entered: ${round(userTotal, 2)}")
                else:
                    print("Coin not recognized. Please insert valid coins.")

