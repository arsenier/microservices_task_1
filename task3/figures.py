import math

class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def compare_area(self, other):
        return self.area() > other.area()

    def compare_perimeter(self, other):
        return self.perimeter() > other.perimeter()

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

square = Square(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)
circle = Circle(2)

print(square.area())       # 25
print(square.perimeter())  # 20

print(rectangle.area())    # 24
print(rectangle.perimeter())  # 18

print(triangle.area())    # 6
print(triangle.perimeter())  # 12

print(circle.area())      # 12.566370614359172
print(circle.perimeter())  # 12.566370614359172

print(square.compare_area(rectangle))  # This shape has a smaller area than the other shape.
print(square.compare_perimeter(triangle))  # This shape has a larger perimeter than the other shape.