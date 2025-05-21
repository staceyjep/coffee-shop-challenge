import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("A")
        with self.assertRaises(ValueError):
            Customer("ThisNameIsWayTooLong")
        self.assertEqual(Customer("Jane").name, "Jane")

    def test_orders_and_coffees(self):
        customer = Customer("Mike")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")

        Order(customer, coffee1, 4.5)
        Order(customer, coffee2, 3.5)

        self.assertEqual(len(customer.orders()), 2)
        self.assertIn(coffee1, customer.coffees())
        self.assertIn(coffee2, customer.coffees())

if __name__ == "__main__":
    unittest.main()
