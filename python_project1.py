from datetime import datetime

while True:
    print("\n1 Add Expense")
    print("2 Show Expenses")
    print("3 Show Total")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount: "))
            desc = input("Enter description: ")

            date = datetime.now().strftime("%d-%m-%Y")

            with open("expenses.txt", "a") as file:
                file.write(f"{amount} {desc} {date}\n")

            print("Expense added")

        except ValueError:
            print("Invalid amount")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as file:
                data = file.readlines()

                if not data:
                    print("No expenses found")
                else:
                    print("\nExpenses:")
                    for line in data:
                        print(line.strip())

        except FileNotFoundError:
            print("No expenses found")

    elif choice == "3":
        total = 0

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    amount, desc, date = line.split(maxsplit=2)
                    total += float(amount)

            print("Total Expense:", total)

        except FileNotFoundError:
            print("No data found")

    elif choice == "4":
        print("Goodbye")
        break  

    else:
        print("Invalid choice")
