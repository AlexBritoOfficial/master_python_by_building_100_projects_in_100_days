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

    isDrinkDispensed = False
    enoughResources = True
    isMoneyHanded = False
    isResourcesEnough = True
    userTotal = 0

    while (not isDrinkDispensed):
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

            orderIngredients = MENU[userResponse]["ingredients"]
            resourceKeysList = list(resources.keys())

            for i, (key, value) in enumerate(orderIngredients.items()):

                if value <= resources[list(resources.keys())[i]]:
                    continue
                else:
                    isResourcesEnough = False

            print(f"The total for your {userResponse}, comes out to ${MENU[userResponse]["cost"]}")

            while userTotal <=  MENU[userResponse]["cost"] and isResourcesEnough:

                userMoney = input(
                    "Insert quarters, dimes, nickels, and pennies into machine \n")

                if  userMoney == "" or float(userMoney) not in [0.25, 0.10, .05, .01]:
                    print("Please only insert quarters, dimes, nickles, and pennies")
                else:
                    userTotal += float(userMoney)
                    print(f"User Total: {userTotal}")
