import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_price_validation(self):
        customer = Customer("TestUser")
        coffee = Coffee("Drip")

        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(customer, coffee, 15)

        order = Order(customer, coffee, 5)
        self.assertEqual(order.price, 5.0)

    def test_relationships_on_init(self):
        customer = Customer("Lena")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 4)

        self.assertIn(order, customer.orders())
        self.assertIn(order, coffee.orders())

if __name__ == "__main__":
    unittest.main()
