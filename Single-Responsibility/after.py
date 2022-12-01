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


# we made a separate class that is going to deal with payments
# if we want to change payment methods, we do it here without modifying our Order class!


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
# print(order.status) # open

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")
# print(order.status) # paid

# and we get the same output as before:
# 210
# Processing debit payment type
# Verifying security code: 0372846

print("\nSecond order:\n")
order2 = Order()
order2.add_item("Laptop", 2, 1000)
order2.add_item("AOC Monitor", 1, 300)
order2.add_item("Kingston USB", 3, 20)
print("Total price: ", order2.total_price())
processor2 = PaymentProcessor()
processor2.pay_credit(order2, "1111111")

# Second order:

# Total price:  2360
# Processing credit payment type
# Verifying security code: 1111111
