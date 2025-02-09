"""
Author: Caleb Goforth
Date: 2/9/2025
File Name: goforth_lemonadeStandSchedule.py
Description: Exercise 5.3 - Python Conditionals, Lists, and Loops 
"""
# Step 1: Define a list of at least 5 tasks related to running a lemonade stand
tasks = [
    "Buy lemons and supplies",
    "Prepare lemonade",
    "Sell lemonade to customers",
    "Count earnings and restock",
    "Clean up the stand"
]

# Step 2: Print all tasks using a for loop
print("Lemonade Stand Tasks for the Week:")
for task in tasks:
    print(f"- {task}")

print("\nDaily Schedule:")

# Step 3: Create a list of days (Sunday - Saturday)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Step 4: Assign tasks to weekdays, rest on weekends
for i, day in enumerate(days):
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off! Take a break and rest. 🍹")
    else:
        print(f"{day}: {tasks[i % len(tasks)]}")  # Assigning tasks in a loop
