class Customer:
    def __init__(self, name):
        self.name = name  # Triggers setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 15):
            raise ValueError("Customer name must be a string between 2 and 15 characters.")
        self._name = value

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})
