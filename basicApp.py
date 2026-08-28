isRunning = True
balance = 0.0

transactions = []

while isRunning:
    print("Hello, welcome to your Personal Finance Manager!")
    option = input(
        "Please choose an option:\n1. View Balance\n2. Add Expense\n3. Add Income\n4. View Transactions\n5. Exit\n\n> ")
    print("\n===============================\n")

    if option == "1":
        print(f"Your current balance is: ${balance:.2f}")
        print("\n===============================\n")
    elif option == "2":
        expense_name = input("Enter the name of the expense: ")
        expense_amount = float(input("Enter the amount of the expense: "))
        balance -= expense_amount
        transactions.append(("Expense", expense_name, expense_amount))
        print(
            f"Expense '{expense_name}' of ${expense_amount:.2f} added. New balance: ${balance:.2f}")
        print("\n===============================\n")
    elif option == "3":
        income_name = input("Enter the name of the income: ")
        income_amount = float(input("Enter the amount of the income: "))
        balance += income_amount
        transactions.append(("Income", income_name, income_amount))
        print(
            f"Income '{income_name}' of ${income_amount:.2f} added. New balance: ${balance:.2f}")
        print("\n===============================\n")
    elif option == "4":
        print("Transaction History:")
        for transaction in transactions:
            print(f"{transaction[0]} {transaction[1]}: ${transaction[2]:.2f}")
        print("\n===============================\n")
    elif option == "5":
        print("Exiting the Personal Finance Manager. Goodbye!")
        isRunning = False
