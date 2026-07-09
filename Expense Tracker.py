#💡 Milestone Project: Build a command-line application, like a Hangman game or a personal expense tracker that saves data to a .txt or .csv file.
while True:
    name = input("What is your name?").capitalize().strip()

    expense = input("Write the amount of money spent on your expense.")

    if expense.isdigit():
        expense = int(expense)
        print(f"{expense:.2f}")
    elif float(expense):
        expense = float(expense)
        print(f"{expense:.2f}")
    else:
        print("Try again.")
        continue

    category = input("Write the category type of your expense.")

    if category.isdigit() or category.isdecimal():
        print("Try again.")
        continue
    else:
        print(category.capitalize().strip())

    current_money = input("How much money do you now have?")

    if current_money.isdigit():
        current_money = int(current_money)
        print(f"{current_money:.2f}")
    elif float(current_money):
        current_money = float(current_money)
        print(f"{current_money:.2f}")
    else:
        print("Try again.")
        continue

    choice = input("Would you like to save and quit?").capitalize().strip()
    if choice == "Quit":
        with open(fr"textfiles/{name}'sExpenses.txt", "a") as file:
            file.write(f"Expense : {expense:.2f}\nCategory : {category}\nCurrent Money : {current_money:.2f}\n")
        print("Bye! Hope to see you soon!")
        break
