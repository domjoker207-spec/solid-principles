"""Liskov Substitution Principle: subtypes must preserve expected behavior."""

from abc import ABC, abstractmethod


# Bad: Square inherits Rectangle's independent-width-and-height behavior.
# Setting the width silently changes the height, breaking callers' assumptions.
class BadRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class BadSquare(BadRectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height


def resize_to_width(rectangle, width):
    original_height = rectangle.height
    rectangle.set_width(width)
    # This is correct for a rectangle, but fails for BadSquare.
    assert rectangle.area() == width * original_height
    return rectangle.area()


# Good: distinct shapes implement the shared area contract without promising
# rectangle-specific mutable dimensions that a square cannot honor.
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the shape's area."""


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def total_area(shapes):
    """Any Shape can be substituted because callers rely only on area()."""
    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    # In a graphics or reporting application, code can work with any shape
    # through the same stable behavior.
    print(f"Rectangle area after resize: {resize_to_width(BadRectangle(2, 3), 4)}")
    try:
        resize_to_width(BadSquare(3), 4)
    except AssertionError:
        print("BadSquare breaks the rectangle caller's expectation")

    shapes = [Rectangle(4, 3), Square(3)]
    print(f"Combined good-shape area: {total_area(shapes)}")
