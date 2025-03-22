# Polymorphism Example
# BAD PRACTICE:
# - Type checking (isinstance)
# - Different method names for same operation
# - Hard-coded behavior based on type
# - Tight coupling


class BadShapeProcessor:
    def process_shape(self, shape):
        if isinstance(shape, Rectangle):
            return shape.get_rectangle_area()
        elif isinstance(shape, Circle):
            return shape.calculate_circle_area()
        # Adding new shapes requires modifying this code


# GOOD PRACTICE:
# - Common interface
# - Runtime polymorphism
# - Open for extension
# - Loose coupling
# Benefits:
# 1. Extensibility
# 2. Maintainability
# 3. Flexibility
# 4. Code reuse

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def describe(self):
        return f"This shape has area {self.calculate_area():.2f} and perimeter {self.calculate_perimeter():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c


class ShapeProcessor:
    def total_area(self, shapes):
        return sum(shape.calculate_area() for shape in shapes)

    def print_all_info(self, shapes):
        for shape in shapes:
            print(shape.describe())


if __name__ == "__main__":
    shapes = [Rectangle(5, 3), Circle(4), Triangle(3, 4, 5)]

    processor = ShapeProcessor()
    processor.print_all_info(shapes)
    print(f"Total area: {processor.total_area(shapes):.2f}")

# Understanding @abstractmethod:
# 1. Purpose:
#    - @abstractmethod decorator marks a method that MUST be implemented by all subclasses
#    - It's used to define a common interface that all shape classes must follow
#    - If a subclass doesn't implement the abstract method, it will raise TypeError

# 2. Rules:
#    - Abstract methods can't be instantiated directly:
#      shape = Shape()  # This would raise TypeError
#    - All abstract methods must be implemented in subclasses
#    - Abstract classes can have both abstract and concrete methods (like describe())

# 3. Benefits:
#    - Enforces a contract for subclasses
#    - Ensures consistent interface across different shapes
#    - Enables polymorphic behavior (treating different shapes uniformly)

# Example Output:
# This shape has area 15.00 and perimeter 16.00  # Rectangle
# This shape has area 50.27 and perimeter 25.13  # Circle
# This shape has area 6.00 and perimeter 12.00   # Triangle
# Total area: 71.27

# Invalid Usage Examples (these would raise errors):
# class InvalidShape(Shape):
#     def calculate_area(self):
#         return 0
#     # Missing calculate_perimeter() - This would raise TypeError

# class InvalidShape2(Shape):
#     pass
#     # Missing both abstract methods - This would raise TypeError

# Direct instantiation of abstract class:
# shape = Shape()  # This would raise TypeError
