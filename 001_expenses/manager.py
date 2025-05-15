import json
from typing import List
from datetime import datetime
from models import Expense, Food, Travel, Utilities

class ExpenseManager:
    def __init__(self):
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def edit_expense(self, index: int, amount=None, date=None, description=None):
        if 0 <= index < len(self.expenses):
            if amount is not None:
                self.expenses[index].amount = amount
            if date is not None:
                self.expenses[index].date = date
            if description is not None:
                self.expenses[index].description = description

    def delete_expense(self, index: int):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]

    def filter_by_category(self, category: str) -> List[Expense]:
        return [e for e in self.expenses if e.category() == category]

    def filter_by_date_range(self, start_date: str, end_date: str) -> List[Expense]:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return [e for e in self.expenses if start <= e.date <= end]

    def total_by_category(self, category: str) -> float:
        return sum(e.amount for e in self.expenses if e.category() == category)

    def total_all_expenses(self) -> float:
        return sum(e.amount for e in self.expenses)

    def all_expenses(self) -> List[Expense]:
        return self.expenses

    def save_to_json(self, file: str):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=4)

    def load_from_json(self, file: str):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for e in data:
                    self.expenses.append(self._create_expense_from_dict(e))
        except FileNotFoundError:
            print(f"No existing data found in {file}. Starting fresh.")
        except json.JSONDecodeError:
            print("Failed to decode JSON. The file might be corrupted.")

    def _create_expense_from_dict(self, data: dict) -> Expense:
        cls = {
            "Food": Food,
            "Travel": Travel,
            "Utilities": Utilities
        }.get(data["category"])
        return cls(data["amount"], data["date"], data["description"])
