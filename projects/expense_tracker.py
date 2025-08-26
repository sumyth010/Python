


expenses = []


while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append({"amount": amount, "category": category})
        print("Expense added!")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nYour expense:")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}.{exp['category']} - {exp['amount']}")
    
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invaid option, try again")
