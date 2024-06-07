"""
To add a new shape:
1. Add a shape name and its required attributes in the SHAPES.
2. Create a child class with inheritance from the Shape class.
3. Rewrite the perimeter() and area() methods for the child class.
"""

from abc import ABC, abstractmethod
from utils import distance_two_points, circle_perimeter, circle_area, triangle_area


SHAPES = {
    'Square': ('TopRight', 'Side'),
    'Rectangle': ('TopRight', 'BottomLeft'),
    'Circle': ('Center', 'Radius'),
    'Triangle': ('Point1', 'Point2', 'Point3'),
}


def get_instance(class_name, args):
    new_obj = globals().get(class_name)
    return new_obj(*args)


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


    @property
    def perimeter(self):
        return self.get_perimeter()

    @property
    def area(self):
        return self.get_area()


    def __str__(self):
        return ', '.join(SHAPES)


class Rectangle(Shape):
    def __init__(self, topRight, bottomLeft):
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.width = topRight[0] - bottomLeft[0]
        self.height = topRight[1] - bottomLeft[1]

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, topRight, side):
        self.topRight = topRight
        self.height = side[0]
        self.width = self.height


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius[0]

    def get_perimeter(self):
        return circle_perimeter(self.radius)

    def get_area(self):
        return circle_area(self.radius)


class Triangle(Shape):
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.side1 = distance_two_points(point1, point2)
        self.side2 = distance_two_points(point2, point3)
        self.side3 = distance_two_points(point3, point1)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        return triangle_area(self.p1, self.p2, self.p3)
