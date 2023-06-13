import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def compute_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


# Example usage
circle = Circle(5)
area = circle.compute_area()
perimeter = circle.compute_perimeter()

print(f"Radius: {circle.radius}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
