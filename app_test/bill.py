class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append((name, price))

    def total(self):
        return sum(price for _, price in self.items)

    def item_count(self):
        return len(self.items)

    def display(self):
        return self.items