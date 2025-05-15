from datetime import datetime

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

def input_date(prompt="Date (YYYY-MM-DD): "):
    while True:
        entry = input(prompt)
        try:
            datetime.strptime(entry, "%Y-%m-%d")
            return entry
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

def choose_category(classes: dict):
    categories = list(classes.keys())
    print("Choose category:")

    print()

    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")
    try:
        choice = int(input("\nChoice: "))

        print()

        return categories[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return None
