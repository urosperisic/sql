from abc import ABC, abstractmethod
from datetime import datetime

class Expense(ABC):
    def __init__(self, amount: float, date: str, description: str):
        self.amount = amount
        self.date = date
        self.description = description

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount cannot be negative.")
        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        try:
            self._date = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @abstractmethod
    def category(self) -> str:
        pass

    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "category": self.category()
        }

    def __str__(self):
        return f"{self.category():<15} | {self.description:<30} | {self.amount:>10.2f} RSD | {self.date.date()}"


class Food(Expense):
    def category(self):
        return "Food"

class Travel(Expense):
    def category(self):
        return "Travel"

class Utilities(Expense):
    def category(self):
        return "Utilities"
