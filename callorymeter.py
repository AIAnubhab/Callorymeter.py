
# Project Title : Daily Calorie Tracker CLI
# Course        : Programming for Problem Solving using Python (ETCCPP102)
# Student Name  : [Your Name Here]
# Date          : [Insert Date]


# Task 1: Welcome Message
print("===================================")
print("   Welcome to Daily Calorie Tracker")
print("===================================\n")
print("This program helps you track your meals and calories.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

n = int(input("How many meals did you eat today? "))

for i in range(n):
    meal = input(f"\nEnter meal name {i+1}: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)

# Task 3: Calorie Calculations
total = sum(calories)
average = total / n
limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total > limit:
    message = "You have exceeded your daily calorie limit!"
else:
    message = "You are within your daily calorie limit."

# Task 5: Neatly Formatted Output
print("Meal Name\tCalories")
for i in range(n):
    print(f"{meals[i]}\t\t{calories[i]}")
print("-------------------------------------------")
print(f"Total:\t\t{total}")
print(f"Average:\t{average:.2f}")
print("-------------------------------------------")
print(message)
print("-------------------------------------------")

# Task 6 (Bonus): Save Session Log to File
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    file = open("calorie_log.txt", "w")
    file.write("------ Daily Calorie Tracker Log ------\n")
    for i in range(n):
        file.write(f"{meals[i]} - {calories[i]} calories\n")
    file.write("--------------------------------------\n")
    file.write(f"Total: {total}\nAverage: {average:.2f}\n")
    file.write(message + "\n")
    file.close()
    print(" Report saved as 'calorie_log.txt'")
else:
    print("Report not saved.")

print("\nThank you for using Daily Calorie Tracker! Stay healthy!")
