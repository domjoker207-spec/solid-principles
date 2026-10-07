"""Single Responsibility Principle: keep each class focused on one job."""


# Bad: this class mixes order data, pricing, persistence, and notifications.
# Each concern can change for a different business or technical reason.
class BadOrder:
    def __init__(self, customer_email, items):
        self.customer_email = customer_email
        self.items = items

    def total(self):
        return sum(price for _, price in self.items)

    def save(self):
        print(f"Saving order for {self.customer_email} to the database")

    def send_confirmation(self):
        print(f"Emailing a receipt to {self.customer_email}")


# Good: the order holds order data and its calculation; separate services
# handle persistence and email, which can evolve independently.
class Order:
    def __init__(self, customer_email, items):
        self.customer_email = customer_email
        self.items = items

    def total(self):
        return sum(price for _, price in self.items)


class OrderRepository:
    def save(self, order):
        print(f"Saving order worth ${order.total():.2f}")


class ReceiptSender:
    def send(self, order):
        print(f"Emailing a receipt to {order.customer_email}")


def checkout(order, repository, receipt_sender):
    """Coordinate a real-world checkout without owning its details."""
    repository.save(order)
    receipt_sender.send(order)


if __name__ == "__main__":
    order = Order("customer@example.com", [("book", 18.00), ("pen", 2.50)])
    print(f"Order total: ${order.total():.2f}")
    checkout(order, OrderRepository(), ReceiptSender())
