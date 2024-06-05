import math


def distance_two_points(point1, point2: tuple) -> float:
    # The Euclidean distance between two points (x1, y1) and (x2, y2).
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def circle_perimeter(radius) -> float:
    return 2 * math.pi * radius


def circle_area(radius) -> float:
    return math.pi * radius ** 2


def triangle_area(point1, point2, point3) -> float:
    # The area of a triangle given the coordinates of its vertices.
    return (0.5 * abs(
        point1[0] * (point2[1] - point2[1]) +
        point2[0] * (point3[1] - point1[1]) +
        point3[0] * (point1[1] - point2[1])))
