from expenses import Food, Travel, Utilities, ExpenseManager

def display_expense(e, index=None):
    label = f"{index}: " if index is not None else ""
    print(f"{label}{e.category()} - {e.description} - {e.amount} RSD ({e.date.date()})")

def input_positive_amount():
    while True:
        entry = input("Amount: ").strip()
        if not entry:
            print("Amount cannot be empty.")
            continue
        try:
            amount = float(entry)
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    file = "expenses.json"
    manager = ExpenseManager()
    manager.load_from_json(file)

    classes = {"Food": Food, "Travel": Travel, "Utilities": Utilities}

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Filter by category")
        print("4. Filter by date")
        print("5. Total by category")
        print("6. Edit expense")
        print("7. Delete expense")
        print("0. Save and exit")

        choice = input("\nChoice: ")

        print()

        if choice == "1":
            cat = input("Category (Food/Travel/Utilities): ")
            amount = input_positive_amount()
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description: ")

            if cat in classes:
                try:
                    manager.add_expense(classes[cat](amount, date, description))
                except ValueError as e:
                    print(f"Error adding expense: {e}")
            else:
                print("Unknown category.")

        elif choice == "2":
            for i, e in enumerate(manager.all_expenses()):
                display_expense(e, i)

        elif choice == "3":
            cat = input("Category: ")
            for e in manager.filter_by_category(cat):
                display_expense(e)

        elif choice == "4":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            for e in manager.filter_by_date_range(start, end):
                display_expense(e)

        elif choice == "5":
            cat = input("Category: ")
            total = manager.total_by_category(cat)
            print(f"Total for {cat}: {total} RSD")

        elif choice == "6":
            try:
                index = int(input("Index of expense to edit: "))
                entry = input("New amount (or Enter to skip): ").strip()
                amount = None
                if entry:
                    amount = float(entry)
                    if amount < 0:
                        print("Amount cannot be negative.")
                        continue

                date = input("New date (or Enter): ")
                description = input("New description (or Enter): ")

                manager.edit_expense(
                    index,
                    amount=amount,
                    date=date if date else None,
                    description=description if description else None,
                )
            except ValueError:
                print("Invalid input.")

        elif choice == "7":
            try:
                index = int(input("Index of expense to delete: "))
                manager.delete_expense(index)
            except ValueError:
                print("Invalid index input.")

        elif choice == "0":
            manager.save_to_json(file)
            print("Data saved. Goodbye!")
            break

        else:
            print("Unknown option.")

if __name__ == "__main__":
    menu()
