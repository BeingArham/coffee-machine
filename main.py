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

def check_ingredients(user_choice):
    """Check if machine has enough ingredients"""
    needed = MENU[user_choice]['ingredients']
    for ingredient in needed:
        if needed[ingredient] > resources[ingredient]:
            print(f"Sorry! Not enough {ingredient} to make {user_choice}!")
            return False
    return True

def deduct_ingredients(user_choice):
    """Deduct ingredients after making coffee"""
    needed = MENU[user_choice]['ingredients']
    for ingredient in needed:
        resources[ingredient] -= needed[ingredient]

def check_resources_for_next():
    """Check if machine can make ANY coffee for next operation"""
    for coffee in MENU:
        needed = MENU[coffee]['ingredients']
        can_make = True
        for ingredient in needed:
            if needed[ingredient] > resources[ingredient]:
                can_make = False
                break
        if can_make:
            return True  # Can still make at least one coffee
    return False  # Cannot make any coffee

def money(quarters_count, dimes_count, nickles_count, pennies_count):
    """Calculate total money inserted"""
    total_quarter = float(quarters_count * 0.25)
    total_dimes = float(dimes_count * 0.10)
    total_nickles = float(nickles_count * 0.05)
    total_pennies = float(pennies_count * 0.01)
    total_sum = round(total_quarter + total_dimes + total_nickles + total_pennies, 2)
    return total_sum

def print_report():
    """Print current resource levels"""
    print("\n📊 Current Resources:")
    print(f"  Water  : {resources['water']}ml")
    print(f"  Milk   : {resources['milk']}ml")
    print(f"  Coffee : {resources['coffee']}g\n")

# ✅ Main loop
machine_on = True

print("☕ Welcome to the Coffee Machine!")

while machine_on:

    # Check if machine can make any coffee before asking
    if not check_resources_for_next():
        print("\n⚠️ Machine is out of ingredients!")
        print("Cannot make any more coffee. Shutting down. Goodbye! 👋")
        break

    print_report()
    user_choice = input("What would you like? (espresso/latte/cappuccino) or 'off' to quit: ").lower()

    # ✅ Secret off switch
    if user_choice == "off":
        print("Turning off machine. Goodbye! 👋")
        machine_on = False

    # ✅ Valid coffee choice
    elif user_choice in MENU:

        # Step 1: Check ingredients
        if not check_ingredients(user_choice):
            print("Please choose another coffee!\n")
            continue

        # Step 2: Insert coins
        print("Please insert coins:")
        quarters_count = int(input("  How many quarters? "))
        dimes_count = int(input("  How many dimes? "))
        nickles_count = int(input("  How many nickles? "))
        pennies_count = int(input("  How many pennies? "))

        total_sum = money(quarters_count, dimes_count, nickles_count, pennies_count)
        cost = MENU[user_choice]['cost']

        # Step 3: Check money
        if total_sum < cost:
            print(f"Sorry! Not enough money. {user_choice} costs ${cost}. Money refunded.\n")
            continue

        # Step 4: Make coffee & give change
        change = round(total_sum - cost, 2)
        deduct_ingredients(user_choice)
        print(f"\n✅ Here is your {user_choice} ☕")
        if change > 0:
            print(f"💰 Here is your change: ${change}\n")

    else:
        print("❌ Invalid choice! Please type espresso, latte or cappuccino\n")