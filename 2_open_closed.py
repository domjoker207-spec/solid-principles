"""Open/Closed Principle: extend behavior without rewriting stable policy."""

from abc import ABC, abstractmethod


# Bad: every new discount rule requires editing this conditional and risks
# changing the behavior of existing cases.
class BadDiscountCalculator:
    def calculate(self, customer_type, total):
        if customer_type == "regular":
            return total
        if customer_type == "member":
            return total * 0.9
        if customer_type == "holiday":
            return total * 0.8
        raise ValueError(f"Unknown customer type: {customer_type}")


# Good: new discount policies are added as implementations of this contract.
class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        """Return the total after applying this discount."""


class NoDiscount(Discount):
    def apply(self, total):
        return total


class MemberDiscount(Discount):
    def apply(self, total):
        return total * 0.9


class HolidayDiscount(Discount):
    def apply(self, total):
        return total * 0.8


class Checkout:
    def __init__(self, discount):
        self.discount = discount

    def total_due(self, subtotal):
        return self.discount.apply(subtotal)


if __name__ == "__main__":
    # In an online shop, a new promotion can be introduced without changing
    # the checkout calculation used by existing promotions.
    checkout = Checkout(MemberDiscount())
    print(f"Member pays: ${checkout.total_due(100):.2f}")
    print(f"Holiday price: ${Checkout(HolidayDiscount()).total_due(100):.2f}")
