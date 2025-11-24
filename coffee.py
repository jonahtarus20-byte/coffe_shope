from order import Order

class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
