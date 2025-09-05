import math
# Define Class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None
# Rectangle Subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle Subclass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Function to demonstrate polymorphism
def print_area(shape):
    print(f"Shape: {shape.name}, Area: {shape.area()}")
# Instantiate a Rectangle and a Circle
rectangle = Rectangle(6, 4)
circle = Circle(7)
# Call print_area() for each object
print_area(rectangle)
print_area(circle)
