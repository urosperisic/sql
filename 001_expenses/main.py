from manager import ExpenseManager
from models import Food, Travel, Utilities
from utils import input_positive_amount, input_date, choose_category, print_error

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
        print("8. Total of all expenses")
        print("0. Save and exit")

        choice = input("\nChoice: ")

        print()

        if choice == "1":
            cat = choose_category(classes)
            if not cat:
                continue
            amount = input_positive_amount()
            date = input_date()
            description = input("Description: ")
            try:
                manager.add_expense(classes[cat](amount, date, description))
            except ValueError as e:
                print_error(f"Error: {e}")

        elif choice == "2":
            for i, e in enumerate(manager.all_expenses()):
                print(f"        {i}: {e}")

        elif choice == "3":
            cat = choose_category(classes)
            if cat:
                for e in manager.filter_by_category(cat):
                    print(f"        {e}")

        elif choice == "4":
            try:
                start = input_date("Start date (YYYY-MM-DD): ")
                end = input_date("End date (YYYY-MM-DD): ")

                print()

                for e in manager.filter_by_date_range(start, end):
                    print(f"        {e}")
            except ValueError as e:
                print_error(f"Error: {e}")


        elif choice == "5":
            cat = choose_category(classes)
            if cat:
                total = manager.total_by_category(cat)
                print(f"        Total for {cat}: {total} RSD")

        elif choice == "6":
            try:
                index = int(input("Index of expense to edit: "))
                entry = input("\nNew amount (or Enter to skip): ").strip()
                amount = float(entry) if entry else None
                if amount is not None and amount < 0:
                    print_error("Amount cannot be negative.")
                    continue
                date = input("New date (or Enter to skip): ").strip()
                description = input("New description (or Enter to skip): ").strip()
                manager.edit_expense(index, amount, date if date else None, description if description else None)
            except ValueError:
                print_error("Invalid input.")

        elif choice == "7":
            try:
                index = int(input("Index of expense to delete: "))
                manager.delete_expense(index)
            except ValueError:
                print_error("Invalid index input.")

        elif choice == "8":
            print(f"        Total expenses: {manager.total_all_expenses()} RSD")

        elif choice == "0":
            manager.save_to_json(file)
            print("Data saved. Goodbye!")
            break

        else:
            print_error("Unknown option.")

if __name__ == "__main__":
    menu()
