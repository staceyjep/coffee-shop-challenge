from customer import Customer
from coffee import Coffee
from order import Order


alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

Order(alice, latte, 4.5)
Order(bob, espresso, 3.0)
Order(alice, espresso, 3.5)


print(f"Alice's Orders: {[o.coffee.name for o in alice.orders()]}")
print(f"Bob's Coffees: {[o.coffee.name for o in bob.orders()]}")
print(f"Customers who ordered Latte: {[c.name for c in latte.customers()]}")
