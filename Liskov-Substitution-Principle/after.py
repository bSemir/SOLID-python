from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):

    # one way of fixing this is by removing security_code from pay method
    # and setting it in the initializer
    # so that we can do different things in initializer depending on the type of class we create
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    # like this!
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    # and here
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    # and here
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
# pass email address as a parameter to the initializer
processor = PaypalPaymentProcessor("hi@email.com")
processor.pay(order)

# now, we are properly using the pay method instead of changing what parameters mean
# in order to fit our specific use case
