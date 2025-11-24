from order import Order

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})
