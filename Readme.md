☕ Coffee Machine — Python Project

A terminal-based coffee machine simulation built entirely in Python. Order your favourite coffee, insert coins, and get your change — just like a real machine!


📌 About The Project
The Coffee Machine is a Python project that simulates a real coffee vending machine. It tracks ingredients, handles coin transactions, gives change, and shuts down automatically when resources run out. Built as part of the 100 Days of Code — Python Bootcamp (Day 15).

🕹️ How It Works

Machine checks if it has enough ingredients to make any coffee
You choose your coffee — espresso, latte, or cappuccino
Machine checks if it has enough ingredients for your choice
You insert coins — quarters, dimes, nickels and pennies
Machine checks if you inserted enough money
✅ Correct amount → Coffee is made, change is returned
❌ Not enough money → Money is refunded
🔁 Loop continues until ingredients run out
⚠️ Machine shuts down when it can't make any more coffee


📁 Project Structure
Coffee Machine Project/
│
├── main.py          # Main game logic, loop and functions


🛠️ Features

✅ Supports 3 coffee types — espresso, latte, cappuccino
✅ Ingredient tracking — deducts ingredients after every coffee
✅ Coin calculator — handles quarters, dimes, nickels, pennies
✅ Change calculator — returns exact change to user
✅ Auto shutdown — stops when ingredients are too low
✅ Resource report — shows current ingredient levels
✅ Input validation — handles invalid coffee choices


☕ Coffee Menu
CoffeeWaterMilkCoffeeCostEspresso50ml0ml18g$1.50Latte200ml150ml24g$2.50Cappuccino250ml100ml24g$3.00

🪙 Coin Values
CoinValueQuarter$0.25Dime$0.10Nickel$0.05Penny$0.01

▶️ How To Run
Requirements

Python 3.x
No external libraries needed

Steps
bash# Clone the repository
git clone https://github.com/YOUR_USERNAME/coffee-machine.git

# Navigate into the folder
cd coffee-machine

# Run the project
python main.py

🖥️ Sample Output
☕ Welcome to the Coffee Machine!

📊 Current Resources:
  Water  : 300ml
  Milk   : 200ml
  Coffee : 100g

What would you like? (espresso/latte/cappuccino) or 'off' to quit: latte
Please insert coins:
  How many quarters? 10
  How many dimes? 0
  How many nickles? 0
  How many pennies? 0

✅ Here is your latte ☕
💰 Here is your change: $0.0

📊 Current Resources:
  Water  : 100ml
  Milk   : 50ml
  Coffee : 76g

What would you like? cappuccino
⚠️ Sorry! Not enough water to make cappuccino!

⚠️ Machine is out of ingredients!
Cannot make any more coffee. Shutting down. Goodbye! 👋

💡 What I Learned

Using nested dictionaries to store structured data
Writing and calling functions with multiple parameters
Using while loops to keep a program running
Validating user input and handling edge cases
Tracking and updating resource/inventory data
Breaking a big problem into small reusable functions


🔧 Functions Overview
FunctionWhat It Doescheck_ingredients()Checks if machine has enough ingredientsdeduct_ingredients()Removes used ingredients after making coffeecheck_resources_for_next()Checks if machine can make any coffeemoney()Calculates total coins inserted by userprint_report()Displays current resource levelsoperation()Handles full transaction logic

🙌 Credits
Built as part of 100 Days of Code - The Complete Python Pro Bootcamp
by Dr. Angela Yu on Udemy.

📄 License
This project is open source and free to use for learning purposes.