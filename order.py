class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price  # Triggers setter

        customer.add_order(self)
        coffee.add_order(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or not (1 <= value <= 10):
            raise ValueError("Price must be a number between 1 and 10.")
        self._price = float(value)
