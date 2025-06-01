""""
Given the course outline of this Udemy course, the course has not yet reached a point where the instructor speaks on OOP, hence the reason no OOP
"""

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
    "water": 300,
    "coffee": 200,
    "milk": 100,
    "money": 0
}

if __name__ == "__main__":

    # This flag is responsible for letting us know, if the drink was dispensed.
    isDrinkDispensed: bool = False

    # This flag is responsible for letting us know, if the drink was dispensed.
    isResourcesEnough: bool = True

    # This flag is responsible for letting us know, if the user has fully inserted their change.
    isMoneyHanded: bool = False

    userTotal: float = 0

    userTotalDict: dict = {
        "quarter": {
            "count": 0
        },
        "dime": {
            "count": 0
        },
        "nickel": {
            "count": 0
        },
        "penny": {
            "count": 0
        }
    }

    while not isDrinkDispensed:
        userResponse = input("Would you like order a espresso/latte/cappuccino ? \n")

        if userResponse.lower().strip() == "no":
            isDrinkDispensed = True
            print("Thank you, have a nice day")

        elif userResponse.lower().strip() == "off":
            isDrinkDispensed = True
            print("Machine shutting down")

        elif userResponse.lower().strip() == "report":
            for key, value in resources.items():
                if key.lower().strip() == "milk" or key.lower().strip() == "water":
                    print(f"{key}: {value}ml")

                elif key.lower().strip() == "coffee":
                    print(f"{key}: {value}g")

                else:
                    print(f"{key}: ${value}")

        elif userResponse.lower().strip() == "":
            print("Please enter something")

        else:

            """
            Process coins.
                
                a.  If there are sufficient resources to make the drink selected, then the program should
                    prompt the user to insert coins.
                
                b.  Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
                
                c.  Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
                    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
            """
            for i, (key, value) in enumerate(MENU[userResponse]["ingredients"].items()):

                if value <= resources[list(resources.keys())[i]]:
                    continue
                else:
                    isResourcesEnough = False

            print(f"\nThe total for your {userResponse}, comes out to ${MENU[userResponse]["cost"]}\n")

            while not isMoneyHanded:

                userMoney = input(
                    "Insert quarters, dimes, nickels, and pennies into machine \n"
                    "\nPlease enter DONE, when you are done inserting your coins.\n")

                if userMoney == "DONE".lower() or userMoney == "DONE".upper():
                    isMoneyHanded = True

                elif userMoney == "" or float(userMoney) not in [0.25, 0.10, .05, .01]:
                    print("Please only insert quarters, dimes, nickles, and pennies")


                else:

                    if float(userMoney) == .25:
                        userTotalDict["quarter"]["count"] = userTotalDict["quarter"]["count"] + 1

                    if float(userMoney) == .10:
                        userTotalDict["dime"]["count"] = userTotalDict["dime"]["count"] + 1

                    if float(userMoney) == .05:
                        userTotalDict["nickel"]["count"] = userTotalDict["nickel"]["count"] + 1

                    if float(userMoney) == .01:
                        userTotalDict["penny"]["count"] = userTotalDict["penny"]["count"] + 1

            """
                    Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
                    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
            """
            print(userTotalDict)