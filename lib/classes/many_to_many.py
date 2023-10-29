class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self] 
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    def num_orders(self):
        return len([order for order in Order.all if order.coffee == self])
    def average_price(self):
        coffee_sum = sum([order.price for order in Order.all if order.coffee == self])
        coffee_count = len([order.coffee for order in Order.all if order.coffee == self])
        return 0 if coffee_count == 0 else coffee_sum / coffee_count

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception("Cannot reassign name after initialization.")
        elif isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Name must be a string of at least 3 characters.")

class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters.")
        
    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending_per_coffee = {}

        for order in Order.all:
            if order.coffee == coffee:
                if order.customer.name not in customer_spending_per_coffee:
                    customer_spending_per_coffee[order.customer.name] = []
                customer_spending_per_coffee[order.customer.name].append(order.price)

        customer_spending_per_coffee = {key: sum(customer_spending_per_coffee[key]) for key in customer_spending_per_coffee}
        customer_spending_per_coffee = sorted(customer_spending_per_coffee, key = lambda key: customer_spending_per_coffee[key], reverse = True)
        richest_customer = customer_spending_per_coffee[0]

        for order in Order.all:
            if order.coffee == coffee:
                if order.customer.name == richest_customer:
                    return order.customer
        
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if hasattr(self, "price"):
            raise Exception("Cannot reassign price after initialization.")
        elif isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise Exception("Price must be a float between 1.0 and 10.0.")
        
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer must be of type Customer.")
        
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Coffee must be of type Coffee.")