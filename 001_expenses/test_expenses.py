import unittest
from models import Food, Travel, Utilities
from manager import ExpenseManager

class TestExpenses(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()
        self.food = Food(1200, "2025-01-01", "Lunch")
        self.travel = Travel(5000, "2025-03-01", "Weekend")
        self.util = Utilities(3000, "2025-02-15", "Electricity")

        self.manager.add_expense(self.food)
        self.manager.add_expense(self.travel)
        self.manager.add_expense(self.util)

    def test_total_by_category(self):
        self.assertEqual(self.manager.total_by_category("Food"), 1200)

    def test_filter_by_category(self):
        result = self.manager.filter_by_category("Travel")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].description, "Weekend")

    def test_filter_by_date_range(self):
        result = self.manager.filter_by_date_range("2025-01-01", "2025-02-01")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].description, "Lunch")

    def test_edit_expense(self):
        self.manager.edit_expense(0, amount=1500)
        self.assertEqual(self.manager.all_expenses()[0].amount, 1500)

    def test_delete_expense(self):
        self.manager.delete_expense(1)
        self.assertEqual(len(self.manager.all_expenses()), 2)

    def test_total_all_expenses(self):
        total = self.manager.total_all_expenses()
        self.assertEqual(total, 1200 + 5000 + 3000)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            Food(-100, "2025-01-01", "Invalid expense")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Travel(200, "01-01-2025", "Bad date")

    def test_edit_with_invalid_index(self):
        # Should not raise but should not change anything
        self.manager.edit_expense(10, amount=9999)
        self.assertEqual(self.manager.total_by_category("Food"), 1200)

    def test_delete_with_invalid_index(self):
        self.manager.delete_expense(10)  # Should silently fail
        self.assertEqual(len(self.manager.all_expenses()), 3)


if __name__ == "__main__":
    unittest.main()
