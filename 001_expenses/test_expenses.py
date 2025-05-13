import unittest
from expenses import Food, Travel, Utilities, ExpenseManager

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

if __name__ == "__main__":
    unittest.main()
