import pytest
from shapes import Square, Rectangle, Circle, Triangle


class TestSquare:
    @pytest.mark.parametrize("topRight, side, expected", [
        ((1, 1), (1,), 4),
        ((1, 1), (2,), 8)
    ])
    def test_perimeter(self, topRight, side, expected):
        assert Square(topRight, side).perimeter() == expected

    @pytest.mark.parametrize("topRight, side, expected", [
        ((1, 1), (1,), 1),
        ((1, 1), (2,), 4)
    ])
    def test_area(self, topRight, side, expected):
        assert Square(topRight, side).area() == expected


class TestRectangle:
    @pytest.mark.parametrize("topRight, bottomLeft, expected", [
        ((2, 2), (1, 1), 4),
        ((10, 2), (1, 1), 20)
    ])
    def test_perimeter(self, topRight, bottomLeft, expected):
        assert Rectangle(topRight, bottomLeft).perimeter() == expected

    @pytest.mark.parametrize("topRight, bottomLeft, expected", [
        ((1, 1), (2, 2), 1),
        ((10, 2), (1, 1), 9)
    ])
    def test_area(self, topRight, bottomLeft, expected):
        assert Rectangle(topRight, bottomLeft).area() == expected


class TestCircle:
    @pytest.mark.parametrize("center, radius, expected", [
        ((1, 1), (4,), 25.132741228718345),
        ((1, 1), (10,), 62.83185307179586)
    ])
    def test_perimeter(self, center, radius, expected):
        assert Circle(center, radius).perimeter() == expected

    @pytest.mark.parametrize("center, radius, expected", [
        ((1, 1), (4,), 50.26548245743669),
        ((1, 1), (10,), 314.1592653589793)
    ])
    def test_area(self, center, radius, expected):
        assert Circle(center, radius).area() == expected


class TestTriangle:
    @pytest.mark.parametrize("point1, point2, point3, expected", [
        ((5, 5), (8, 8), (10, 2), 16.398147902301346),
        ((1, 5), (-3, 100), (0, 150), 290.17754061647224),
    ])
    def test_perimeter(self, point1, point2, point3, expected):
        assert Triangle(point1, point2, point3).perimeter() == expected

    @pytest.mark.parametrize("point1, point2, point3, expected", [
        ((5, 5), (8, 8), (10, 2), 27.0),
        ((1, 5), (-3, 100), (0, 150), 217.5),
    ])
    def test_area(self, point1, point2, point3, expected):
        assert Triangle(point1, point2, point3).area() == expected
