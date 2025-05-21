class Coffee:
    def __init__(self, name):
        self.name = name  # Triggers setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")
        self._name = value

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})
