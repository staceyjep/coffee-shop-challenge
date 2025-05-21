import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("AB")
        self.assertEqual(Coffee("Mocha").name, "Mocha")

    def test_orders_and_customers(self):
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")

        Order(customer1, coffee, 3.0)
        Order(customer2, coffee, 3.5)

        self.assertEqual(len(coffee.orders()), 2)
        self.assertIn(customer1, coffee.customers())
        self.assertIn(customer2, coffee.customers())

if __name__ == "__main__":
    unittest.main()
